from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa base", 28980, seller)
    Item("Fuente de alimentación", 8980, seller)
    Item("Caja de PC", 8727, seller)
    Item("HDD de 3.5 pulgadas", 10980, seller)
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("Refrigerador de CPU", 13400, seller)
    Item("Tarjeta gráfica", 23800, seller)

print("🤖 Por favor, dime tu nombre")
customer = Customer(input())

print("🏧 Por favor, ingresa la cantidad de dinero para cargar en tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Comienza la compra")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor, ingresa el número del producto")
    number = int(input())

    print("⛏ Por favor, ingresa la cantidad de productos")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Monto total: {customer.cart.total_amount()}")

    print("😭 ¿Quieres terminar la compra? (yes/no)")
    end_shopping = input() == "yes"

print("💸 ¿Confirmar la compra? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ Pertenencias de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo de la billetera de {customer.name}: {customer.wallet.balance}")

print(f"📦 Estado del inventario de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo de la billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Monto total: {customer.cart.total_amount()}")

print("🎉 Fin")
