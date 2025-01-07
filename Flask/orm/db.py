from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 객체를 생성
db = SQLAlchemy()

# db 객체와 모델클래스를 같은 패일에 위치시킬수도 있음
# 이러면 모델별로 관리하기가 힘듬

# 따로하면 db.init_app(app) 을 사용해서 작업의 일관성을 유지할 수 있다.