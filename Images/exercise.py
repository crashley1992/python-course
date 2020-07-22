from PIL import Image

words = Image.open('word_matrix.png')
mask = Image.open("mask.png")

mask.size
mask = mask.resize((1015,559))
mask.putalpha(200)

words.paste(mask,(0,0),mask)
words.show()