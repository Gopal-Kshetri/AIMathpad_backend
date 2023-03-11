from keras.models import load_model

def model_load():
    # model = load_model('./models/inferenced.keras')
    model = load_model('./models/weights2.pth')
    model.summary()
    