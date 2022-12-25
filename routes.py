from flask import *
from models import *


def register_routes(app):
    app.register_blueprint(api_bp)


#API ROUTES
api_bp = Blueprint('api_v01', __name__, url_prefix="/api/v0.1/")

@api_bp.route('/session', methods=["GET"])
def get_sessions():
    session = get_session()
    return jsonify([i.json() for i in session.query(GameSession).all()])


#USER ROUTES