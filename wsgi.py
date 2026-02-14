from app import create_app, db

app = create_app()

# Create database tables if they don't exist
# This ensures the DB is initialized on Render deployment
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()