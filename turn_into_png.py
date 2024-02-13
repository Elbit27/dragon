from PIL import Image

# Open the JPG file
jpg_image = Image.open('two_caves.jpg')

# Save as PNG
jpg_image.save('two_caves.png', 'PNG')
