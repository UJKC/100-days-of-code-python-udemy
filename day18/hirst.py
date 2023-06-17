import colorgram

rgb_color = []
colors = colorgram.extract('day18\image.jpg', 6)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)
print(rgb_color)
good_color = [(132, 166, 205), (221, 148, 106)]