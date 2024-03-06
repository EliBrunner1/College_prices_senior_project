from flask import Flask, render_template
from forms import SearchForm
from API_Call import html_output

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return render_template('Main_Page.html')

@app.route('/college_search')
def college_search():
    # Render the college_search.html page
    return render_template('college_search.html', html_output=html_output)

@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        search_query = form.search_query.data
        # Process the search query (e.g., query your database)
        # Return search results to display on another page
        # Example: return render_template('results.html', results=results)
    return render_template('search.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
