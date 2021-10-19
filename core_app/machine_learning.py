import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC


def push_data(data):
    df = pd.DataFrame([data], columns = ["gender","ethnicity","age","infection_department",
    "height","evolution_time","number_active_injuries",
    "ulcer_area","glucantime_dosage"])

    df_proc = process_data(df)
    if load_model(df_proc) == 1:
        return False
    else:
        return True
    # True -> Cure, False -> Fail

def process_data(df):
    dep = df["infection_department"].values[0]

    if dep == "Narino":
        df["infection_department"] = 0
    
    elif dep == "Cauca":
        df["infection_department"] = 2

    elif dep == "Tolima":
        df["infection_department"] = 1
    
    else:
        df["infection_department"] = 3


    scaler = MinMaxScaler() 
    scaled_values = scaler.fit_transform(df) 
    df.loc[:,:] = scaled_values
    return df


def build_model(model, X_train, y_train):
    clf = model
    clf.fit(X_train, y_train)
    
    return clf
def load_model(data):
    smote = pd.read_excel("fake_smote.xlsx")
    original = pd.read_excel("preprocesado.xlsx")

    df = smote.append(original)

    labels = df["cure_or_fail"]
    del df['cure_or_fail']

    svm = SVC(C = 10, gamma = 0.001, kernel = 'linear')
    print(df, labels)
    model = build_model(svm, df, labels)

    return model.predict(data)
