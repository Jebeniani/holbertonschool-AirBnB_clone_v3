#!/usr/bin/python3
"""
route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', methods=['GET'])
def send_status():
    """returns the status"""

    resp = {'status': 'OK'}
    return jsonify(resp)


@app_views.route('/stats')
def show_stats():
    """returns the count for all objects"""
    rep = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(rep)
