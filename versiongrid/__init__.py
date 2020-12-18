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


def get_app(**extra_config):
    app = connexion.App(__name__, specification_dir="./openapi/")
    app.app.json_encoder = encoder.JSONEncoder

    # Set up the application configuration
    config = app.app.config
    config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", True)
    config.from_mapping(os.environ)
    if config.get("POSTGRES_HOST") and config.get("POSTGRES_DB"):
        # If you have environment variables for the DB, create the db url
        config.update(
            {
                "SQLALCHEMY_DATABASE_URI": _make_sql_url(
                    config["POSTGRES_HOST"],
                    config["POSTGRES_DB"],
                    port=config.get("POSTGRES_PORT"),
                    user=config.get("POSTGRES_USER"),
                    password=config.get("POSTGRES_PASSWORD"),
                )
            }
        )
    # Load any extra config
    config.update(extra_config)

    app.add_api("openapi.yaml", arguments={"title": "VersionGrid"}, pythonic_params=True)

    # Additional app setup
    CORS(app.app)
    db.init_app(app.app)

    with app.app.app_context():
        db.create_all()

    return app
