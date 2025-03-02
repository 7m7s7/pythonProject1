from flask import Flask
import os

application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev')

@application.route('/')
def hello_world():
    return('<h1> hello cicd </h1>'
           f'<p>Środowisko: {ENV} </p>')

if __name__ == '__main__':
    application.run(debug=True)

