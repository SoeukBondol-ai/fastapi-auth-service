from app.db.session import engine
from app.db.base import Base
from app.db.models.user import User

Base.metadata.create_all(bind=engine)

print("Database tables created")