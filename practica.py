import requests
import pandas as pd

# Consumir el servicio HTTP para una frase específica
def obtener_prediccion(frase):
    url = f'http://127.0.0.1:8080/prediccion/{frase}'
    response = requests.get(url)
    
    if response.status_code == 200:
        prediction = response.json()['prediction']
        return prediction
    else:
        return f'Error al hacer la solicitud HTTP para la frase "{frase}": {response.status_code}'

# Leer un archivo CSV que contiene frases
def leer_csv_y_predecir(archivo_csv):
    # Lee el archivo CSV
    df = pd.read_csv(archivo_csv)
    
    # Itera sobre las filas del DataFrame y hace solicitudes HTTP para cada frase
    for index, row in df.iterrows():
        frase = row['Frase']
        prediction = obtener_prediccion(frase)
        print(f'Frase: "{frase}", Resultado: {prediction}')

# Función principal
def main():
    archivo_csv = 'frases.csv'
    leer_csv_y_predecir(archivo_csv)

if __name__ == "__main__":
    main()
