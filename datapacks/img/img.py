# python -m pip install --upgrade pip
# python -m pip install --upgrade Pillow
from PIL import Image
# pip install numpy
import numpy as np

#######################################################################
image_file_name = "kirbycope.png"
#######################################################################


def closest(colors, color):
    """ https://stackoverflow.com/a/54244301/1106708 """
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return smallest_distance 


def concrete_art(str_closest_color):
    if str_closest_color == str(concrete_black).replace(" ",""):
        return "black_concrete"
    elif str_closest_color == str(concrete_blue).replace(" ",""):
        return "blue_concrete"
    elif str_closest_color == str(concrete_brown).replace(" ",""):
        return "brown_concrete"
    elif str_closest_color == str(concrete_cyan).replace(" ",""):
        return "cyan_concrete"
    elif str_closest_color == str(concrete_gray).replace(" ",""):
        return "gray_concrete"
    elif str_closest_color == str(concrete_green).replace(" ",""):
        return "green_concrete"
    elif str_closest_color == str(concrete_light_blue).replace(" ",""):
        return "light_blue_concrete"
    elif str_closest_color == str(concrete_light_gray).replace(" ",""):
        return "light_gray_concrete"
    elif str_closest_color == str(concrete_lime).replace(" ",""):
        return "lime_concrete"
    elif str_closest_color == str(concrete_magenta).replace(" ",""):
        return "magenta_concrete"
    elif str_closest_color == str(concrete_orange).replace(" ",""):
        return "orange_concrete"
    elif str_closest_color == str(concrete_pink).replace(" ",""):
        return "pink_concrete"
    elif str_closest_color == str(concrete_purple).replace(" ",""):
        return "purple_concrete"
    elif str_closest_color == str(concrete_red).replace(" ",""):
        return "red_concrete"
    elif str_closest_color == str(concrete_white).replace(" ",""):
        return "white_concrete"
    elif str_closest_color == str(concrete_yellow).replace(" ",""):
        return "yellow_concrete"


def glass_art(str_closest_color):
    if str_closest_color == str(concrete_black).replace(" ",""):
        return"black_stained_glass"
    elif str_closest_color == str(concrete_blue).replace(" ",""):
        return"blue_stained_glass"
    elif str_closest_color == str(concrete_brown).replace(" ",""):
        return"brown_stained_glass"
    elif str_closest_color == str(concrete_cyan).replace(" ",""):
        return"cyan_stained_glass	"
    elif str_closest_color == str(concrete_gray).replace(" ",""):
        return"gray_stained_glass"
    elif str_closest_color == str(concrete_green).replace(" ",""):
        return"green_stained_glass"
    elif str_closest_color == str(concrete_light_blue).replace(" ",""):
        return"light_blue_stained_glass"
    elif str_closest_color == str(concrete_light_gray).replace(" ",""):
        return"light_gray_stained_glass"
    elif str_closest_color == str(concrete_lime).replace(" ",""):
        return"lime_stained_glass"
    elif str_closest_color == str(concrete_magenta).replace(" ",""):
        return"magenta_stained_glass"
    elif str_closest_color == str(concrete_orange).replace(" ",""):
        return"orange_stained_glass"
    elif str_closest_color == str(concrete_pink).replace(" ",""):
        return"pink_stained_glass"
    elif str_closest_color == str(concrete_purple).replace(" ",""):
        return"purple_stained_glass"
    elif str_closest_color == str(concrete_red).replace(" ",""):
        return"red_stained_glass"
    elif str_closest_color == str(concrete_white).replace(" ",""):
        return"white_stained_glass"
    elif str_closest_color == str(concrete_yellow).replace(" ",""):
        return"yellow_stained_glass"


# https://minecraft.fandom.com/wiki/Concrete#ID
concrete_black=[0,0,0]
concrete_blue=[45,47,144]
concrete_brown=[97,61,33]
concrete_cyan=[21,119,136]
concrete_gray=[54,57,61]
concrete_green=[74,92,37]
concrete_light_blue=[36,138,200]
concrete_light_gray=[126,126,116]
concrete_lime=[96,170,26]
concrete_magenta=[169,48,159]
concrete_orange=[225,97,0]
concrete_pink=[211,100,141]
concrete_purple=[100,31,156]
concrete_red=[142,32,32]
concrete_white=[208,214,215]
concrete_yellow=[241,175,21]
list_of_colors = [concrete_black, concrete_blue, concrete_brown, concrete_cyan, concrete_gray, concrete_green, concrete_light_blue, concrete_light_gray, concrete_lime, concrete_magenta, concrete_orange, concrete_pink, concrete_purple, concrete_red, concrete_white, concrete_yellow]

im = Image.open(image_file_name)
pix = im.load()
h = im.size[0]
w = im.size[1]
if h == 16 and w == 16:
    offset = 8

fileName = f"datapacks/img/data/img/functions/items/player/{image_file_name.split('.')[0]}.mcfunction"
with open(fileName, 'a') as mcfunction:
    for x in range(h):
        for y in range(w):
            rgb = pix[x, y]
            color = [rgb[0], rgb[1], rgb[2]]
            closest_color = closest(list_of_colors, color)
            func = f"setblock ~{x-offset} ~ ~{y-offset} "
            str_closest_color = str(closest_color).replace("[[", "[").replace("   ",",").replace("  ", ",").replace(" ",",").replace("]]", "]")
            if str(rgb) == "(0, 0, 0, 0)" :
                func+="air"
            else:
                func+=concrete_art(str_closest_color)
            mcfunction.write(func+'\n')

fileName = f"datapacks/img/data/img/functions/items/sky/{image_file_name.split('.')[0]}.mcfunction"
with open(fileName, 'a') as mcfunction:
    for x in range(h):
        for y in range(w):
            rgb = pix[x, y]
            color = [rgb[0], rgb[1], rgb[2]]
            closest_color = closest(list_of_colors, color)
            func = f"setblock ~{x-offset} 319 ~{y-offset} "
            str_closest_color = str(closest_color).replace("[[", "[").replace("   ",",").replace("  ", ",").replace(" ",",").replace("]]", "]")
            if str(rgb) == "(0, 0, 0, 0)" :
                func+="air"
            else:
                func+=glass_art(str_closest_color)
            mcfunction.write(func+'\n')
