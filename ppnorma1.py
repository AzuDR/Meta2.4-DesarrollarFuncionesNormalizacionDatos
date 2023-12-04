""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 1.Realizar una función que normalice los datos usando min-max que reciba como
parámetro un DataFrame y otro parámetro que sea una lista de columnas a normalizar.
Retornar el DataFrame con los datos normalizados.
"""
import pandas as pd

df = "boston_house_prices.csv"
data = pd.read_csv(df)
#print(data)
columnas = ["RM", "TAX"]
#CALCULO MIN-MAX X=(xi-min)/(max-min)
def minmax(data, columnas):
    datad = pd.DataFrame()
    for col in columnas:
        max = data[col].max()
        min = data[col].min()
        datad[f"MINMAX-{col}"] = (data[col] - min) / (max - min)
    return (datad)

print(minmax (data, columnas))