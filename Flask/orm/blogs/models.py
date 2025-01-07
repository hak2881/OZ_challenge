from db import db

class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    content=db.Column(db.String(300), nullable=False)
    created_at=db.Column(db.DateTime, default=db.func.current_timestamp())
    
    