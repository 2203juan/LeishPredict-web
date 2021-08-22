import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def push_data(data):
    df = pd.DataFrame([data], columns = ["eb_lc_sexo","eb_lc_etnia","edad","eb_lc_dpto_infeccion",
    "eb_lc_estatura","eb_lc_tiempo_evolucion","eb_lc_num_lc_activas",
    "eb_lc_ulcera_area_1","eb_lc_tto_mcto_glucan_dosis"])

    df = process_data(df)
    print(df)

def process_data(df):
    df["eb_lc_dpto_infeccion"] = pd.factorize(df["eb_lc_dpto_infeccion"])[0]

    scaler = MinMaxScaler() 
    scaled_values = scaler.fit_transform(df) 
    df.loc[:,:] = scaled_values
    return df

def load_model():
    pass

def predict():
    pass
