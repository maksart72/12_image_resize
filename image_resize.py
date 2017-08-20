import sys
import os
import argparse

def resize_image(path_to_original, path_to_result,width,height,scale):
    print('Done!',path_to_original, path_to_result,width,height,scale)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: python image_resize.py <path to file> [parameters]')
        sys.exit(1)
    else:
        filename =  sys.argv[1]
        print(filename) 
    print('End')       

    pass
    """  
        if not sys.argv[2]:
            print('O')
            path_to_result = ''
        else:
            path_to_result = sys.argv[2]
        
        if not sys.argv[3]:
            print('W')
            width = 800
        else:
            width = sys.argv[3]

        if not sys.argv[4]:
            print('H')
            height = 600
        else:
            height = sys.argv[4]

        if not sys.argv[5]:
            print('S')
            scale = 1
        else:
            scale = sys.argv[5]

        if not os.path.exists(path_to_original):
            raise Exception("Error! File doesn't exist!")
    except IndexError:
        print("Error: Empty argument, try image_resize.py <original filename> <result filename> <width> <height> <scale>")
    except ValueError:
        print('Error! Check your geo position input!')
    else:
        resize_image(path_to_original, path_to_result,width,height,scale)
 """