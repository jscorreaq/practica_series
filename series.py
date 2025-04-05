import pandas as pd


pares = pd.Series([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
impares = pd.Series([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

for i in range(len(pares)):

    suma = pares[i] + impares[i]
    resta = pares[i] - impares[i]
    mult = pares[i] * impares[i]
    div = pares[i] / impares[i]

    print(f"Suma {i}: ",suma)
    print(f"Resta {i}: ",resta)
    print(f"Multiplicacion {i}: ",mult)
    print(f"Division {i}: ",div)
