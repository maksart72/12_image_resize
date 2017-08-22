import sys
import os
import argparse
from PIL import Image


def get_arguments():

    parser = argparse.ArgumentParser(description='Image resizer')
    parser.add_argument('filename', help='input source filename')
    parser.add_argument('-w', '--width', nargs='?',
                        type=int, help='set new width')
    parser.add_argument('-H', '--height', nargs='?',
                        type=int, help='set new height')
    parser.add_argument('-s', '--scale', nargs='?',
                        type=float, help='set new image scale size')
    parser.add_argument('-o', '--output', nargs='?',
                        help='set output path for result image')
    return parser


def load_image(filename):
    try:
        original = Image.open(filename)
    except:
        print("Unable to load image")
        sys.exit(1)
    return original


def save_image(original, size, dest_path):
    try:
        new = original.resize(size, Image.ANTIALIAS)
        new.save(dest_path)
        print('Done! New file is created:', dest_path)
    except PermissionError:
        print('Can not save resized file! Check permissions or correction of destination path:', dest_path)

def validate_arguments(new_width, new_height):
    if new_width == 0 or new_height == 0:
        print('Size "0" is not valid!')
        sys.exit(1)
    return

def get_new_filename(filename, new_width, new_height, output):

    file_name, file_extension = os.path.splitext(filename)
    filename_path = file_name.split('\\')
    filename_full = filename_path[-1]
    if output:
        name = output + filename_full
    else:
        name = filename_full
    new_filename = str('%s__%dx%d.%s' % (name, new_width, new_height, file_extension))
    return new_filename

def calculate_size(original_width, original_height, new_width, new_height, scale):
    new_size = ()
    if scale:
        print('Scale! Width and height ignored!')
        new_size = (int(original_width * scale), int(original_height * scale))
    else:
        if new_width and new_height:
            new_size = (int(new_width), int(new_height))
        if not new_width:
            new_size = (
                int(original_width * (new_height / original_height)), int(new_height))
        if not new_height:
            new_size = (int(new_width), int(
                original_height * (new_width / original_width)))
    return new_size


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Incorrect parameters. Use: "python image_resize.py -h" for help')
        sys.exit(1)
    else:
        arguments = get_arguments()
        parameters = arguments.parse_args()
        filename = parameters.filename
        original_image = load_image(filename)
        width = original_image.size[0]
        height = original_image.size[1]
        validate_arguments(parameters.width, parameters.height)
        calculate_size(width, height, parameters.width,
                       parameters.height, parameters.scale)
        new_size = calculate_size(
            width, height, parameters.width, parameters.height, parameters.scale)
        new_filename = get_new_filename(
            parameters.filename, new_size[0], new_size[1], parameters.output)
        save_image(original_image, new_size, new_filename)
