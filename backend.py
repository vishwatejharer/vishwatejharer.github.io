from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



app.run(debug=True)
