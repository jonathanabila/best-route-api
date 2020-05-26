from routes.best_route.blueprint import setup_blueprint
from server import app

app.register_blueprint(setup_blueprint())
app.testing = True
