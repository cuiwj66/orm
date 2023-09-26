from addnews import add_bp
from model.usermodel import UserModel
from model.newsmodel import NewsModel
from flask_restful import Api,Resource,marshal,fields
from flask import request,render_template,make_response,redirect,session
from init_app import db
api = Api(add_bp)

class Addnews(Resource):
    def get(self):
        uid = request.args.get('uid')
        uname = request.args.get("uname")
        return make_response(render_template('addnews.html',uid = uid,uname=uname))
    def post(self):
        title = request.form.get('title')
        uid = request.form.get('id')
        content = request.form.get('content')
        date = request.form.get('date')
        res = NewsModel(title=title,content=content,time=date,author_id=uid)
        db.session.add(res)
        db.session.commit()
        if res:
            # return redirect("/show/shownews/?id=%s") % uid
            return {"message":"success"}
        else:
            return {"message":"fail"}



api.add_resource(Addnews,"/addnews/")
