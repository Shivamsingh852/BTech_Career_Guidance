import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import random
import os

def generate_synthetic_data(num_samples=2000):
    np.random.seed(42)
    random.seed(42)
    
    data = []
    careers = ['Software Engineer', 'Data Scientist', 'Business Analyst', 
               'Graphic Designer', 'HR Manager', 'Product Manager']
               
    for _ in range(num_samples):
        # Generate random raw features
        academic = random.randint(50, 100)
        prog_skill = random.randint(1, 10)
        comm_skill = random.randint(1, 10)
        analy_skill = random.randint(1, 10)
        interest = random.choice([0, 1, 2, 3]) # 0:Coding, 1:Design, 2:Management, 3:Data Analysis
        personality = random.choice([0, 1]) # 0:Introvert, 1:Extrovert
        
        # Rule-based logic to create a learnable dataset (simulating real-world patterns)
        if interest == 0 and prog_skill >= 7:
            career = 'Software Engineer'
        elif interest == 3 and analy_skill >= 7:
            career = 'Data Scientist'
        elif interest == 2 and comm_skill >= 7 and personality == 1:
            career = 'Product Manager'
        elif interest == 1:
            career = 'Graphic Designer'
        elif comm_skill >= 8 and personality == 1:
            career = 'HR Manager'
        elif analy_skill >= 7 and comm_skill >= 6:
            career = 'Business Analyst'
        else:
            career = random.choice(careers)
            
        # Normalize continuous features EXACTLY as data_processing.py does
        norm_academic = academic / 100.0
        norm_prog = prog_skill / 10.0
        norm_comm = comm_skill / 10.0
        norm_analy = analy_skill / 10.0
        
        data.append([norm_academic, norm_prog, norm_comm, norm_analy, interest, personality, career])
        
    df = pd.DataFrame(data, columns=['Academic', 'Programming', 'Communication', 'Analytical', 'Interest', 'Personality', 'Career'])
    return df

if __name__ == '__main__':
    print("Generating synthetic dataset mapping profiles to careers...")
    df = generate_synthetic_data(2000)
    
    # Save dataset to data/ folder for documentation/presentation purposes
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/synthetic_career_data.csv', index=False)
    
    X = df[['Academic', 'Programming', 'Communication', 'Analytical', 'Interest', 'Personality']]
    y = df['Career']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Decision Tree Classifier...")
    # Using Decision Tree because the tree structure is very easy to visualize and explain in a Viva
    model = DecisionTreeClassifier(max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    print(f"Model Accuracy on Test Data: {accuracy:.2f}%")
    
    # Save the trained model
    os.makedirs('models', exist_ok=True)
    with open('models/career_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Success! Model saved to models/career_model.pkl")
