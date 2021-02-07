import math

f = open("image.ppm", "w")
f.write("P3 500 500 255\n")

for x in range(500):
    for y in range(500):
        r = int(math.sqrt(x * y) % 256)
        g = int(math.sqrt(x) % 256)
        b = int(math.sqrt(y) % 256)

        f.write(f"{r} {g} {b} ")

f.close()