# piXtract, the RGB value extraction tool

## Introduction
piXtract is a Python tool that takes in an image file and outputs a .txt file that contains the RGB values of every pixel in the image. The program first asks for a path to the image, then it goes through the pixels of the image left to right, top to bottom, starting from the top left corner. Every RGB value is stored in the format ```[R, G, B]``` and each row of pixels is stored as its own line in the output file. The lines in the resulting file can be used as lists in python as is.
## Compatibility and limitations
Known to work with the following file types: ```.jpg, .png, .bmp.```

Known __not__ to work with the following file types: ```.gif```

While there is no obvious reason why piXtract wouldn't work with an image of any given pixel count, it has only been tested with reasonably-sized images. Please report all compatibilities not listed above so they can be added to the documentation.
## Requirements
- Python 3.x
- Pillow (PIL) library
## Usage
To use piXtract, simply run the script in your terminal and follow the prompt:

```python piXtract.py```

The program will prompt you to enter the path to the image file, then it will generate the .txt file containing the RGB values of the image and save it in the same directory as the original image. The .txt file will be named after the original image file.
