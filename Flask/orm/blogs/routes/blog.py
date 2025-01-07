from flask import jsonify, request
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Blog

blog_blp = Blueprint("Blogs","blogs", description="Operations on blog", url_prefix='/blogs')

# API LIST
# 전체 게시글 불러오기 GET
# 게시글을 작성 POST

@blog_blp.route('/')
class BlogList(MethodView):
    def get(self):
        blogs = Blog.query.all()
        
        return jsonify([{
            "id": blog.id,
            "title":blog.title,
            "content": blog.content,
            "created_at": blog.created_at
        } for blog in blogs])

    def post(self):
        data = request.json
        new_blog=Blog(title=data["title"], content=data["content"],created_at=data["created_at"])
        db.session.add(new_blog)
        db.session.commit()
        
        return jsonify({"msg":"Successfully Created blog"}), 201
    
# 하나의 게시글 불러오기 GET
# 특정 게시글 수정하기 PUT
# 특정 게시글 삭제하기 DELETE

@blog_blp.route("/<int:blog_id>")
class BlogResource(MethodView):
    
    def get(self, blog_id):
        blog = Blog.query.get_or_404(blog_id)
        
        return jsonify({"id":blog.id,
                        "title":blog.title,
                        "content":blog.content,
                        "created_at":blog.created_at})
        
    def put(self, blog_id):
        data = request.json
        
        blog = Blog.query.get_or_404(blog_id)
        blog.title = data["title"]
        blog.content = data["content"]
        db.session.commit()
        
        return jsonify({"msg": "Successfully Updated"})
        
    def delete(self, blog_id):
        blog = Blog.query.get_or_404(blog_id)
        db.session.delete(blog)
        db.session.commit()
        
        return jsonify({"msg": "Successfully delete"})
    