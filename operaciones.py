import pandas as pd

def menu():
    print("== MENU PRINCIPAL ==")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def Ejercicio1():
    datos = pd.Series(index=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

    for i in range(len(datos.index)):
        valor = int(input(f"Ingrese el valor para {datos.index[i]}: "))
        datos[datos.index[i]] = valor


    print("Serie de valores: \n", datos)
    print("Serie de los valores ordenada: \n", datos.sort_values())
    print("promedio de los valores: ", datos.mean())
    print("valor minimo de la serie: ", datos.min())
    print("valor maximo de la serie: ", datos.max())
    print("suma de los valores de la serie: ", datos.sum())

    # Determinar meses por encima y por debajo del promedio
    promedio = datos.mean()
    meses_por_encima = datos[datos > promedio]
    meses_por_debajo = datos[datos < promedio]

    print("\nMeses por encima del promedio:")
    for mes, valor in meses_por_encima.items():
        print(f"{mes}: {valor}")

    print("\nMeses por debajo del promedio:")
    for mes, valor in meses_por_debajo.items():
        print(f"{mes}: {valor}")


def ejercicio2():
    cant = int(input("Ingrese la cantidad de libros que desea registrar: "))

    titulos = []
    prestamos = []

    for i in range(cant):
        titulo = input(f"Ingrese el título del libro {i+1}: ")
        prestamo = int(input(f"Ingrese la cantidad de préstamos del libro '{titulo}': "))
        titulos.append(titulo)
        prestamos.append(prestamo)
    
    libros = pd.Series(data=prestamos, index=titulos)
    
    # Mostrar la información
    print("\nInformación de libros y préstamos:")
    print(libros)
    
    # Estadísticas básicas
    print("\nESTADISTICAS DEL MES:")
    print(f"Total de préstamos: {libros.sum()}")
    print(f"Promedio de préstamos: {libros.mean()}")
    print(f"Libro más prestado: {libros.idxmax()} con {libros.max()} préstamos")
    print(f"Libro menos prestado: {libros.idxmin()} con {libros.min()} préstamos")

    # Rotacion de libros
    alta_circulacion = libros[libros > 14]
    baja_circulacion = libros[libros < 15]

    print("\nLibros con alta circulación:")
    for titulo, valor in alta_circulacion.items():
        print(f"{titulo}: {valor}")

    print("\nLibros con baja circulación:")
    for titulo, valor in baja_circulacion.items():
        print(f"{titulo}: {valor}")

if __name__ == "__main__":
    opcion = menu()
    if opcion == 1:
        Ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")