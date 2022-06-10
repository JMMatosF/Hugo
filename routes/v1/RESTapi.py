import flask
from flask import request, jsonify
from cria_post import cria_post
from utils.parse_input import parse_input

app = flask.Flask(__name__)
app.config["DEBUG"] = True

add_post = [
    [
        parse_input(),
        cria_post(),

    ]
]


@app.route('/', methods=['GET'])
def home():
    return jsonify(add_post)


@app.route('/api/v1/resources/books/all', methods=['POST'])
def api_all():
    return jsonify(add_post)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'post_title' in request.args:
        post_title = int(request.args['post_title'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in add_post:
        if book['post_title'] == post_title:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()

if __name__ == '__main__':
    app.run()
