# Model -> Table 생성
# 게시글 - board
# 유저 - user

from db import db

# 나중에는 models 폴더안에 User.py 이런식으로 여러개를 만드는게 좋다ㅠ 
class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False ) # Varchar 가 없어 파이썬으로 표현
    email = db.Column(db.String(100), unique=True, nullable = False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic') # author을 역참조 이것을 사용해서도 보드 테이블을 불러오지 않고 셀렉
    
    # lazy = 'dynamic' 실제로 데이터를 가져오지 않고 있다고 만 알려줌
    # 모든글을 한번에 업로드하지 않고 특정 글만 업로드
    
class Board(db.Model):
    __tablename__ = "boards"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # 원래는 foreignkey 로 연결하는거에 그쳤다면 ORM방식은 역참조 라는 방식이 있다
    author = db.relationship('User', back_populates='boards') 