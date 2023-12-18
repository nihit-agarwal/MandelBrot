# Importing libraries
from PIL import Image
import threading
def main():
    print("Inside the main block")
    c = complex(0.1,0.5)
    n = 10
    inSet = checkConvergence(c,n)
    print(f"{c} is in the Mandelbrot set: {inSet}")

def create():
    print("Attempt to create the mandelbrot set image")
    width = 2000
    height = 2000
    image = Image.new("RGB", (width, height), "white")
    pixels = image.load()
    scale = 0.001
    n = 1000
    array = []
    for i in range(height):
        for j in range(width):
            x = (j - width/2) * scale
            y = (height/2 - i) * scale
            c = complex(x,y)
            array.append(c)
    num_threads = 8
    threads = []
    start = 0
    print(len(array))
    for th in range(num_threads):
        stop = int(start + height * width / num_threads)
        threads.append(threading.Thread(target=checkConvergence, args=(array, n, start, stop)))
        threads[-1].start()
        start = stop
    for th in range(num_threads):
        threads[th].join()
    for i in range(height):
        for j in range(width):
            if array[i * width + j]:
                pixels[j,i] = (0,0,0)
            else:
                pixels[j,i] = (255,0,0)
    image.save("Mandelbrot.png")
def verify(z):
    if z.real ** 2 + z.imag ** 2 > 4:
        return False
    else:
        return True
def mandelbrot(n,c):
    if n == 0:
        return 0
    elif n < 0:
        return None
    z = complex(mandelbrot(n - 1, c)) ** 2 + c
    #print(z)
    return z

def checkConvergence(arr,n, start, stop):
    # arr is a complex number array
    # n is the threshold beyond which number is expected to converge
    # start index for thread
    # stop (exclusive)
    for iterations in range(start,stop):
        i = 0
        prev = complex(0,0)
        while (prev.real**2 + prev.imag**2 <= 4 and i <= n):
            prev = prev * prev + arr[iterations]
            i += 1
        if i > n:
            arr[iterations] = True
        else:
            arr[iterations] = False

if __name__ == '__main__':
    #main()
    create()