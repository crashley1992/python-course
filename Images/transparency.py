from PIL import Image

blue = Image.open('blue_color.png')
purple = Image.open('purple.png')
red = Image.open('red_color.jpg')

# will make an image more transparent. High number more solid the color
blue.putalpha(255)

# blending the images can be done by copy and pasting over them
blue.paste(im=red,box=(0,0),mask=red)
