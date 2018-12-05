import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Jose!!! Build Number: " + os.getenv('extra_data', "none")

if __name__ == '__main__':
    app.run()
