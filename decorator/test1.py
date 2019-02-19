

def hello(f):
    def inner(*args,**kwargs):
        return f(*args,**kwargs)
    return inner

@hello
def  test():
    print("hello world!")


def auth(func):
    def inner(*args,**kwargs):
        au =session.get("username")
        if au:
            return func(*args,**kwargs)
        else:
            return render_template("login.html")
    return inner

def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        username=session.get("username")
        if not username:
            return redirect("/login")
        return func(*args,**kwargs)
    return inner
