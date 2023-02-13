#Ejercicio 6: Descuento en los microprocesadores

def descuentos():
    print("A continuacion tendra una calculadora de descuentos en los microprocesadores")
    print("Eres abonado a COMMAQ o a BEL? (S/N)")
    abonado = input()
    if abonado == "S":
        print("A cual de los 2? (COMMAQ/BEL)")
        abonado = input()
    print("Cuantos microprocesadores quieres comprar?")
    cantidad = int(input())
    if cantidad (10000, 20000):
        print("Tendra un descuento del 10%")
    elif cantidad (20001, 40000 ):
        print("Va a tener un descuento del 15%")
    elif cantidad > 40000:
        print("Le harán un descuento del 20%")
