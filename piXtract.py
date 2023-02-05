from PIL import Image

def image_to_txt(image_path):
    """
    This function takes in an image file and outputs a .txt file 
    that contains the RGB values of every pixel in the image. Known to 
    work with .jpg, .png and .bmp files.Will definitely not work
    with .gif files, but might work with some others.

    Args:
    - image_path (str): The path to the image file.

    Returns:
    None
    """

    # Open the image using the PIL Image library
    img = Image.open(image_path)

    # Load the pixels of the image
    pixels = img.load()

    # Get the width and height of the image
    width, height = img.size

    # Open the output text file
    txt_file = open(f"{image_path.split('.')[0]}.txt", 'w')

    # Loop through the pixels of the image from top to bottom, left to right
    for h in range(height):
        line = []
        for w in range(width):
            line.append(str(list(pixels[w, h])))
        txt_file.write(", ".join(line) + "\n")

    # Close the output text file
    txt_file.close()

if __name__ == "__main__":
    print("""
            ___   ___                  _   
           (_) \ / / |                | |  
      _ __  _ \ V /| |_ _ __ __ _  ___| |_ 
     | '_ \| | > < | __| '__/ _` |/ __| __|
     | |_) | |/ . \| |_| | | (_| | (__| |_ 
     | .__/|_/_/ \_\\___|_|  \__,_|\___|\__|
     | |                               
     |_|  The RGB value extraction tool! """)
    print()
    # Ask for the path to the image file
    image_path = input("Enter the path to the image file: ")

    # Call the image_to_txt function to convert the image to text
    image_to_txt(image_path)

