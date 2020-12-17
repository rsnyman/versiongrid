import logging

import fauxfactory
import pytest

from versiongrid import get_app
from versiongrid.db.base import session
from versiongrid.db.models import Component
from versiongrid.db.models import Dependency
from versiongrid.db.models import Version


@pytest.fixture
def app():
    logging.getLogger("connexion.operation").setLevel("ERROR")
    extra_config = {
        "TESTING": True,
        "LIVESERVER_PORT": 0,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    }
    app = get_app(**extra_config)
    return app.app


def _make_component():
    return Component(
        name=fauxfactory.gen_alpha(length=20, start="component_"),
        title=fauxfactory.gen_alpha(length=20, start="Component "),
    )


def _make_version(component):
    return Version(version=fauxfactory.gen_alpha(), component=component)


@pytest.fixture
def component(app):
    """A randomly generated component"""
    c = _make_component()
    session.add(c)
    session.commit()
    yield c
    if Component.query.get(c.id):
        session.delete(c)
        session.commit()


@pytest.fixture
def dependency_component(app):
    """A second randomly generated component"""
    c = _make_component()
    session.add(c)
    session.commit()
    yield c
    if Component.query.get(c.id):
        session.delete(c)
        session.commit()


@pytest.fixture
def version(component):
    """A randomly generated version of a randomly generated component"""
    v = _make_version(component)
    session.add(v)
    session.commit()
    yield v
    if Version.query.get(v.id):
        session.delete(v)
        session.commit()


@pytest.fixture
def dependency_version(dependency_component):
    """A second randomly generated version of a secondly randomly generated component"""
    v = _make_version(dependency_component)
    session.add(v)
    session.commit()
    yield v
    if Version.query.get(v.id):
        session.delete(v)
        session.commit()


@pytest.fixture
def dependency(version, dependency_version):
    d = Dependency(component_version_id=version.id, dependency_version_id=dependency_version.id)
    session.add(d)
    session.commit()
    yield d
    if Dependency.query.get(d.id):
        session.delete(d)
        session.commit()
