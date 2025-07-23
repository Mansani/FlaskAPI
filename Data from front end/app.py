from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# Replace with your actual connection string
MONGO_URI =  "mongodb+srv://Tharun:1234@cluster0.s8y2nrb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['test_db']
collection = db['submissions']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return render_template('form.html', error="All fields are required.")

        try:
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for('success'))
        except Exception as e:
            return render_template('form.html', error=str(e))

    return render_template('form.html')

@app.route('/success')
def success():
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
