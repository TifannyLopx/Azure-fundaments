import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str)
args = parser.parse_args()

df = pd.read_csv(args.input_data)
print(df.head(10)) ## antes solo lo leia y con el print lo puedo ver también

#este se ejecuta con python 4_Archivo_URI-Read.py --input_data "Datos/datos.csv"