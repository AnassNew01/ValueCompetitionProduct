from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get form data
    location = request.form['location']
    categories = request.form['categories']
    #price = request.form['price']

    # Yelp API code
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer me9I9-TguqVtEblYhIrQK8lrIa06QjKoSRqZgLltU0ywXHnpYZ2_rlBUpru99uZ3ddJN7xJTcMNSes6gI8lGfhJK7h9f6XH_aNnzQbQ5xLI5Pi6-Ucc1qHs1Fd1QZHYx'
    }
    params = {
        'location': location,
        'categories': categories,
        #'price': price,
        'limit': 50
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)

    # Render results template with data
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
