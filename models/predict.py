import pickle
import pandas as pd
import os


MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)


#ML FLOW SOFTWARE VERSION
MODEL_VERSION = "1.0.0"


class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
    input_df=pd.DataFrame([user_input])
    output=prediction = model.predict(input_df)[0]


    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    
    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))
    confidence_rounded = round(confidence, 4)
    confidence_pct = round(confidence * 100, 1)

    return {
        "predicted_category": prediction,
        "confidence": confidence_rounded,
        "class_probabilities": class_probs,
    }