import cv2
from PIL import Image
import numpy as np

# biblioteka opencv-python
def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image_cv(path): 
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(type(img))
    show_image(img) # funckja napisana wyzej
    return img


def read_image_PIL(path):
    im = Image.open(path)
    try:
        print(im)
    except:
        print(type(im))
    im.show()
    return im


print("Biblioteka OpenCV") # obraz jako tablica kolorów
image = read_image_cv("image.jpg")

# # Biblioteka pillow
# print("Biblioteka Pillow") # obraz jako obiekt klasy PIL
# read_image_PIL("image.jpg")

# 1. Flip obrazka
# Flip obrazka do góry nogami - algorytm
def reverse_short(img):
    img_reverse = img[::-1]
    return img_reverse

show_image(reverse_short(image))

# Flip obrazka do góry nogami - wersja wbudowana
show_image(cv2.flip(image,0))


# 2. Skala szarości
def gray_scale(img):
    for row in range(img.shape[0]): # 175
        for column in range(img.shape[1]): # 288
            gray = int(sum(img[row][column])/3)  # R+G+B /3 = średnia
            img[row][column][0] = gray
            img[row][column][1] = gray
            img[row][column][2] = gray
    return np.array(img)

show_image(gray_scale(image))

show_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))