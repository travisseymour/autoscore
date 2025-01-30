import importlib
from importlib.metadata import version


def get_version() -> str:
    try:
        return version("autoscore")
    except importlib.metadata.PackageNotFoundError:
        return "???"
