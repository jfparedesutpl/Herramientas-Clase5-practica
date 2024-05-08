import pandas as pd
import requests

def obtener_sentimiento(frase):
    url = "http://127.0.0.1:8080/prediccion/" + frase
    response = requests.get(url) #Petición del servicio
    data = response.json()
    return data['prediction']

def main():
    archivo_csv = "Herramientas Practica semana 5/frases.csv"
    df = pd.read_csv(archivo_csv, names=["Frase"], header=None)  # Leer el CSV con Pandas
    for index, row in df.iterrows():
        frase = row["Frase"]
        resultado = obtener_sentimiento(frase)
        print(f"Frase: {frase}, Resultado: {resultado}")

if __name__ == "__main__":
    main()
