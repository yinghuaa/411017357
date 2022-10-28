from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 411016937 韓志偉的求職相關資訊</h1>"
    homepage += "<a href=/profile>我的個人簡介</a><br><br>"
    homepage += "<a href=/introduce>MIS相關工作介紹</a><br><br>"
    homepage += "<a href=/UCAN>職涯測驗結果</a><br><br>"
    homepage += "<a href=/autobiography>求職履歷自傳</a><br><br>"
    return homepage

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/introduce")
def introduce():
    return render_template("introduce.html")

@app.route("/UCAN")
def UCAN():
    return render_template("UCAN.html")

@app.route("/autobiography")
def autobiography():
    return render_template("autobiography.html")

#@app.route("/account", methods=["GET", "POST"])
#ef account():
    #if request.method == "POST":
     #   user = request.form["user"]
      #  pwd = request.form["pwd"]
       # result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        #return result
    #else:
     #   return render_template("account.html")


#if __name__ == "__main__":
#    app.run()