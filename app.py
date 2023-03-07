from flask import Flask


app=Flask(__name__)


@app.route("/junaid") #localhost:port_number/home
#localhost:port_number/reult_page

def home():
    return "our first flask application"


if __name__=='__main__':
    app.run(debug=True)