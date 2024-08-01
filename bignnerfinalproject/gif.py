import imageio.v3 as iio
from PIL import Image
import numpy as np

# List of image filenames
filenames = ["nyan-cat1.png", "nyan-cat2.png", "nyan-cat3.png"]
images = []

# Open the first image to get the target dimensions
first_image = Image.open(filenames[0])
target_size = first_image.size  # (width, height)
first_image.close()

# Resize all images to the target size and convert to NumPy array
for filename in filenames:
    img = Image.open(filename)
    img_resized = img.resize(target_size, Image.LANCZOS)

    # Convert to NumPy array and ensure RGB format
    img_array = np.array(img_resized.convert('RGB'))
    images.append(img_array)
    img.close()


# Save the list of images as a GIF
iio.imwrite('team.gif', images, duration=500, loop=0)
