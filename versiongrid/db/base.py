from uuid import UUID

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.types import CHAR
from sqlalchemy.types import TypeDecorator


db = SQLAlchemy()
Model = db.Model
Boolean = db.Boolean
Column = db.Column
DateTime = db.DateTime
Float = db.Float
ForeignKey = db.ForeignKey
Integer = db.Integer
LargeBinary = db.LargeBinary
Table = db.Table
Text = db.Text
relationship = db.relationship
inspect = db.inspect
session = db.session


class PortableUUID(TypeDecorator):
    """Platform-independent UUID type.

    Uses PostgreSQL's UUID type, otherwise uses CHAR(32), storing as stringified hex values.

    Based on https://docs.sqlalchemy.org/en/13/core/custom_types.html#backend-agnostic-guid-type
    """

    impl = CHAR

    def __init__(self, *args, **kwargs):
        if "as_uuid" in kwargs:
            self.as_uuid = kwargs.pop("as_uuid")
        else:
            self.as_uuid = False
        super().__init__(*args, **kwargs)

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(PostgresUUID(as_uuid=self.as_uuid))
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == "postgresql":
            return value
        else:
            if isinstance(value, UUID):
                return str(value)
            else:
                return value

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            if self.as_uuid and not isinstance(value, UUID):
                value = UUID(value)
            return value
