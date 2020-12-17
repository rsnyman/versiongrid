#!/usr/bin/env python3
from versiongrid import get_app


if __name__ == "__main__":
    get_app().run(port=8080, debug=True)
