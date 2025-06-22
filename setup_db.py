from app import db, create_app
from app.models import Artist, Exhibit, Visitor

app = create_app()

with app.app_context():
    db.create_all()
    print("Табелите се креирани успешно.")
