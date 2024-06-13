servicios = {"Lavado y Secado" : 0, "Solo lavado": 2, "Solo secado": 3, "Manicure": 4, "Pedicure": 5}
para_lo_que_da = []

for servicio in servicios:
    total = int(input(f"Cuanto quieres pagar por un {servicio}: "))
    servicios[servicio] = total


para_lo_que_da = {servicio: total for servicio, total in servicios.items() if total >= 500}

print("En base a tu respuestas, te da para un:")
for servicio, total in para_lo_que_da.items():
    print(f"{servicio}")