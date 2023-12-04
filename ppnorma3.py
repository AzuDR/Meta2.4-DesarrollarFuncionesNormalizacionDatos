""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 3. Realizar una función que normalice los datos usando escalado simple que reciba
como parámetro un DataFrame y otro parámetro que sea una lista de columnas a
normalizar. Retornar el DataFrame con los datos normalizados
"""
import pandas as pd

df = "boston_house_prices.csv"
data = pd.read_csv(df)
#print(data)
columnas = ["RM", "TAX"]
#ESCALADA SIMPLE X= (xI)/max
def escsimple(data, columnas):
    datad = pd.DataFrame()
    for col in columnas:
        max = data[col].max()
        datad[f"Esimple-{col}"] = data[col] / max
    return (datad)

print (escsimple (data, columnas))