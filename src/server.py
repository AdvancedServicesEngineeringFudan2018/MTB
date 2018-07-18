from flask import request, render_template
from flask_bootstrap import Bootstrap
from flask_stupe import paginate, schema_required
from flask_stupe.json import Stupeflask
from marshmallow import Schema
from marshmallow.fields import String
from pymongo import MongoClient

app = Stupeflask(__name__)
users = MongoClient().database.users
bootstrap = Bootstrap(app)

class UserSchema(Schema):
    username = String(required=True)
    password = String()

@app.route("/", methods=["GET"])
def main():
    return render_template("map.html")


@app.route("/user", methods=["POST"])
@schema_required(UserSchema)
def post_user():
    result = users.insert_one(request.schema)
    request.schema.update(_id=result.inserted_id)
    return request.schema


@app.route("/user/<ObjectId:id>")
def get_user(id):
    return users.find_one({"_id": id})


@app.route("/users")
@paginate(limit=100)
def get_users():
    return users.find()

if __name__ == "__main__":
    app.debug = True
    app.run()