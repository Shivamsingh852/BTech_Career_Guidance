import numpy as np
import pandas as pd

def preprocess_user_data(user):
    """
    Module 2: Data Processing
    Cleans, normalizes, and encodes user input into a feature vector
    that the ML model can consume.
    """
    # 1. Extract raw data from the user database model
    # Providing defaults in case of missing data to prevent crashes
    academic = user.academic_percentage or 0.0
    prog_skill = user.programming_skill or 0
    comm_skill = user.communication_skill or 0
    analy_skill = user.analytical_skill or 0
    interest = user.interests or 'None'
    personality = user.personality_type or 'None'
    
    # 2. Categorical Encoding
    # In a simple B.Tech project, manual mapping or LabelEncoding is easiest to explain in a viva.
    interest_map = {
        'Coding': 0,
        'Design': 1,
        'Management': 2,
        'Data Analysis': 3,
        'None': -1
    }
    encoded_interest = interest_map.get(interest, -1)
    
    personality_map = {
        'Introvert': 0,
        'Extrovert': 1,
        'None': -1
    }
    encoded_personality = personality_map.get(personality, -1)
    
    # 3. Data Normalization / Scaling
    # Normalizing all numerical inputs to a 0.0 - 1.0 scale ensures algorithms 
    # like KNN don't heavily weight the 0-100 academic score over the 1-10 skill scores.
    norm_academic = academic / 100.0
    norm_prog = prog_skill / 10.0
    norm_comm = comm_skill / 10.0
    norm_analy = analy_skill / 10.0
    
    # 4. Construct the Final Feature Vector
    # This must match the exact feature order used during model training in Step 4.
    feature_vector = np.array([[
        norm_academic, 
        norm_prog, 
        norm_comm, 
        norm_analy, 
        encoded_interest, 
        encoded_personality
    ]])
    
    return feature_vector
