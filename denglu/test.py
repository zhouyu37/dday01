# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect,session,Response
import functools
app = Flask(__name__)
app.secret_key="aaaaa"

#app.config.from_object('settings.DevConfig')

def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        au =session.get("username")
        if au:
            return func(*args,**kwargs)
        else:
            return redirect('/login')
    return inner

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", **{"msg": ""})
    else:
        username=request.form.get("username")
        password=int(request.form.get("password"))
        if username == "alex" and password == 123:
            session['username']=username
            return redirect("/index")
        else:
            return render_template("login.html",**{"msg":"wrong username or password"})


@app.route("/index")
@auth
def index():
    return render_template("index.html")

@app.route("/order",methods=["GET"])
@auth
def order():
    return Response("order")

@app.route("/logout")
@auth
def logout():
    del session["username"]
    return redirect("/login")

if __name__=="__main__":
    app.run()