from flask import Flask, render_template
from API_Call import html_output

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Main_Page.html')

@app.route('/college_search')
def college_search():
    # Render the college_search.html page
    return render_template('college_search.html', html_output)

@app.route("/search")
def search():
    q = request.args.get("q")
    print(q)

    if q:
        results = Song.query.filter(Song.title.icontains(q) | Song.performer.icontains(q)) \
        .order_by(Song.peak_position.asc()).order_by(Song.chart_debut.desc()).limit(100).all()
    else:
        results = []

    return render_template("search_results.html", results=results)


if __name__ == '__main__':
    app.run(debug=True)
