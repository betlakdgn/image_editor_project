from PIL import Image

def process_image(input_path, output_path, width, height, rotate, flip, crop_x, crop_y, crop_w, crop_h):
    image = Image.open(input_path)

    image = image.resize((width, height))
    image = image.rotate(rotate, expand=True)

    if flip == "horizontal":
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip == "vertical":
        image = image.transpose(Image.FLIP_TOP_BOTTOM)

    image = image.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
    image.save(output_path)
