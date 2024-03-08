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

if __name__ == '__main__':
    app.run(debug=True)
