# Обзор сторонних библиотек Python
# Библиотека pillow
from PIL import Image
import time

im = Image.open("cat_123.jpg")
im_2 = im.copy()  # создание копии изображения
im_2.thumbnail((500, 600))   # изменяем размеры исходного изображения im_2
im_3 = im.transpose(Image.FLIP_TOP_BOTTOM) # вертикальный зеркальный образ

im.show() # метод show для просмотра изображения
time.sleep(2)
im_2.show()
time.sleep(2)
im_3.show()

# Сохраним изображения в виде анимированного GIF
image_filenames = ["k1.jpg", "k2.jpg", "k3.jpg",]
images = [Image.open(filename) for filename in image_filenames]
images[0].save(
    "animated_cat.gif",
    save_all=True,
    append_images=images[1:],
    duration=500,  # длительность каждого кадра в милисекундах
    loop=0,
)


# Библиотека requests
import requests

r = requests.get('http://github.com/')
print(r.url)
print(r.status_code)
print(r.history)











