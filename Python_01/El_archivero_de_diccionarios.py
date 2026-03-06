estudiantes =[
    {"nombre": "Ana", "nota": 90},
    {"nombre": "Luis", "nota": 50}
]
for persona in estudiantes:
    if persona["nota"] >= 60:
        print(F" {persona ['nombre']} ha Aprovado")
exit()