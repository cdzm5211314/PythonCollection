# -*- coding:utf-8 -*-
# @Desc : Flask框架小示例
# @Author : Administrator
# @Date : 2019-05-15 15:00

from flask import Flask
from flask import request  # 获取请求信息
from flask import render_template  # 返回模版数据
from flask import redirect  # url重定向
from flask import url_for   # url反向路由
from flask import jsonify   # 返回json字符串
from flask_sqlalchemy import SQLAlchemy  # 强大的关系型数据库框架
from flask_wtf import FlaskForm  # 页面表单模型类
from wtforms import StringField  # 表单字段字符串类型
from wtforms import SubmitField  # 表单提交按钮
from wtforms.validators import DataRequired  # 表单字段验证器

"""
pip install flask-sqlalchemy
pip install flask-mysqldb
pip install flask-wtf
"""

### 创建flask的应用对象: 参数内容如下
# 参数: __name__ 在此表示当前模块的名字
# 模块名,flask以这个模块所在目录为总目录,默认这个目录中的static为静态目录,templates为模版目录
# 参数: static_url_path = "/python3"      # 访问静态资源的url前缀,默认值为static
# 参数: static_folder = "static"          # 静态文件的目录,默认就是static
# 参数: template_folder = "templates"     # 模版文件的目录,默认就是templates
app = Flask(__name__)


### 使用类配置参数
class Config(object):
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/pythondb"
    # 设置sqlalchemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # form表单需要配置secret_key信息,form表单需要添加csrf_token
    SECRET_KEY = "PythonDemo"
app.config.from_object(Config)


### 定义数据库表的模型类
db = SQLAlchemy(app)
# 定义作者模型类
class Author(db.Model):
    __tablename__ = "tbl_authors"  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # primary_key 主键
    name = db.Column(db.String(32), unique=True)  # unique 唯一
    books = db.relationship("Book",backref="author")  # ???
    def __repr__(self):
        return "<Author: %s>" %self.name
# 定义书籍模型类
class Book(db.Model):
    __tablename__ = "tbl_books"  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # primary_key 主键
    name = db.Column(db.String(64), unique=True)  # unique 唯一
    author_id = db.Column(db.Integer,db.ForeignKey("tbl_authors.id"))  # .ForeignKey 外键
    def __repr__(self):
        return "<Book: %s>" %self.name

### 创建表单模型类
class AuthorBook(FlaskForm):
    author_name = StringField(label="作者",validators=[DataRequired(u"作者名字必须填写")])
    book_name = StringField(label="书籍",validators=[DataRequired(u"书籍名字必须填写")])
    submit = SubmitField(label="保存")

### 编写视图函数
@app.route("/", methods=["GET","POST"])
def index():
    # 创建表单对象
    form = AuthorBook()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name = author_name)
        db.session.add(author)
        db.session.commit()  # 此处要先提交作者的数据到数据库,后面才能得到author_id的值
        book = Book(name = book_name, author_id= author.id)
        # book = Book(name = book_name, author= author)  # 根据此定义 books = db.relationship("Book",backref="author")  # ???
        db.session.add(book)
        db.session.commit()

    # 查询数据库的所有作者信息
    author_li = Author.query.all()
    return render_template("index.html",authors = author_li,form=form)

# /delete_book  post  json
# {book_id : data}
# @app.route("/delete_book", methods=["POST"])
# def delete_book():
#     # 获取请求信息
#     # 如果前端发送的请求数据是json数据,get_json()会解析成字典数据
#     # get_json() 要求前端发送的数据类型: "content-Type":"application/json"
#     req_dict = request.get_json()
#     book_id = req_dict.get("book_id")
#
#     # 先根据id查询数据,然后再删除数据
#     book = Book.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#
#     # return redirect(url_for("index"))
#     # 返回到前端的数据类型: "content-Type":"application/json"
#     return jsonify(code=0,message = "OK")

# /delete_book?book_id = xxx
@app.route("/delete_book", methods=["GET"])
def delete_book():
    # 获取请求信息
    book_id = request.args.get("book_id")

    # 先根据id查询数据,然后再删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == '__main__':
    # db.drop_all()   # 数据库中有表的时候删除表
    # db.create_all() # 根据模型类创建表

    # 构建数据库数据
    # author_wo = Author(name="我吃西红柿")
    # author_yu = Author(name="鱼人二代")
    # author_tang = Author(name="唐家三少")
    # db.session.add_all([author_wo,author_yu,author_tang])
    # db.session.commit()

    # book_wo = Book(name="星辰变",author_id=author_wo.id)
    # book_wo2 = Book(name="吞噬星芒",author_id=author_wo.id)
    # book_yu = Book(name="校花的贴身高手",author_id=author_yu.id)
    # book_tang = Book(name="善良的死神",author_id=author_tang.id)
    # db.session.add_all([book_wo, book_wo2, book_yu,book_tang])
    # db.session.commit()

    app.run(debug=True)  # 启动Flask程序


