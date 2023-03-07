from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


# --------------------------------------------------------------------------
""" 可以函数名字和url不匹配 """


@app.route("/")
def index():
    return "index"


@app.route("/2")
def index2():
    return "index2"


# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
""" url末尾 """

# 只能用 'http://127.0.0.1:8888/hello', 不能用 'http://127.0.0.1:8888/hello/'
@app.route("/hello")
def h():
    return "Hello"


# 结尾跟不跟'/'都行，输入回车后都会自动变成带'/'的形式
@app.route("/world")
def w():
    return "world"


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
""" url变量 
@app.route("/user/<username>") 和 def user(username) 中使用一致的变量名字 username，否则报错。

"""


@app.route("/user/<username>")
def user(username):
    return f"username: {username}"


# 转化器，在user2()函数中 username 是int类型
# 转换器的默认缺省值是 string
@app.route("/user2/<int:username>")
def user2(username):
    return str(username + 6)


# 可有可无
@app.route("/user3")
@app.route("/user3/<username>")
def user3(username=None):
    return f"username: {username}"


# --------------------------------------------------------------------------
""" HTTP 方法
缺省情况下，一个路由只回应 GET 请求。
"""


@app.route("/http", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        return "POST"
    else:  # GET
        return "GET"


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
""" 渲染模版 """


@app.route("/show")
def show():
    return render_template("home.html")


@app.route("/show2")  # 传数据
def show2():
    # data是在 second.html中的{{data}}的名字，随便起，只要一致
    return render_template("home.html", data="666")


# --------------------------------------------------------------------------


@app.route("/test")
def test():
    return render_template("second.html")


"fff"
if __name__ == "__main__":

    # debug=True，自动重载，默认False

    # host : 默认为127.0.0.1（localhost）
    # port 默认值为5000

    # 内部，
    #  * Running on http://127.0.0.1:8080
    # app.run(port=8080)

    # 外部
    # 设置为'0.0.0.0'或者本机的'192.168.0.2'都行，前者写起来简单
    # app.run(host='192.168.211.225', port=8888)
    app.run(
        debug=True, host="0.0.0.0", port=8888, ssl_context=("server.crt", "server.key")
    )


##########################
"""
python hello.py
"""
# 确保防火墙关闭了
##########################
