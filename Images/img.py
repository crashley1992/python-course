from PIL import Image

mac = Image.open('example.jpg')

# gives width and height
mac.size

mac.format_description

# cropping images xy,width,height are coordinates needed
mac.crop((0,0,100,100))

# opens image in computer, windows will open it up with image gallery app
# mac.show()

pencils = Image.open('pencils.jpg')

pencils.size

# x = 0
# y = 0

# # grabs 30% of image width
# w = 1950 / 3 
# h = 1300 /10

# pencils.crop((x,y,w,h))

# bottom pencils
x = 0
y = 0

w = 1950 / 3 
h = 1300 

pencils.crop((x,y,w,h))

halfway = 1993/2

x = halfway - 200
w = halfway + 200

y = 800
h = 125

computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))