import random 
senha = ""
caracteres = "zaq12xvfr5683214msply"

for digito in range (6):
    aleatorio = random.choice(caracteres)
    senha += aleatorio 
    print("-" * 20)
    print(senha)
    print("-" * 20) 
    
