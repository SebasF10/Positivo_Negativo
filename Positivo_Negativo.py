# programa para verificar si un numero es positivo o negativo

# input
X = int(input("digite un numero: "))

# processing
if X > 0:
    RTA = "Positivo"
elif X == 0:
    RTA = "su numero es neutro "
else:
    RTA = "negativo"

# output
print("el numero",X,"es",RTA)