import pickle
import os

model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'career_model.pkl')
model = None

def load_model():
    global model
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

def predict_career(feature_vector):
    """
    Module 3: AI Recommendation Engine
    Consumes the feature vector and predicts the career.
    """
    if model is None:
        load_model()
    
    if model is None:
        return "Model not trained. Run train_model.py first."
    
    prediction = model.predict(feature_vector)
    return prediction[0]
