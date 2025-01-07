from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# AIP List
# /board/
# 전체 게시글을 가져오는 API (GET)
# 게시글 작성 (POST)

# get,post,put,delete 등의 메소드를 각각 처리할 수 있는 메서드를 클래스에 정의할 수 있음
@board_blp.route('/')
class BoardList(MethodView) : # HTTP 메소드 별로 클래스를 정의할 수 잇께 해주는 기능을 제공
    def get(self):
        boards = Board.query.all() # board 테이블 안에 있는 모든 컬럼 가져옴 join 할필요가 없네?
        # 전부 가져왔으니까 하나씩 추리자
        # for board in boards:
        #     print("id:",board.id)
        #     print("title:",board.title)
        #     print("content:",board.content)
        #     print("userid:",board.user_id)
        #     print("author:",board.author) # user 니까 user 모델에서또 접근할수 있다
        #     print("author:",board.author.name)
        #     print("author:",board.author.email)
        
        # 더 간결히
        return jsonify([{"id": board.id, 
                        'title':board.title,
                        'content':board.content,
                        'user_id': board.author.id,
                        'author_name': board.author.name} 
                        for board in boards])
            
        # return 'success'
    def post(self):
        data = request.json # 유저가 보낸 데이터를 json 으로 받겠다.
        new_board = Board(title=data['title'], content=data['content'],user_id=data['user_id']) # 게시글을 만들려면 모델 자체를 불러와야함, 필요한 것들을 다적어서
        db.session.add(new_board) # 이객체를 추가해주세요
        db.session.commit()  # 커밋만 하면 뭘 커밋할건지 모름
        
        return jsonify({'msg': 'success create board'}), 201

# /board/<int:board_id>
# 하나의 게시글 불러오기 (GET)
# 특정 게시글 수정하기 (PUT)
# 특정 게시글 삭제하기 (DELETE)

@board_blp.route("/<int:board_id>")
class BoardResource(MethodView): # 하나만 만들거임, 보드가 모듈로 임포트 되있기에 board로 하면 안됨 이름
    def get(self,board_id): # 아이디를 갖고있는 상태에서 시작하기에 함수에서 받고 시작
        board = Board.query.get_or_404(board_id) # 보드아이디가 존재하면 받고 없으면 404 띄워라
        
        return jsonify({'id':board.id,
                        'title':board.title,
                        'content':board.content,
                        'author':board.author.name})
    
    def put(self, board_id): # orm 방식 우선 가져와
        board = Board.query.get_or_404(board_id)
        
        data = request.json # 유저가 json 형태로 보여주는 데이터를 담아주는거임 어떤 내용을 업데이트 시킬건지
        
        board.title = data['title'] # 갚 덮어쓰기 한거임 받아온거에
        board.content = data['content']
        
        db.session.commit() # 데이터가 바뀐것을 알려야함
        
        return jsonify({'msg' : 'Successfuly updated board data'}), 201
        
        # 포스트맨에서 put으로 바꿔서 해보자
    
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        
        db.session.delete(board)
        db.session.commit()

        return jsonify({"msg":"Successfully delete board data"}), 201
    