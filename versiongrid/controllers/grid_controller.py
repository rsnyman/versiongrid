import connexion

from versiongrid.db.base import session
from versiongrid.db.models import Component
from versiongrid.db.models import Dependency
from versiongrid.db.models import Version


def add_grid(grid=None):
    """add_grid

    Create a new dependency grid.

    :param grid:
    :type grid: dict | bytes

    :rtype: Grid
    """
    if not connexion.request.is_json:
        return "Bad request, JSON required", 400
    grid = connexion.request.get_json()
    component = Component.query.filter(Component.name == grid["component"]).first()
    if not component:
        return f"Component {grid['component']} not found", 404
    version = (
        Version.query.filter(Version.component == component)
        .filter(Version.version == grid["version"])
        .first()
    )
    if not version:
        version = Version(version=grid["version"], component=component)
        session.add(version)
        # session.commit()
    for dependency in grid["dependencies"]:
        dep_component = Component.query.filter(Component.name == dependency["component"]).first()
        if not dep_component:
            return "Dependency component {dependency['component']} not found", 404
        dep_version = (
            Version.query.filter(Version.component == dep_component)
            .filter(Version.version == dependency["version"])
            .first()
        )
        if not dep_version:
            dep_version = Version(component=dep_component, version=dependency["version"])
            session.add(dep_version)
            session.commit()
        dep = Dependency(component_version_id=version.id, dependency_version_id=dep_version.id)
        session.add(dep)
        session.commit()
    return grid, 201


def get_grid(component, version=None):
    """Check a component&#39;s dependencies

    Return a component's latest dependency grid. If a version is supplied, the dependency grid for
    that version will be returned.

    :param component:
    :type component: str
    :param version:
    :type version: str

    :rtype: Grid
    """
    comp = Component.query.filter(Component.name == component).first()
    if not comp:
        return f"Component {component} not found", 404
    if version:
        vers = (
            Version.query.filter(Version.component == comp)
            .filter(Version.version == version)
            .first()
        )
        if not vers:
            return f"Version {version} not found for component {component}", 404
    else:
        vers = (
            Version.query.filter(Version.component == comp).order_by(Version.created.desc()).first()
        )
        if not vers:
            return f"No versions found for component {component}", 404
    dependencies = Dependency.query.filter(Dependency.component_version_id == vers.id).all()
    grid = {"component": comp.name, "version": vers.version, "dependencies": []}
    for dependency in dependencies:
        grid["dependencies"].append(
            {
                "component": dependency.dependency_version.component.name,
                "version": dependency.dependency_version.version,
            }
        )
    return grid
