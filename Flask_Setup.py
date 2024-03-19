from flask import Flask, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from API_Call import CollegeSchoolFetcher
import requests

db = SQLAlchemy()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Main_Page.html')

college_search_bp = Blueprint("college_search", __name__)

@college_search_bp.route('/college_search.html', methods=["GET", "POST"])
def college_search():
    if request.method == "POST":
        state = request.form.get("state")
        degree_levels = request.form.get("degree_levels")
        try:
            # Assuming your API key is stored elsewhere (e.g., environment variable)
            colleges = CollegeSchoolFetcher("HRnr80yWE4NsBtYUorM2hHu1EAhRYIIRJpqZ7eDa").fetch_college_data(state, degree_levels)
            return render_template("search_results.html", colleges=colleges)
        except Exception as e:
            print("Error fetching data:", e)
            return "Error fetching data", 500
    else:
        return render_template("college_search.html")

app.register_blueprint(college_search_bp)

if __name__ == '__main__':
    app.run(debug=True)
