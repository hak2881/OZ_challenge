from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView # 데이터베이스 CRUD 방식 사용을 위해
from db import db # 데이터 베이스 조회
from models import User # 유저데이터 모델 불러오기

# 라우팅 작업
user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix='/user')

# 설정한거 app.py 에서 등록하자 이제

# API LIST :
# 전체 유저 데이터 조회 (GET)
# 유저 생성 (POST)

@user_blp.route('/') # 라우트 경로 를 새로추가하면 flask 정지시켰다가 다시 실행 해야 적용됨
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        return jsonify([{'id':user.id,
                        'name':user.name,
                        'email':user.email} 
                        for user in users])
    
    def post(self):
        data = request.json # 유저로부터 받자 postman
        # 포스트맨에서 post -> body -> raw
        # {"name":"python","eamil":"python@gmail.com"}
        
        new_user = User(name=data['name'], email=data['email']) # 만들고 new_user 객체에 담기
        
        db.session.add(new_user) # 새로운 유저를 추가해주세요
        db.session.commit()
        
        return jsonify({"msg":"Successfully created new user"}), 201

# 특정 유저 데이터 조회 (GET)
# 특정 유저 데이터 업데이트 (PUT)
# 특정 유저 데이터 삭제 (DELETE)

@user_blp.route("/<int:user_id>")
class UserResource(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({'name':user.name,'email':user.email})
    def put(self, user_id):
        pass
        user = User.query.get_or_404(user_id)
        data = request.json
        
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        
        return jsonify({"msg":"Successfully updated user"}), 201
        

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({"msg":"Successfully delete user"}), 201