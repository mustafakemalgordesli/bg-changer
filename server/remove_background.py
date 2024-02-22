import rembg
import numpy as np
from PIL import Image

def remove_background(input_image_path, output_image_path):
    input_image = Image.open(input_image_path)
    rgb_image = input_image.convert('RGB')  

    input_array = np.array(rgb_image)

    output_array = rembg.remove(input_array)


    output_image = Image.fromarray(output_array)

    output_image.save(output_image_path)
