"""Various methods related to I/O."""
import os


def write_file(path, contents, mode="w"):
    """Writes contents to a file at a given path."""
    with open(path, mode) as f:
        f.write(contents)


def exists(path):
    """Checks if a file is present at the given path."""
    return os.path.exists(path)


def create_folder(path):
    """Creates a folder at a pathif it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
