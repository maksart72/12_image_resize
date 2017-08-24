import sys
import os
import argparse
from PIL import Image


def get_arguments():

    parser = argparse.ArgumentParser(description='Image resize utility. '
                                                 'Put positional argument and one of width, height or scale argument for proper work.')
    parser.add_argument('filename', help='input source filename')
    parser.add_argument('-w', '--width', nargs='?',
                        type=int, help='set new width, must be > 0')
    parser.add_argument('-H', '--height', nargs='?',
                        type=int, help='set new height, must be > 0')
    parser.add_argument('-s', '--scale', nargs='?',
                        type=float, help='set new image scale size, must be > 0 but < 10')
    parser.add_argument('-o', '--output', nargs='?',
                        help='set output path for result image')
    return parser


def load_image(filename):
    try:
        original = Image.open(filename)
    except OSError:
        print("Unable to load image")
    return original


def save_image(original, size, dest_path):
    try:
        new = original.resize(size, Image.ANTIALIAS)
        new.save(dest_path)
        print('Done! New file is created:', dest_path)
    except PermissionError:
        print('Can not save resized file! Check permissions or correction of destination path:', dest_path)

def validate_arguments(new_width, new_height, scale):
    return bool((new_width and new_width > 0) or (new_height and new_height > 0) or (scale and 0 < scale < 10))

def get_new_filename(filename, new_size, output):

    new_width, new_height = new_size
    file_name, file_extension = os.path.splitext(filename)
    filename_path = file_name.split('\\')
    filename_full = filename_path[-1]
    if output:
        new_name = output + filename_full
    else:
        new_name = filename_full
    new_filename = str('%s__%dx%d%s' % (new_name, new_width, new_height, file_extension))
    return new_filename

def calculate_size(original_size, new_width, new_height, scale):

    original_width, original_height = original_size 
    new_size = ()

    if new_width and new_height:
        new_size = (int(new_width), int(new_height))

    if not new_width and new_height:
        new_size = (
            int(original_width * (new_height / original_height)), int(new_height))

    if not new_height and new_width:
        new_size = (int(new_width), int(
            original_height * (new_width / original_width)))

    if scale:
        print('You input scale! Width and height parameters are ignored!')
        new_size = (int(original_width * scale), int(original_height * scale))

    return new_size


if __name__ == '__main__':

    arguments = get_arguments()
    parameters = arguments.parse_args()
    filename = parameters.filename

    if validate_arguments(parameters.width, parameters.height, parameters.scale):

        original_image = load_image(filename)

        new_size = calculate_size(
        original_image.size, parameters.width, parameters.height, parameters.scale)

        new_filename = get_new_filename(
        parameters.filename, new_size, parameters.output)

        save_image(original_image, new_size, new_filename)

    else:
        print('Something wrong with parameters! Run "image_resize.py -h" for help.')