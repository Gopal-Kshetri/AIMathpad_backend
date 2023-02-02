from keras.models import load_model

def model_load():
    model = load_model('./models/inferenced.keras')
    model.summary()
    