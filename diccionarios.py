alumno = {
    "nombre": "Ana López",
    "grupo": "3A",
    "calificaciones": [8.5, 9.0, 7.5]
}

print(alumno["nombre"])  # "Ana López"

alumno["email"] = "ana@mail.com"
alumno["grupo"] = "3B"

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

for valor in alumno.values():
    print(valor)

for clave in alumno:
    print(clave)