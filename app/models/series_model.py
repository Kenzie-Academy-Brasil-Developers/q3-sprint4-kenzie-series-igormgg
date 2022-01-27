from app.models import DatabaseConnector

class Series(DatabaseConnector):
    def __init__(self, *args, **kwargs):
        self.serie = kwargs['serie']
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre']
        self.imdb_rating = kwargs['imdb_rating']

    def create_series(self):
        self.get_conn_cur()

        query = """
            INSERT INTO
                ka_series (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s ,%s, %s)
            RETURNING *
        """

        query_values = list(self.__dict__.values())

        self.cur.execute(query, query_values)

        inserted_serie = self.cur.fetchone()

        self.commit_and_close()

        return inserted_serie

    @classmethod
    def read_series(cls):
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series;"

        cls.cur.execute(query)

        series = cls.cur.fetchall()

        cls.commit_and_close()

        return series

    @classmethod
    def serie_by_id(cls, serie_id):
        cls.get_conn_cur()
        
        query = "SELECT * FROM ka_series WHERE id = %s"
        
        query_id = str(serie_id)

        cls.cur.execute(query, query_id)

        serie = cls.cur.fetchone()

        cls.commit_and_close()

        return serie