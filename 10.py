from PIL import Image
filename = "buildings.jpg"
with Image.open(filename) as img:
    img.load()
# cropped = image.crop((177, 882, 1179, 1707))
# cropped.save(('/path/to/photos/cropped_jelly2.png'))