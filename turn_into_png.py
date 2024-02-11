from PIL import Image

# Open the JPG file
jpg_image = Image.open('/home/elburs27/Desktop/py.13/Projects/drogan/frst_with_wizard.jpg')

# Save as PNG
jpg_image.save('frst_with_wizard.png', 'PNG')
