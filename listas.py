alumnos = ["Ana", "Luis", "Paty"]
calif = [9.0, 7.5, 8.2]

print(alumnos[0])  # "Ana"
print(alumnos[-1])  # "Paty"

alumnos.append("Carlos")
alumnos.remove("Luis")

print(len(alumnos))  # 3

for a in alumnos:
    print(a)