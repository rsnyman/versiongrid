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

    def update(self, record_dict):
        if "id" in record_dict:
            record_dict.pop("id")
        for key, value in record_dict.items():
            setattr(self, key, value)


class Component(Model, DictMixin):
    __tablename__ = "components"

    id = Column(PortableUUID(), primary_key=True, default=_gen_uuid, unique=True, nullable=False)
    name = Column(Text, index=True)
    title = Column(Text)

    versions = relationship("Version", backref="component")


class Dependency(Model, DictMixin):
    __tablename__ = "dependencies"

    id = Column(PortableUUID(), primary_key=True, default=_gen_uuid, unique=True, nullable=False)
    component_version_id = Column(PortableUUID(), ForeignKey("versions.id"), index=True)
    dependency_version_id = Column(PortableUUID(), ForeignKey("versions.id"), index=True)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def component_version(self):
        return Version.query.get(self.component_version_id)

    @property
    def dependency_version(self):
        return Version.query.get(self.dependency_version_id)


class Version(Model, DictMixin):
    __tablename__ = "versions"

    id = Column(PortableUUID(), primary_key=True, default=_gen_uuid, unique=True, nullable=False)
    component_id = Column(PortableUUID(), ForeignKey("components.id"), index=True)
    commit = Column(Text, index=True)
    image_tag = Column(Text, index=True)
    template_ref = Column(Text, index=True)
    revision = Column(Text, index=True)
    version = Column(Text, index=True)
    created = Column(DateTime, default=datetime.utcnow)
