from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db
from .data_processing import preprocess_user_data
from .ml_engine import predict_career
from .resources import get_career_resources
from .chatbot import get_chatbot_response
from .ml_engine import predict_career
from .resources import get_career_resources

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Username already exists.')
            return redirect(url_for('main.register'))
            
        new_user = User(username=username, password=generate_password_hash(password, method='scrypt'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
        
    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.profile'))
        else:
            flash('Please check your login details and try again.')
            
    return render_template('login.html')

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.academic_percentage = float(request.form.get('academic_percentage'))
        current_user.programming_skill = int(request.form.get('programming_skill'))
        current_user.communication_skill = int(request.form.get('communication_skill'))
        current_user.analytical_skill = int(request.form.get('analytical_skill'))
        current_user.interests = request.form.get('interests')
        current_user.personality_type = request.form.get('personality_type')
        
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('main.recommendation'))
        
    return render_template('profile.html', user=current_user)

@main_bp.route('/recommendation')
@login_required
def recommendation():
    if current_user.academic_percentage is None:
        flash("Please complete your profile assessment first.")
        return redirect(url_for('main.profile'))
        
    feature_vector = preprocess_user_data(current_user)
    predicted_career = predict_career(feature_vector)
    resources = get_career_resources(predicted_career)
    
    return render_template('recommendation.html', career=predicted_career, resources=resources)


@main_bp.route('/api/chat', methods=['POST'])
def api_chat():
    user_message = request.json.get('message', '')
    response = get_chatbot_response(user_message)
    return jsonify({'response': response})


from .models import Feedback
@main_bp.route('/submit_feedback', methods=['POST'])
@login_required
def submit_feedback():
    career = request.form.get('career')
    rating = int(request.form.get('rating'))
    comments = request.form.get('comments')
    feedback = Feedback(user_id=current_user.id, predicted_career=career, rating=rating, comments=comments)
    db.session.add(feedback)
    db.session.commit()
    flash('Thank you for your feedback! This helps improve our ML model.')
    return redirect(url_for('main.recommendation'))

import json
import plotly
import plotly.express as px
import pandas as pd

@main_bp.route('/admin')
@login_required
def admin_dashboard():
    if current_user.username != 'admin':
        flash('Access denied: Administrator only.')
        return redirect(url_for('main.index'))
        
    feedbacks = Feedback.query.all()
    if not feedbacks:
        return render_template('admin.html', graphJSON=None, feedbacks=[])
        
    df = pd.DataFrame([{'Career': f.predicted_career, 'Rating': f.rating} for f in feedbacks])
    avg_ratings = df.groupby('Career')['Rating'].mean().reset_index()
    
    fig = px.bar(avg_ratings, x='Career', y='Rating', title='Average User Rating by Predicted Career', range_y=[0, 5])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('admin.html', graphJSON=graphJSON, feedbacks=feedbacks)
