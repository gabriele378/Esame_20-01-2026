from database.DB_connect import DBConnect
from model.album import Album
from model.artist import Artist
from model.genre import Genre


class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result



    def get_albums(self, min_albums):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT SUM(album) as somma_album
                FROM album a
                WHERE somma_album >= %s
                """
        cursor.execute(query,(min_albums,))
        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result



    def get_artisti_stesso_genere(self):
            conn = DBConnect.get_connection()
            result = []
            cursor = conn.cursor(dictionary=True)
            query = """
                    SELECT a.artist_id , g.name
                    FROM genre g, album a , track t
                    WHERE a.id = t.album_id and t.genre_id = g.id
                    """
            cursor.execute(query)
            for row in cursor:
                result.append(row['artist_id'],row['name'])
            cursor.close()
            conn.close()
            return result