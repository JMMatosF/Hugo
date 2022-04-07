import markdown
import flask
from flask import jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open('a.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)


@app.route('/', methods=['GET'])
def home():
    return jsonify(html)


app.run()


if __name__ == '__main__':
    app.run()
