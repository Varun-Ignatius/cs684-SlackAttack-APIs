from operator import and_
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests
from sqlalchemy import extract
from flask_cors import CORS
from sqlalchemy import Boolean



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://9mydq7twrs11xmikngyc:pscale_pw_BKggjTt2mzbfaq7DJPPcPjSFRp83w61c5dzrQmBuqn0@aws.connect.psdb.cloud/slackattack-news-usersdatabase?ssl=true'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db= SQLAlchemy(app)

ma = Marshmallow(app)

class User(db.Model):
  __tablename__ = "user_account"
  userName = db.Column(db.String(24), primary_key = True)
  user_pass = db.Column(db.String(32))
  email = db.Column(db.String(40))
  general = db.Column(db.Boolean)
  business = db.Column(db.Boolean)
  entertainment = db.Column(db.Boolean)
  health = db.Column(db.Boolean)
  science = db.Column(db.Boolean)
  sports = db.Column(db.Boolean)
  technology = db.Column(db.Boolean)


  def __init__(self, userName, user_pass, email, general, business, entertainment, health, science, sports, technology):
    self.userName = userName
    self.user_pass =user_pass
    self.email =email
    self.general =general
    self.business = business
    self.entertainment = entertainment
    self.health = health
    self.science = science
    self.sports =sports
    self.technology = technology
   

class UserSchema(ma.Schema):
  class Meta:
    fields = ('userName', 'user_pass', 'email', 'general', 'business', 'entertainment', 'health', 'science', 'sports', 'technology' )

class UserCategorySchema(ma.Schema):
  class Meta:
    fields = ('userName', 'general', 'business', 'entertainment', 'health', 'science', 'sports', 'technology' )

user_Schema = UserSchema(many = True)
user_Category_Schema = UserCategorySchema()

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
    new_user = User(userName, user_pass, email, False, False, False, False, False, False, False)
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

@app.route("/News/<string:userName>", methods = ['GET'])
def news(userName):
   user = User.query.get(userName)
  
   result = user_Category_Schema.dump(user)
   if len(result):
      response = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4ae22761ac7c4d698eff795df06742f0')
      return response.json()
   elif userName == "noUser":
      response = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=4ae22761ac7c4d698eff795df06742f0')
      return response.json()
   else:
       return jsonify({"Code": 401,
        "Message": "Invalid UserName"}) 
   

@app.route("/Categories/<string:userName>", methods = ['GET'])
def categories(userName):
    user = User.query.get(userName)
  
    result = user_Category_Schema.dump(user)
    if len(result):
        return jsonify({"Code": 200,
        "Message": "Valid Username",
        "data": result}) 
    else:
        return jsonify({"Code": 401,
        "Message": "Invalid UserName"}) 

@app.route("/Categories/<string:userName>", methods = ['PUT'])
def updateCategories(userName):

    user = User.query.get(userName)    
    if user is not None:
        user.general = request.json['general']
        user.business = request.json['business']
        user.entertainment = request.json['entertainment']
        user.health = request.json['health']
        user.science = request.json['science']
        user.sports = request.json['sports']
        user.technology = request.json['technology']
        db.session.commit()
        updatedUser = User.query.get(userName)
        result = user_Category_Schema.dump(updatedUser)
        return jsonify({"Code": 200,
        "Message": "Valid Username",
        "data":result}) 
    else:
        return jsonify({"Code": 401,
        "Message": "Invalid UserName"}) 

if __name__ == "__main__":
    app.run(debug=True)