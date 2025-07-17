
import datetime


# caja_registradora.py

ticket = [
    "1 - beef steak - 30,23",
    "4 - coca cola - 4,20",
    "-2 - coca cola - 1,40",
    "1 - bread - 0,90"
]
# función para calcular el importe total del ticket
def calculate_total_amount(ticket):
    total = 0.0
    tax = 1.16
    
    #recorremos el ticket
    for sale in ticket:
        sale_details = sale.split(" - ")
        units = int(sale_details[0])
        product_name = sale_details[1].capitalize()
        unit_price = float(sale_details[2].replace(",", "."))
        
        # Se evalúa si las unidades son negativas o positivas
        if units < 0:
            total -= unit_price
        else:
            total += unit_price
        # calculamos el total con impuestos
        total_with_tax = total * tax
        
        print(f'Products: {product_name}, Units: {units}, Price: {unit_price * units}')
    # mostramos solo el total con impuestos y fecha actual
    print(f'Total: {total_with_tax}, Date: {datetime.date.today()}')


calculate_total_amount(ticket)