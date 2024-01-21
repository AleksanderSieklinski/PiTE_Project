import numpy as np
import pandas as pd
from keras.models import load_model
import os

def predict_if_PumpDump(sciezka_do_pliku, data=None):
    best_model = load_model('Machine_learning/ML_model_and_data/model_epoch_307.hdf5')
    recent_data = pd.read_csv(sciezka_do_pliku) 
    if data is not None:
        recent_data = recent_data[recent_data['Date'] < data].tail(20)   
    else:
        recent_data = recent_data.tail(20)
        
    recent_data = recent_data[['Close', 'compound', 'likes', 'retweets']]
    recent_data = recent_data.values.astype('float32')
    recent_data = np.reshape(recent_data, (1, recent_data.shape[0], recent_data.shape[1]))
    X_recent = recent_data.copy()
    prediction = best_model.predict(X_recent)
    #print(prediction)
    
    ifPumpDump = 0
    if prediction[0][0] < 0.15:
        ifPumpDump = 0
    elif prediction[0][0] < 0.3:
        ifPumpDump = 1
    else:
        ifPumpDump = 2
    print("Zagrozenie w skali 0-2:")
    print("0-brak, 1-potencjalne, 2-wysokie")
    print("Zagrozenie pump&dump dla naszej krypto: ", ifPumpDump)
    return ifPumpDump

#predict_if_PumpDump('csvs/chaincoin_merged.csv')
#predict_if_PumpDump('csvs/chaincoin_merged.csv', '2021-06-08')

