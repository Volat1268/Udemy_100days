import colorgram


colors = colorgram.extract("image.jpg", 100)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_rgb_color = (r, g, b)
    rgb_colors.append(new_rgb_color)
print(rgb_colors)