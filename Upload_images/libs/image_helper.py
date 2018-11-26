import os
import re
from typing import Union
from werkzeug.datastructures import FileStorage

from flask_uploads import UploadSet, IMAGES
# IMAGES = tuple('jpg jpe jpeg png gif svg bmp'.split())


# An “upload set” is a single collection of files. You just declare them in the code:
# set name and allowed extensions
IMAGE_SET = UploadSet("images", IMAGES) # IMAGES is a collcetion of allowed extensions


def save_image(image: FileStorage, folder: str = None, name: str = None) -> str:
    """Takes FileStorage and save it to a folder"""
    return IMAGE_SET.save(image, folder, name)


def get_path(filename: str = None, folder: str = None) -> str:
    """Take image name and folder and return full path"""
    return IMAGE_SET.path(filename, folder)


def find_image_any_format(filename: str, folder: str) -> Union[str, None]:
    """
    Given a format-less filename, try to find the file by appending each of the allowed formats to the given
    filename and check if the file exists
    :param filename: formatless filename
    :param folder: the relative folder in which to search
    :return: the path of the image if exists, otherwise None
    """
    for _format in IMAGES:  # look for existing avatar and delete it
        avatar = f"{filename}.{_format}"
        avatar_path = IMAGE_SET.path(filename=avatar, folder=folder)
        if os.path.isfile(avatar_path):
            return avatar_path
    return None


def _retrieve_filename(file: Union[str, FileStorage]) -> str:
    """
    Take FileStorage and return the file name.
    Allows our function to call this with both filenames and 
    FileStorages and always gets back a file name
    Make our filename related functions generic, 
    able to deal with FileStorage object as well as filename str.
    """
    if isinstance(file, FileStorage):
        return file.filename
    return file


def is_filename_safe(file: Union[str, FileStorage]) -> bool:
    """
    Check our regex and return if the string matches or not
    Check if a filename is secure according to our definition
    - starts with a-z A-Z 0-9 at least one time
    - only contains a-z A-Z 0-9 and _().-
    - followed by a dot (.) and a allowed_format at the end
    """
    filename = _retrieve_filename(file)
    allowed_format = "|".join(IMAGES)
    # format IMAGES into regex, eg: ('jpeg','png') --> 'jpeg|png'
    regex = f"^[a-zA-Z0-9][a-zA-Z0-9_()-\.]*\.({allowed_format})$"
    return re.match(regex, filename) is not None

# get_basename('regrg/rg4tgtg/thy5j/name.py') -> "name.py"
def get_basename(file: Union[str, FileStorage]) -> str:
    """
    Return file's basename, for example
    get_basename('some/folder/image.jpg') returns 'image.jpg'
    """
    filename = _retrieve_filename(file)
    return os.path.split(filename)[1]


# get_basename('regrg/rg4tgtg/thy5j/name.py') -> ".py"
def get_extension(file: Union[str, FileStorage]) -> str:
    """         
    Return file's extension, for example
    get_extension('image.jpg') returns '.jpg'
    """
    filename = _retrieve_filename(file)
    return os.path.splitext(filename)[1]

# print(_retrieve_filename('/wefwf/frwgferqge/image.jpg'))
# print(get_extension('image.jpg'))
# print(get_basename('regrg/rg4tgtg/thy5j/name.py'))