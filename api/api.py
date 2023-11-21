from quart import Quart, jsonify
from bot import database

app = Quart(__name__)
data = database.Database()


@app.route("/api/guilds/<guild_id>", methods=["GET"])
def guild_id(guild_id):
    """Gets a guild data with a its given id from our database"""
    return jsonify(data.record("SELECT * FROM Guilds WHERE GuildID = ?", guild_id))


@app.route("/api/guilds", methods=["GET"])
def guilds():
    """Gets all guild data from our database"""
    return jsonify(data.record("SELECT * FROM Guilds"))


@app.route("/api/users/<user_id>", methods=["GET"])
def user_id(user_id):
    """Gets a user's data with its given id from our database"""
    return jsonify(data.record("SELECT * FROM Users WHERE UserID = ?", user_id))


@app.route("/api/users", methods=["GET"])
def users():
    """Gets all user data from our databse"""
    return jsonify(data.record("SELECT * FROM Users"))
