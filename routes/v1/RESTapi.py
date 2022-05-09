import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

add_post = [
    {
        'post_title': 'algo',
        'post_text': 'text',
    }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction " \
           "novels.</p> "


@app.route('/api/v1/resources/books/all', methods=['GET'])
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
