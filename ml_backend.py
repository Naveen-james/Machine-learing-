from flask import Flask, render_template, jsonify
import numpy as np
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# Sample dataset generator
def generate_sample_data():
    """Generate sample data for dashboard"""
    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(30, 0, -1)]
    
    return {
        'sales': [np.random.randint(1000, 5000) for _ in range(30)],
        'revenue': [np.random.randint(10000, 50000) for _ in range(30)],
        'users': [np.random.randint(100, 500) for _ in range(30)],
        'dates': dates,
        'categories': ['Product A', 'Product B', 'Product C', 'Product D'],
        'category_sales': [2500, 3200, 1800, 2100]
    }

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/data')
def get_data():
    return jsonify(generate_sample_data())

if __name__ == '__main__':
    app.run(debug=True, port=5000)