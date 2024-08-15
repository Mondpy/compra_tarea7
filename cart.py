
class Cart:
    from item_manager import show_items
    from ownable import set_owner 
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        return sum(item.price for item in self.items)

    def check_out(self):
        total = self.total_amount()
        if self.owner.wallet.balance < total:
            print("😞 Fondos insuficientes en la billetera")
            return

        for item in self.items:
            item.owner.wallet.deposit(item.price)
            self.owner.wallet.withdraw(item.price)
            item.set_owner(self.owner)

        self.items.clear()
        print("🎉 Compra realizada con éxito")


  # Al codificar el método check_out, elimina el pass.
        # Requisitos
        #   - El monto total de la compra de todos los ítems en el carrito (Cart#items) debe ser transferido desde la billetera del dueño del carrito a la billetera del dueño de cada ítem.
        #   - La propiedad de todos los ítems en el carrito (Cart#items) debe ser transferida al dueño del carrito.
        #   - El carrito debe quedar vacío.
        # Consejo
        #   - La billetera del dueño del carrito ==> self.owner.wallet
        #   - La billetera del dueño del ítem ==> item.owner.wallet
        #   - Transferir dinero significa ==> retirar la cantidad de la billetera de (¿quién?) e ingresarla en la billetera de (¿quién?)
        #   - La propiedad del ítem se transfiere al dueño del carrito ==> Cambiar el propietario (item.owner = ?)

