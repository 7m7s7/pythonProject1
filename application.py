from flask import Flask
import os

application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev')

if ENV == 'dev':
    pass # ustawienia dla wersji produktowej
else:
    pass # ustawienia dla wersji developerskiej

@application.route('/')
def hello_world():
    if ENV == 'dev':
        return 'tadam'
    else:
        return('<h1> hello cicd </h1>'
               f'<p>Środowisko: {ENV} </p>')

if __name__ == '__main__':
    application.run(debug=True)

