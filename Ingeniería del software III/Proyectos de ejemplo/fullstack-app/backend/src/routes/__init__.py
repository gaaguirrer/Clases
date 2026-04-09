from flask import Blueprint

# Define the blueprint for the routes
routes_bp = Blueprint('routes', __name__)

# Import the route handlers
from . import example_routes  # Replace with actual route files as needed

def init_routes(app):
    app.register_blueprint(routes_bp)