![map-markers](/map-markers.png)

# map-markers-java
Use a Python script to create map art in Minecraft Java. The color pallet is simple; concrete for the ground blocks and glass for the sky blocks. Glass blocks have the same color on the map as their concrete counterparts but do not cast a shadow on the ground below.
</br>![colors](/colors.png)</br>
I took the (above) screenshot and used the color picker tool in [Paint.Net](https://www.getpaint.net/index.html) to get the RGB values.
```
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
```
## Usage
Run `img:give` to get the book.
</br>Run `img:items/player/{itemName}` to set blocks at centered your position at your current elevation.
</br>Run `img:items/sky/{itemName}` to set blocks at centered your position at y-level 319 (max) elevation.

## Installation
Use an existing world that is already setup to use the datapack.
1. Download the [zip file](https://github.com/kirbycope/map-markers-java/archive/refs/heads/main.zip)
1. Unarchive zip contents into the [Saves folder](https://help.minecraft.net/hc/en-us/articles/4409159214605-Managing-Data-and-Game-Storage-in-Minecraft-Java-Edition) of Minecraft Java Edition

### Creating New Images
Running the Python script will create new `.mcfunction` files in the datapack for you to use in-game.
1. Copy your 16x16 `.png` file to the root of the save folder
1. Open the save folder in [VS Code](https://code.visualstudio.com/)
1. Open the "img.py file"
   - The Python script has some dependencies:
      1. In VS Code, open a terminal window
      1. Run `python -m pip install --upgrade pip`
      1. Run `python -m pip install --upgrade Pillow`
      1. Run `pip install numpy`
1. Scroll to the end and change the file name(s)
1. Run the python script (use the F5 key or Play button)

### Package New Images into Datapack
In order to play on other worlds, you'll want to package up the datapack. Archive (`.zip`) the "datapacks/img" folder.

## Datapack Installation
Use this datapack with your own worlds.
1. Download the [zip file](https://github.com/kirbycope/map-markers-java/raw/main/map-markers.zip)
1. Install for a
   * [New World](https://minecraft.fandom.com/wiki/Tutorials/Installing_a_data_pack#At_the_creation_of_a_world)
   * [Existing World](https://minecraft.fandom.com/wiki/Tutorials/Installing_a_data_pack#In_an_existing_world)
