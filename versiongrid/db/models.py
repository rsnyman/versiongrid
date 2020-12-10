from datetime import datetime
from uuid import uuid4

from versiongrid.db.base import Column
from versiongrid.db.base import DateTime
from versiongrid.db.base import ForeignKey
from versiongrid.db.base import inspect
from versiongrid.db.base import Model
from versiongrid.db.base import PortableUUID
from versiongrid.db.base import relationship
from versiongrid.db.base import Text


def _gen_uuid():
    """Generate a UUID"""
    return str(uuid4())


class DictMixin(object):
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Component(Model, DictMixin):
    __tablename__ = "components"

    id = Column(PortableUUID(), primary_key=True, default=_gen_uuid, unique=True, nullable=False)
    name = Column(Text, index=True)
    title = Column(Text)

    versions = relationship("Version")


class Dependency(Model, DictMixin):
    __tablename__ = "dependencies"

    id = Column(PortableUUID(), primary_key=True, default=_gen_uuid, unique=True, nullable=False)
    component_version_id = Column(PortableUUID(), ForeignKey("versions.id"), index=True)
    dependency_version_id = Column(PortableUUID(), ForeignKey("versions.id"), index=True)
    created = Column(DateTime, default=datetime.utcnow)


class Version(Model, DictMixin):
    __tablename__ = "versions"

    id = Column(PortableUUID(), primary_key=True, default=_gen_uuid, unique=True, nullable=False)
    component_id = Column(PortableUUID(), ForeignKey("component.id"), index=True)
    commit = Column(Text, index=True)
    image_tag = Column(Text, index=True)
    template_ref = Column(Text, index=True)
    revision = Column(Text, index=True)
    version = Column(Text, index=True)
    created = Column(DateTime, default=datetime.utcnow)

    environments = relationship("VersionEnvironment")

    def to_dict(self):
        version_dict = super().to_dict()
        version_dict["environments"] = {
            "name": self.environments.environment.name,
            "deployed_date": self.environments.deployed_date,
        }
        return version_dict


class Environment(Model, DictMixin):
    __tablename__ = "environments"

    id = Column(PortableUUID(), primary_key=True, default=_gen_uuid, unique=True, nullable=False)
    name = Column(Text, index=True)


class VersionEnvironment(Model):
    __tablename__ = "environments_versions"

    environment_id = Column(PortableUUID(), ForeignKey("environments.id"), primary_key=True)
    version_id = Column(PortableUUID(), ForeignKey("versions.id"), primary_key=True)
    deployed_date = Column(DateTime)

    environment = relationship("Environment")
