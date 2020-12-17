# coding: utf-8
import json


def test_add_dependency(client, version, dependency_version):
    """Test case for add_dependency

    Create a new dependency
    """
    dependency = {
        "component_version_id": version.id,
        "dependency_version_id": dependency_version.id,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.open(
        "/dependency",
        method="POST",
        headers=headers,
        data=json.dumps(dependency),
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.json["component_version_id"] == version.id
    assert response.json["dependency_version_id"] == dependency_version.id


def test_delete_dependency(client, dependency):
    """Test case for delete_dependency

    Delete a single dependency
    """
    response = client.open(
        "/dependency/{dependency_id}".format(dependency_id=dependency.id),
        method="DELETE",
    )
    assert response.status_code == 200


def test_get_dependency(client, dependency):
    """Test case for get_dependency

    Get a single dependency
    """
    headers = {"Accept": "application/json"}
    response = client.open(
        "/dependency/{dependency_id}".format(dependency_id=dependency.id),
        method="GET",
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json["component_version_id"] == dependency.component_version_id
    assert response.json["dependency_version_id"] == dependency.dependency_version_id


def test_get_dependency_list(client, dependency):
    """Test case for get_dependency_list

    Get a list of dependencies
    """
    headers = {"Accept": "application/json"}
    response = client.open("/dependency", method="GET", headers=headers)
    assert response.status_code == 200
    assert len(response.json["dependencies"]) == 1
    assert (
        response.json["dependencies"][0]["component_version_id"] == dependency.component_version_id
    )
    assert (
        response.json["dependencies"][0]["dependency_version_id"]
        == dependency.dependency_version_id
    )


def test_update_dependency(client, dependency, dependency_version):
    """Test case for update_dependency

    Update a single dependency
    """
    updated_dependency = {
        "dependency_version_id": dependency_version.id,
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.open(
        "/dependency/{dependency_id}".format(dependency_id=dependency.id),
        method="PUT",
        headers=headers,
        data=json.dumps(updated_dependency),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json["dependency_version_id"] == dependency.dependency_version_id
