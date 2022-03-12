from PIL import Image
image = Image.open("example.jpg")

red, green, blue = image.split()

shift_pixels = 200
transparency = 0.5
size_max = (80, 80)

coordinates_red = (shift_pixels, 0, image.width, image.height)
cropped_red_1 = red.crop(coordinates_red)

coordinates_cutting_two_sides = (shift_pixels/2, 0, (image.width - shift_pixels/2), image.height)
coordinates_blue = (0, 0, (image.width - shift_pixels), image.height)

cropped_red_2 = red.crop(coordinates_cutting_two_sides)
blend_rad = Image.blend(cropped_red_1, cropped_red_2, transparency)

cropped_blue_1 = blue.crop(coordinates_blue)
cropped_blue_2 = blue.crop(coordinates_cutting_two_sides)
blend_blue = Image.blend(cropped_blue_1, cropped_blue_2, transparency)

cropped_green = green.crop(coordinates_cutting_two_sides)

new_image = Image.merge('RGB', (blend_rad, cropped_green, blend_blue))

new_image.save('original_image.jpg')

new_image.thumbnail(size_max)

new_image.save('mini_image.jpg')