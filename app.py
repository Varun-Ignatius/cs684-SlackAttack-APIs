from operator import and_
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import extract



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://o2oqb95gqjltq49y25jo:pscale_pw_Lhs7iI5zynFOD9WNbkqJP5CI7getwJwq8EwAwImVAvZ@us-east.connect.psdb.cloud/slackattack-news-usersdatabase?ssl=true'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db= SQLAlchemy(app)

ma = Marshmallow(app)

class User(db.Model):
  __tablename__ = "user_account"
  userName = db.Column(db.String(24), primary_key = True)
  user_pass = db.Column(db.String(32))
  email = db.Column(db.String(40))
  


  def __init__(self, userName, user_pass, email):
    self.userName = userName
    self.user_pass =user_pass
    self.email =email
   

class UserSchema(ma.Schema):
  class Meta:
    fields = ('userName', 'user_pass', 'email' )

user_Schema = UserSchema(many = True)

@app.route("/signIn/<string:userName>&<string:password>", methods = ['GET'])
def signIn(userName, password):
    user = User.query.filter(and_(User.userName == userName, User.user_pass == password)).all()
  
    result = user_Schema.dump(user)
    if len(result):
        return jsonify({"Code": 200,
        "Message": "Signed In Successfully"}) 
    else:
        return jsonify({"Code": 401,
        "Message": "Invalid UserName or Password"}) 

@app.route("/signUp", methods = ['POST'])
def signUp():
    userName = request.json['userName']
    user_pass = request.json['user_pass']
    email = request.json['email']
    new_user = User(userName, user_pass, email)
    user = User.query.filter(User.userName == userName).all()
    result = user_Schema.dump(user)
    if len(result):
       return jsonify({"Code": 401,
        "Message": "Username Already Taken"}) 
    else:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Code": 200,
            "Message": "Signed Up Successfully"}) 


if __name__ == "__main__":
    app.run(debug=True)