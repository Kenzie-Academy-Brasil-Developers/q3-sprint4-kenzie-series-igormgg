from flask import jsonify, request
from psycopg2.errors import UniqueViolation

from app.models.series_model import Series

def series():

    series = Series.read_series()

    series_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

    series_list = [dict(zip(series_keys, serie)) for serie in series]

    return {"data": series_list}, 200

def select_by_id(serie_id):
    try:
        serie = Series.serie_by_id(serie_id)
    
        series_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

        serie = dict(zip(series_keys, serie))

        return {"data": serie}, 200

    except TypeError:
            return {"error": "Not Found"}, 404

def create():
    data = request.get_json()

    data_to_post = {}
    data_to_post['serie'] = data['serie'].title()
    data_to_post['seasons'] = data['seasons']
    data_to_post['released_date'] = data['released_date']
    data_to_post['genre'] = data['genre'].title()
    data_to_post['imdb_rating'] = data['imdb_rating']

    serie = Series(**data_to_post)

    try:
        inserted_serie = serie.create_series()
    
    except UniqueViolation as e:
        return jsonify({'error': e.args}), 422

    series_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

    inserted_serie = dict(zip(series_keys, inserted_serie))

    return jsonify(inserted_serie), 201