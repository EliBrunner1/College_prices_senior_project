from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')


# link to the next page.
@app.route('/college_search')
def college_search():
    # Render the college_search.html page
    return render_template('college_search.html')


if __name__ == '__main__':
    app.run(debug=True)

#test
