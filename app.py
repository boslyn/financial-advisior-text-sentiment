from flask import Flask,render_template,request
import google.generativeai as palm
from textblob import TextBlob

api = "AIzaSyDSOMHPCfvCDEot0nLOsn8VTROVQvDn_sU"
palm.configure(api_key=api)
model={"model":"models/chat-bison-001"}
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA", methods=["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite", methods=["GET","POST"])
def makersuite():
    q=request.form.get("q")
    r = palm.chat(messages=q, **model)
    return(render_template("makersuite.html",r=r.last))

""" @app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html")) """

@app.route("/singapore_joke", methods=["GET","POST"])
def singapore_joke():
    return(render_template("singapore_joke.html"))

@app.route("/text_sentiment", methods=["GET","POST"])
def text_sentiment():
    return(render_template("text_sentiment.html"))

@app.route("/text_sentiment_reply", methods=["GET","POST"])
def text_sentiment_reply():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return render_template('text_sentiment_reply.html', text=text, sentiment=sentiment)



if __name__ == "__main__":
    app.run()