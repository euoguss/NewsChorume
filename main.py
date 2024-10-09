from flask import Flask, Blueprint, url_for
from routes.home import home_route

app = Flask(__name__)
app.register_blueprint(home_route)



app.run(debug=True)