from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value=0>
            <br>
            <textarea rows="4" cols="50" name="text">{0}</textarea>
            <br>
            <input type="submit" value="Submit Query">
        </form> 
    </body>
</html>"""

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form.get('rot'))
    text = request.form.get('text')
    encrypted_text = rotate_string(text,rot)
    encrypted_text =  encrypted_text

    return form.format(encrypted_text)

@app.route("/")
def index():
    encrypted = ""
    return form.format(encrypted)

app.run()