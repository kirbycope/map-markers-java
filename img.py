import os
# python -m pip install --upgrade pip
# python -m pip install --upgrade Pillow
from PIL import Image
# pip install numpy
import numpy as np


#######################################################################
black=[25,25,25]
blue=[50,75,175]
brown=[100,75,50]
cyan=[75,125,151]
gray=[75,75,75]
green=[100,125,50]
light_blue=[100,151,213]
light_gray=[151,151,151]
lime=[125,201,25]
magenta=[175,75,213]
orange=[213,125,50]
pink=[238,125,162]
purple=[125,62,175]
red=[151,50,50]
white=[251,251,251]
yellow=[225,225,50]
basic_colors = [black, blue, brown, cyan, gray, green, light_blue, light_gray, lime, magenta, orange, pink, purple, red, white, yellow]
#######################################################################


def closest(color):
    """ https://stackoverflow.com/a/54244301/1106708 """
    colors = np.array(basic_colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return smallest_distance[0]


def concrete_art(closest_color):
    if (closest_color == black).all():
        return "black_concrete"
    elif (closest_color == blue).all():
        return "blue_concrete"
    elif (closest_color == brown).all():
        return "brown_concrete"
    elif (closest_color == cyan).all():
        return "cyan_concrete"
    elif (closest_color == gray).all():
        return "gray_concrete"
    elif (closest_color == green).all():
        return "green_concrete"
    elif (closest_color == light_blue).all():
        return "light_blue_concrete"
    elif (closest_color == light_gray).all():
        return "light_gray_concrete"
    elif (closest_color == lime).all():
        return "lime_concrete"
    elif (closest_color == magenta).all():
        return "magenta_concrete"
    elif (closest_color == orange).all():
        return "orange_concrete"
    elif (closest_color == pink).all():
        return "pink_concrete"
    elif (closest_color == purple).all():
        return "purple_concrete"
    elif (closest_color == red).all():
        return "red_concrete"
    elif (closest_color == white).all():
        return "white_concrete"
    elif (closest_color == yellow).all():
        return "yellow_concrete"


def glass_art(closest_color):
    if (closest_color == black).all():
        return "black_stained_glass"
    elif (closest_color == blue).all():
        return "blue_stained_glass"
    elif (closest_color == brown).all():
        return "brown_stained_glass"
    elif (closest_color == cyan).all():
        return "cyan_stained_glass	"
    elif (closest_color == gray).all():
        return "gray_stained_glass"
    elif (closest_color == green).all():
        return "green_stained_glass"
    elif (closest_color == light_blue).all():
        return "light_blue_stained_glass"
    elif (closest_color == light_gray).all():
        return "light_gray_stained_glass"
    elif (closest_color == lime).all():
        return "lime_stained_glass"
    elif (closest_color == magenta).all():
        return "magenta_stained_glass"
    elif (closest_color == orange).all():
        return "orange_stained_glass"
    elif (closest_color == pink).all():
        return "pink_stained_glass"
    elif (closest_color == purple).all():
        return "purple_stained_glass"
    elif (closest_color == red).all():
        return "red_stained_glass"
    elif (closest_color == white).all():
        return "white_stained_glass"
    elif (closest_color == yellow).all():
        return "yellow_stained_glass"


def create_mcfunction(image_file_name, img_type):
    im = Image.open(image_file_name)
    pix = im.load()
    h = im.size[0]
    w = im.size[1]
    offset = (h+w)//4
    fileName = f"datapacks/img/data/img/functions/items/{img_type}/{image_file_name.split('.')[0]}.mcfunction"
    os.remove(fileName)
    with open(fileName, 'a') as mcfunction:
        for x in range(h):
            for y in range(w):
                rgb = pix[x, y]
                color = [rgb[0], rgb[1], rgb[2]]
                closest_color = closest(color)
                if img_type == "player": func = f"setblock ~{x-offset} ~ ~{y-offset} "
                elif img_type == "sky": func = f"setblock ~{x-offset} 319 ~{y-offset} "
                if str(rgb) == "(0, 0, 0, 0)":
                    func+="air"
                else:
                    if img_type == "player": func+=concrete_art(closest_color)
                    elif img_type == "sky": func+=glass_art(closest_color)
                mcfunction.write(func+'\n')


create_mcfunction("apple.png", "player")
create_mcfunction("apple.png", "sky")
