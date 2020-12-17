# coding: utf-8
import json


def test_add_component(client):
    """Test case for add_component

    Create a new component
    """
    component = {"name": "name", "title": "title"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.open(
        "/component",
        method="POST",
        headers=headers,
        data=json.dumps(component),
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.json["name"] == "name"
    assert response.json["title"] == "title"


def test_delete_component(client, component):
    """Test case for delete_component

    Delete a single component
    """
    response = client.open(
        "/component/{component_id}".format(component_id=component.id), method="DELETE"
    )
    assert response.status_code == 200


def test_get_component(client, component):
    """Test case for get_component

    Get a single component
    """
    headers = {
        "Accept": "application/json",
    }
    response = client.open(
        "/component/{component_id}".format(component_id=component.id), method="GET", headers=headers
    )
    assert response.status_code == 200
    assert response.json["name"] == component.name
    assert response.json["title"] == component.title


def test_get_component_list(client, component):
    """Test case for get_component_list

    Get a list of components
    """
    headers = {
        "Accept": "application/json",
    }
    response = client.open("/component", method="GET", headers=headers)
    assert response.status_code == 200
    assert len(response.json["components"]) == 1
    assert response.json["components"][0]["name"] == component.name
    assert response.json["components"][0]["title"] == component.title


def test_update_component(client, component):
    """Test case for update_component

    Update a single component
    """
    updated_component = {"name": "updated_name", "title": "updated_title"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.open(
        "/component/{component_id}".format(component_id=component.id),
        method="PUT",
        headers=headers,
        data=json.dumps(updated_component),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json["name"] == "updated_name"
    assert response.json["title"] == "updated_title"
