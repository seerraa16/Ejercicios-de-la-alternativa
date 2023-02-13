#Ejercicio 6: Descuento en los microprocesadores

def descuentos():
    print("Descuentos en los microprocesadores")
    print("Eres abonado a COMMAQ o a BEL? (S/N)")
    abonado = input()
    if abonado == "S":
        print("A cual de los 2? (COMMAQ/BEL)")
        abonado = input()
    print("Cuantos microprocesadores quieres comprar?")
    cantidad = int(input())
