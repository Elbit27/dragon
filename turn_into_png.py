from PIL import Image

# Open the JPG file
jpg_image = Image.open('/home/elburs27/Desktop/py.13/Projects/dragon/media/photo_2024-02-17_20-27-52.jpg')

# Save as PNG
jpg_image.save('mauntain.png', 'PNG')
