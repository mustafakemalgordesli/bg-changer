from PIL import Image

def add_background(input_image_path, background_image_path, output_image_path, margin=10, scale_factor=0.5):
    background = Image.open(background_image_path)

    input_image = Image.open(input_image_path).convert("RGBA")

    background = background.resize((int(background.width * scale_factor), int(background.height * scale_factor)), Image.LANCZOS)

    width, height = background.size

    input_image_width, input_image_height = input_image.size

    enlarge_factor = width / input_image_width
    
    input_image = input_image.resize((int(input_image_width * enlarge_factor), int(input_image_height * enlarge_factor)), Image.LANCZOS)

    new_image = Image.new("RGBA", (width + margin * 2, height + margin * 2), (255, 255, 255, 0))

    new_image.paste(background, (margin, margin))

    new_image.paste(input_image, (margin, margin), input_image)

    new_image.save(output_image_path, format="PNG")


# if __name__ == "__main__":
#     input_image_path = "assets/foto2.png" 
#     background_image_path = "assets/foto.jpg"
#     output_image_path = "assets/output_image.png" 
#     margin = 0
#     scale_factor = 1

#     add_background(input_image_path, background_image_path, output_image_path, margin, scale_factor)

