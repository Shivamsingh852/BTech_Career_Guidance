import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# A basic corpus for offline TF-IDF matching (No heavy external API required)
qa_corpus = [
    ("What does a software engineer do?", "Software engineers design, develop, and test software applications and systems. They write code in languages like Python, Java, or C++."),
    ("How do I become a data scientist?", "To become a data scientist, focus on learning Python or R, statistics, machine learning, and data visualization tools like Tableau."),
    ("What skills are needed for a business analyst?", "Business analysts need strong communication, analytical thinking, SQL, Excel, and an understanding of Agile methodologies."),
    ("Tell me about graphic design.", "Graphic designers create visual concepts using software like Adobe Photoshop and Illustrator to communicate ideas that inspire and inform."),
    ("What is HR management?", "HR managers plan, direct, and coordinate the administrative functions of an organization. They oversee recruiting, interviewing, and hiring."),
    ("What is product management?", "Product managers guide the success of a product and lead the cross-functional team responsible for improving it.")
]

questions = [q for q, a in qa_corpus]
answers = [a for q, a in qa_corpus]

# Train the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_chatbot_response(user_message):
    """
    Module 6: NLP Chatbot Integration
    Uses TF-IDF + Cosine Similarity for offline matching.
    Optionally falls back to OpenAI if configured in the environment.
    """
    # 1. OPTIONAL: Check for OpenAI API Key in environment
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key and OpenAI:
        try:
            client = OpenAI(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful B.Tech career guidance counselor. Keep answers under 3 sentences."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=100
            )
            return response.choices[0].message.content
        except Exception as e:
            print("OpenAI API failed, falling back to offline NLP matching.", e)

    # 2. OFFLINE NLP: TF-IDF Matching
    user_vector = vectorizer.transform([user_message])
    similarities = cosine_similarity(user_vector, question_vectors)
    
    best_match_idx = np.argmax(similarities)
    best_match_score = similarities[0][best_match_idx]
    
    # Threshold for relevance
    if best_match_score > 0.2:  
        return answers[best_match_idx]
    else:
        return "I'm a simple career chatbot! Try asking me 'What does a software engineer do?' or 'How do I become a data scientist?'. (To enable advanced AI answers, add an OPENAI_API_KEY to the environment variables)."
