import json
from os import environ
import pytest
from flask import Flask
from app.application import configure, blueprint


@pytest.fixture()
def client():
    app = Flask(__name__)
    configure("application.properties")
    app.register_blueprint(blueprint)
    return app.test_client()


def test_post(client):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = {
        'id': 1,
        'name': 'scott'
    }
    response = client.post('/api', data=json.dumps(data), headers=headers)
    assert response.status_code == 201


def test_put(client):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = {
        'name': 'tiger'
    }
    response = client.put('/api/1', data=json.dumps(data), headers=headers)
    assert response.status_code == 200


def test_get(client):
    response = client.get('/api/1')
    assert response.status_code == 200


def test_delete(client):
    response = client.delete('/api/1')
    assert response.status_code == 200
