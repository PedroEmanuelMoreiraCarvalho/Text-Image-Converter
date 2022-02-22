from PIL import Image, ImageEnhance

image_text = ''

proportion = 0.1

density = 'Ñ@#W$9876543210?!abc;:+=-,._ '

image = Image.open('rammus.jpg')

w = int(image.size[0]*proportion)
h = int((image.size[1]*proportion)/2)

img_small = image.resize((w, h))
converter = ImageEnhance.Color(img_small)
bw_image = converter.enhance(0)
rgb_im = bw_image.convert('RGB')

for i in range(h):
	image_text+='\n'
	for o in range(w):
		r, g, b = rgb_im.getpixel((o, i))
		pixel_density = int(r/8.8)
		image_text+=(density[pixel_density])

with open('image text.txt', 'w') as f:
    f.write(image_text)

#by Ierokirykas