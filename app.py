from flask import Flask,jsonify


app = Flask(__name__)


@app.route("/signIn", methods = ['GET'])
def signIn():
    return jsonify({"Code": 200,
        "Message": "Signed In Successfully"}) 

@app.route("/signUp", methods = ['POST'])
def signUp():
    return jsonify({"Code": 200,
        "Message": "Signed Up Successfully"}) 


if __name__ == "__main__":
    app.run(debug=True)