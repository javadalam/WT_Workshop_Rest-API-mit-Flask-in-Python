from flask import Flask
from flask_restful import Resource, Api 
 
app = Flask(__name__)
api = Api(app)

class People(Resource):
    def get(self, Name, Age):
        return{"name" : Name , "age" : Age }
    
    # def post(self, Adresse):
       # return{"adresse" : Adresse}
       #<string:Adresse>

api.add_resource(People,"/people/<string:Name>/<int:Age>")

if __name__ == "__main__":
    app.run(debug=True)