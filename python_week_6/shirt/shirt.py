import sys
import os
from PIL import Image, ImageOps


def resize_n_crop(input_image, output_image, overlay_image):
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    shirtfile = Image.open("shirt.png")
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])



if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    input_ext = os.path.splitext(input_filename)[1].lower()
    output_ext = os.path.splitext(output_filename)[1].lower()

    if input_ext not in [".jpg", ".jpeg", ".png"] or output_ext not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(input_filename):
        sys.exit("Input does not exist")

    resize_n_crop(input_filename, output_filename, "shirt.png")



