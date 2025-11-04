from flask import Blueprint, jsonify

profile_routes = Blueprint("profile", __name__)

@profile_routes.route("/api/profile", methods=["GET"])
def get_profile():
    return jsonify({"message": "Profile route works!"})
