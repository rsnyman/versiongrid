#!/usr/bin/env python3
import os

import connexion
from flask_cors import CORS

from versiongrid import encoder
from versiongrid.db.base import db


def _make_sql_url(hostname, database, **kwargs):
    """Build a URL for SQLAlchemy"""
    url = hostname
    if kwargs.get("port"):
        url = "{}:{}".format(url, kwargs["port"])
    if kwargs.get("user"):
        credentials = kwargs["user"]
        if kwargs.get("password"):
            credentials = "{}:{}".format(credentials, kwargs["password"])
        url = "{}@{}".format(credentials, url)
    return "postgresql://{}/{}".format(url, database)


def main():
    app = connexion.App(__name__, specification_dir="./openapi/")
    app.app.json_encoder = encoder.JSONEncoder

    # Set up the application configuration
    config = app.app.config
    config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", True)
    config.from_mapping(os.environ)
    if config.get("POSTGRESQL_HOST") and config.get("POSTGRESQL_DATABASE"):
        # If you have environment variables for the DB, create the db url
        config.update(
            {
                "SQLALCHEMY_DATABASE_URI": _make_sql_url(
                    config["POSTGRESQL_HOST"],
                    config["POSTGRESQL_DATABASE"],
                    port=config.get("POSTGRESQL_PORT"),
                    user=config.get("POSTGRESQL_USER"),
                    password=config.get("POSTGRESQL_PASSWORD"),
                )
            }
        )

    app.add_api("openapi.yaml", arguments={"title": "VersionGrid"}, pythonic_params=True)

    # Additional app setup
    CORS(app.app)
    db.init_app(app.app)

    with app.app.app_context():
        db.create_all()

    app.run(port=8080)


if __name__ == "__main__":
    main()
