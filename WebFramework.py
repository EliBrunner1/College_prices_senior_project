#this is web-frame work it will be using flask
from flask import Flask, render_template, request


app = Flask(__name__)

# Mock function to calculate acceptance chance based on GPA
def calculate_acceptance_chance(gpa):
    # Replace this with your actual logic to calculate acceptance chance
    if gpa >= 3.0:
        return "High"
    elif gpa >= 2.5:
        return "Medium"
    else:
        return "Low"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        gpa = float(request.form['gpa'])
        acceptance_chance = calculate_acceptance_chance(gpa)
        return render_template('result.html', gpa=gpa, acceptance_chance=acceptance_chance)

if __name__ == '__main__':
    app.run(debug=True)
