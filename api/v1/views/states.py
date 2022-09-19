#!/usr/bin/python3
"""view for State objects that handles all default RESTFul API actions"""
from curses import meta
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, make_response, request, abort


@app_views.route('/states', strict_slashes=False,
                 methods=['GET'])
def get_states():
    """get all states"""
    states = []
    all = storage.all("State").values()
    for s in all:
        states.append(s.to_dict())
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_id(state_id):
    """get state by state_id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_id(state_id):
    """delete by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    data = request.get_json()
    state.name = data['name']
    state.save()
    return jsonify(state.to_dict()), 200
