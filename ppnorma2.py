""""
Azucena Dominguez Romero 951
17 de Octubre de 2023
PROBLEMA 2. Realizar una función que normalice los datos usando Z-Score que reciba como
parámetro un DataFrame y otro parámetro que sea una lista de columnas a
normalizar. Retornar el DataFrame con los datos normalizados.

"""
import pandas as pd

df = "boston_house_prices.csv"
data = pd.read_csv(df)
#print(data)
columnas = ["RM", "TAX"]
#CALCULO Z-CORE X=(Xi - Promedio)/std
def zscore(data, columnas):
    datad = pd.DataFrame()
    for col in columnas:
        prom = data[col].mean()
        std= data[col].std()
        datad[f"zscore-{col}"] = (data[col] - prom) / std
    return (datad)

print(zscore (data, columnas))