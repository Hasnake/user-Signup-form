from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eeeeee;
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
      <!-- create your form here -->
    <form method="post">
        <label>Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <br><br>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Query"/>
    </body>
</html>
"""
def index():
    return "Hello World"

app.run()
