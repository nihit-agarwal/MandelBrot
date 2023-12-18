from PIL import Image


depth = 100
width = 20000
height = 20000
scale = 0.0001


def convergenceCheck(num: complex):
    prev = complex(0,0)
    i = 0
    while (prev.real**2 + prev.imag**2 <= 4 and i <= depth):
            prev = prev * prev + num
            i += 1
    if i > depth:
        return True
    else:
        return False


def create():
    print("Attempt to create the mandelbrot set image")
    image = Image.new("RGB", (width, height), "white")
    pixels = image.load()
    for i in range(height):
        for j in range(width):
            x = (j - width/2) * scale
            y = (height/2 - i) * scale
            comp_num = complex(x,y)
            if convergenceCheck(comp_num):
                pixels[j,i] = (0,0,0)
            else:
                pixels[j,i] = (255,0,0)

    image.save("SingleThread.png")


if __name__ == '__main__':
    #main()
    create()