import markdown
import flask
import main

app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open(main.filename, 'r') as f:
    text = f.read()
    html = markdown.markdown(text)


@app.route('/', methods=['GET'])
def home():
    return html


app.run()


if __name__ == '__main__':
    app.run()
