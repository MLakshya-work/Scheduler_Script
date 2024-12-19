from flask import Flask
from app.routes import routes

app = Flask(__name__)  # Flask will now automatically look for templates in the root folder
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)

