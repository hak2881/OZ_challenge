from flask import Flask
from flask_smorest import Api
from db import db
from models import Blog

app = Flask(__name__)
# sqlachemy 를 통해 database에 접속할 수 있는 명령어
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pwd@localhost/oz'
# 객체가 바뀔때마다 trackking 하면 메모리에 너무 부하가 심해 왠만하면 false로 사용
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app) # db 선정

# blueprint 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app) # smorest 를 사용할수있게 flask 와 api 연결, 블루프린터 사용가능

from routes.blog import blog_blp # 등록!!

api.register_blueprint(blog_blp) # 만들엇으니 이제 등록


from flask import render_template 
@app.route('/manage-blog')
def manage_boards():
    return render_template('blogs.html')

if __name__ == "__main__" :
    with app.app_context(): # Flask 애플리케이션 컨텍스트를 수동으로 생성하고, 컨텍스트 안에서 작업을 수행할 수 있게 합니다.
        db.create_all() # 이거를 하면 models 에 만들어진 테이블들이 전부 만들어짐
        
    app.run(debug=True)