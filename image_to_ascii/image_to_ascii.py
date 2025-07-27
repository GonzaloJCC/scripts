from PIL import Image

IMAGE_NAME = "img_name"
IMAGE_EXTENSION = ".jpg"
NEW_SIZE_RATIO = 25

def main() -> None:

    img_name = IMAGE_NAME
    img_extension = IMAGE_EXTENSION

    img = Image.open(f"{img_name}{img_extension}")
    if not img:
        print("Image not found")
        return
    
    width, height = img.size

    # ASCII characters are much bigger than a pixel, so it's necesary to resize the image
    
    new_width = width * 2 // NEW_SIZE_RATIO
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.43)  # 0.3 factor to correct for ASCII char height/width ratio
    img = img.resize((new_width, new_height))
    width, height = img.size


    grid = []
    for _ in range (height):
        grid.append([" "] * width)

    ascii_characters = {
    '@': 0,
    '#': 51,
    '8': 102,
    '&': 153,
    '%': 204,
    '$': 255,
    '*': 306,
    '+': 357,
    '=': 408,
    '-': 459,
    ':': 510,
    '.': 561
}

    img = img.convert("RGB") # Converts each pixel to an RGB tuple (0 - 255, 0 - 255, 0 - 255)
    pix = img.load() # Loads all the pixels

    for y in range(height):
        for x in range(width):
            r, g, b = pix[x, y]
            brightness = 0.299*r + 0.587*g + 0.114*b
            scaled_brightness = brightness * (612 / 255)  # Scale to match max ascii value

            if scaled_brightness <= ascii_characters['@']:
                grid[y][x] = '@'
            elif scaled_brightness <= ascii_characters['#']:
                grid[y][x] = '#'
            elif scaled_brightness <= ascii_characters['8']:
                grid[y][x] = '8'
            elif scaled_brightness <= ascii_characters['&']:
                grid[y][x] = '&'
            elif scaled_brightness <= ascii_characters['%']:
                grid[y][x] = '%'
            elif scaled_brightness <= ascii_characters['$']:
                grid[y][x] = '$'
            elif scaled_brightness <= ascii_characters['*']:
                grid[y][x] = '*'
            elif scaled_brightness <= ascii_characters['+']:
                grid[y][x] = '+'
            elif scaled_brightness <= ascii_characters['=']:
                grid[y][x] = '='
            elif scaled_brightness <= ascii_characters['-']:
                grid[y][x] = '-'
            elif scaled_brightness <= ascii_characters[':']:
                grid[y][x] = ':'
            elif scaled_brightness <= ascii_characters['.']:
                grid[y][x] = '.'
            else:
                grid[y][x] = ' '


    with open(f"{img_name}.txt", "w") as new_image:
        for row in grid:
            new_image.write("".join(row)+"\n")
        print("All done! :)")


if __name__ == "__main__":
    main()