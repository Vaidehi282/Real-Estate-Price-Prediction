import json
import pickle
import numpy as np
import pandas as pd

data_columns = None
locations = None
model = None


def predict_price(location, sqft, bhk, bath):
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    try:
        loc_index = data_columns.index(location)
        x[loc_index] = 1
    except ValueError:
        print(f"Location '{location}' not found in data columns.")
        return None

    x_df = pd.DataFrame([x], columns=data_columns)
    return round(model.predict(x_df)[0], 2)


def get_locations():
    load_saved_artifacts()
    return locations


def load_saved_artifacts():
    global data_columns
    global locations
    global model
    print("Loading artifacts")
    with open('artifacts/columns.json', 'r') as f:
        data = json.load(f)['data columns']
        data_columns = [x for x in data]
        locations = data[3:]

    with open('artifacts/bangalore_home_price_model.pickle', 'rb') as f:
        model = pickle.load(f)


if __name__ == '__main__':
    get_locations()
    print(predict_price('Hegde Nagar', 1000, 2, 2))
    print(predict_price('1st Phase JP Nagar', 2000, 2, 2))
