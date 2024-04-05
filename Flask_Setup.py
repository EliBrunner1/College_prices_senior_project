from flask import Flask, request, render_template, Blueprint
from API_Call import CollegeSchoolFetcher
import requests

app = Flask(__name__, static_url_path='/static')

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
            colleges = CollegeSchoolFetcher("HRnr80yWE4NsBtYUorM2hHu1EAhRYIIRJpqZ7eDa").fetch_college_data(state, degree_levels)
            return render_template("college_search.html", colleges=colleges)
        except Exception as e:
            print("Error fetching data:", e)
            return "Error fetching data", 500
    else:
        return render_template("college_search.html")

app.register_blueprint(college_search_bp)



if __name__ == '__main__':
    app.run(debug=True)
