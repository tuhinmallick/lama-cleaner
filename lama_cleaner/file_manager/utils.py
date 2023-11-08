# Copy from: https://github.com/silentsokolov/flask-thumbnails/blob/master/flask_thumbnails/utils.py
import importlib
import os
from pathlib import Path

from typing import Union


def generate_filename(original_filename, *options):
    name, ext = os.path.splitext(original_filename)
    for v in options:
        if v:
            name += f"_{v}"
    name += ext

    return name


def parse_size(size):
    if isinstance(size, int):
        # If the size parameter is a single number, assume square aspect.
        return [size, size]

    if isinstance(size, (tuple, list)):
        return size + type(size)(size) if len(size) == 1 else size
    try:
        thumbnail_size = [int(x) for x in size.lower().split("x", 1)]
    except ValueError:
        raise ValueError(  # pylint: disable=raise-missing-from
            "Bad thumbnail size format. Valid format is INTxINT."
        )

    if len(thumbnail_size) == 1:
        # If the size parameter only contains a single integer, assume square aspect.
        thumbnail_size.append(thumbnail_size[0])

    return thumbnail_size


def aspect_to_string(size):
    return size if isinstance(size, str) else "x".join(map(str, size))


IMG_SUFFIX = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}


def glob_img(p: Union[Path, str], recursive: bool = False):
    p = Path(p)
    if p.is_file() and p.suffix in IMG_SUFFIX:
        yield p
    else:
        files = Path(p).glob("**/*.*") if recursive else Path(p).glob("*.*")
        for it in files:
            if it.suffix not in IMG_SUFFIX:
                continue
            yield it
