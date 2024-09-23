# Paletteer

A simple python script that produced a png containing the colors specified as a line-delimited list of RGB values (expressed as `#RRGGBB` in hexdecimal).

## Motivation

Working on 2d pixel art is a lot of fun, but depending on your setup and which applications you're using, creating a cohesive palette can be time consuming and manually intensive.

We have created a [Google Sheet](https://docs.google.com/spreadsheets/d/1B6X9GsLyplz67aGvTK1dT1qvh9ocayL4qrzdNWhJmhI/edit?usp=sharing) that you can copy for yourself and use to create your own palettes. It takes HSV values and translates them into RGB values you can paste into a text file that paletteer will read to create a .png file containing swatches. This .png can then be imported into programs like Aseprite.

## Installing

Clone paletteer from GitHub with the following command:

```sh
git clone git://github.com/folkloreinteractive/paletteer
```

### POSIX environments

```sh
source ./env.sh
```

### Windows Powershell

```sh
./setup.ps1
```

## Running

Paletteer requires you to provide two arguments:

 1. the text file containing the line-delimited RGB values
 2. the file to write the resulting .png file to

```sh
python ./main.py ./palette.txt ./palette.png
```

## Example Text File

A valid list of RGB values must be line delimited, like this:

__example-rgbs.txt__
```txt
#5f29cc
#4a36b3
#3d3d99
#333b66
#4d2640
#662e41
#803433
#994836
#b37436
#cc9629
#e6c317
#ffff00
#ffff8a
```