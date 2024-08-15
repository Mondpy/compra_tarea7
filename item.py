class Item:
    instances = []
    from ownable import set_owner 
    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Cuando se crea una instancia de Item, esa instancia (self) se almacena en la variable de clase instances.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Devuelve instances ==> Esto significa que Item.item_all() devuelve todas las instancias de Item que se han creado hasta ahora.
        return Item.instances