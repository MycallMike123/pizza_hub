from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # Check if tables exist before creating them
        existing_tables = db.engine.table_names()
        if 'restaurant' not in existing_tables:
            db.create_all()  # Create tables

    return app
