import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self._albums_list = []
        self.load_all_artists()
        self._artisti_stesso_genere = DAO.get_artisti_stesso_genere()

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        self._albums_list = DAO.get_albums(min_albums)



    def build_graph(self):

        self._graph.clear()

        for album in self._albums_list:
            artist_id_album = album['artist_id']


            for artist in self._artists_list:
                artist_id = artist['id']


                if artist_id == artist_id_album:
                    self._graph.add_node(artist)


                    for artist1 in self._artists_list:
                        for artist2 in self._artists_list:
                            generi_comuni = ""

                            if artist1['id'] != artist2['id'] and "il genere è uguale tra i due artisti":
                                self._graph.add_edge(artist1, artist2, weight = generi_comuni)






