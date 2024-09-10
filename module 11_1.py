import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from time import sleep
from labelme.utils import draw

a = np.array([[1, 2, 3],
              [4, 15, 6],
              [7, 8, 9]])
b = a * 2
c = a + b
print(f'Массив А:')
print(a)
print(f'Размер массива A равен {a.size}')
print(f'Сумма всех элементов массива A равна {a.sum()}')
print(f'Сренее арифметичесое всех элементов массива A равно {a.mean():.2f}')
print(f'Минимальное значение массива A равно {a.min()}')
print(f'Мфксимальное значение массива A равно {a.max()}')
sleep(1)
print(f'Массив B = A * 2:')
print(b)
sleep(1)
print(f'Массив C = A + B:')
print(c)
sleep(1)
a[a > 0] = 0
d = a
print(f'Массив D:')
print(d)

sleep(4)
print('_________')
image = Image.open('kitty2.jpg')
image.show()
print(f'Размер картинки: {image.size}')
image2 = image.resize((100, 170))
image2.save('test_kitty.jpg')
image2 = Image.open('test_kitty.jpg')
image2.show()
image3 = image.rotate(90)
image3.save('test2_kitty.jpg')
image3 = Image.open('test2_kitty.jpg')
image3.show()
image4 = image.crop((0, 0, int(image.width / 2), int(image.height / 2)))
image4.save('test3_kitty.jpg')
image4 = Image.open('test3_kitty.jpg')
image4.show()
image5 = image.filter(ImageFilter.BLUR)
image5.save('test4_kitty.jpg')
image5 = Image.open('test4_kitty.jpg')
image5.show()
font = ImageFont.truetype('arial.ttf', 40)
drawer = ImageDraw.Draw(image)
drawer.text((5, 5), "Поздравляем!", font=font, fill="black")
image6 = Image.open('test5_kitty.jpg')
image6.show()
