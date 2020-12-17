# coding: utf-8
import json

from versiongrid.db.models import Dependency
from versiongrid.db.models import Version


def test_add_grid(client, component, dependency_component):
    """Test case for add_grid"""
    grid = {
        "component": component.name,
        "version": "1.0",
        "dependencies": [{"component": dependency_component.name, "version": "1.1"}],
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.open(
        "/grid",
        method="POST",
        headers=headers,
        data=json.dumps(grid),
        content_type="application/json",
    )
    assert response.status_code == 201
    version = Version.query.filter(Version.component == component).first()
    assert version is not None
    dependency_version = Version.query.filter(Version.component == dependency_component).first()
    assert dependency_version is not None
    dependency = Dependency.query.filter(Dependency.component_version_id == version.id).first()
    assert dependency is not None
    assert dependency.dependency_version_id == dependency_version.id


def test_get_grid(client, dependency):
    """Test case for get_grid

    Check a component's dependencies
    """
    component = dependency.component_version.component
    dependency_component = dependency.dependency_version.component
    headers = {
        "Accept": "application/json",
    }
    response = client.open(
        "/grid/{component}".format(component=component.name),
        method="GET",
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json["component"] == component.name
    assert response.json["version"] == dependency.component_version.version
    assert len(response.json["dependencies"]) == 1
    assert response.json["dependencies"][0]["component"] == dependency_component.name
    assert response.json["dependencies"][0]["version"] == dependency.dependency_version.version
