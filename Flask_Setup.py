from flask import Flask, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from API_Call import CollegeSchoolFetcher
import requests
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Main_Page.html')

college_search_bp = Blueprint("college_search", __name__)

@college_search_bp.route('/college_search.html')
def college_search_page():
    # Render the college_search.html page
    return render_template('college_search.html')

@college_search_bp.route("/search", methods=["GET", "POST"])
def search():
    q = request.args.get("q")
    print(q)
    # q = query user will search from "q" and it will be searched by the name of college, price, state, etc.
    if q:
        results = CollegeSchoolFetcher.query.filter(CollegeSchoolFetcher.school_name.icontains(q) | CollegeSchoolFetcher.school_state.icontains(q)) \
            .order_by(CollegeSchoolFetcher.instate_tuition.asc()).order_by(CollegeSchoolFetcher.outstate_tuition.asc()).limit(100).all()
    else:
        results = []
    return render_template("search_results.html", results=results)

app.register_blueprint(college_search_bp)

if __name__ == '__main__':
    app.run(debug=True)
