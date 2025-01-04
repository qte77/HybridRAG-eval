"""Redirects to entrypoint of the app"""

from .main import main
from sys import exit

if __name__ == "__main__":
    exit(main())
