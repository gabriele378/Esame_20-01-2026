import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        pass

    def handle_connected_artists(self, e):

        value = self._view.txtNumAlbumMin
        try:
            if value > 0:
                value = int(value)

        except (ValueError, TypeError):
            self._view.show_alert("Errore")






