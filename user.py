from item_manager import show_items, items_list, pick_items
from wallet import Wallet

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)

    # Asegúrate de que estos métodos estén disponibles para la clase
    show_items = show_items
    items_list = items_list
    pick_items = pick_items
