# coding: utf-8
import json


def test_add_version(client, component):
    """Test case for add_version

    Create a new version
    """
    version = {"component": component.name, "version": "1.0"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.open(
        "/version",
        method="POST",
        headers=headers,
        data=json.dumps(version),
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.json["component_id"] == component.id
    assert response.json["version"] == "1.0"


def test_delete_version(client, version):
    """Test case for delete_version

    Delete a single version
    """
    response = client.open("/version/{version_id}".format(version_id=version.id), method="DELETE")
    assert response.status_code == 200


def test_get_version(client, version):
    """Test case for get_version

    Get a single version
    """
    headers = {
        "Accept": "application/json",
    }
    response = client.open(
        "/version/{version_id}".format(version_id=version.id), method="GET", headers=headers
    )
    assert response.status_code == 200
    assert response.json["id"] == version.id
    assert response.json["component_id"] == version.component_id
    assert response.json["version"] == version.version


def test_get_version_list(client, version):
    """Test case for get_version_list

    Get a list of versions
    """
    headers = {
        "Accept": "application/json",
    }
    response = client.open("/version", method="GET", headers=headers)
    assert response.status_code == 200
    assert len(response.json["versions"]) == 1
    assert response.json["versions"][0]["id"] == version.id
    assert response.json["versions"][0]["component_id"] == version.component_id
    assert response.json["versions"][0]["version"] == version.version


def test_update_version(client, version):
    """Test case for update_version

    Update a single version
    """
    updated_version = {
        "version": "1.2",
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.open(
        "/version/{version_id}".format(version_id=version.id),
        method="PUT",
        headers=headers,
        data=json.dumps(updated_version),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json["version"] == updated_version["version"]
