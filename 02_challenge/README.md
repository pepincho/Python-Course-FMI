# Черно и бяло

За целта на това предизвикателство ще трябва да се поразровите малко и да откриете начин да обърнем нормална картинка до черно-бяла такава (grayscale). Ще очакваме да напишете декоратор grayscale, за функциите rotate_left, rotate_right, invert, darken и lighten от първа задача.

Пример:

Написали сме си rotate_left от първа задача (ако не сте, можете да използвате някое решение на ваш колега, тъй като са вече публични) и изглежда така:

```
def rotate_left(image):
    return list(zip(*image))[::-1]
```
Ще използваме отново снимка на една малка панда:

![Панда](https://raw.githubusercontent.com/pepincho/Python-Course-FMI/master/02_challenge/panda.jpg)


И ако я подадем на rotate_left използвайки render.py:

```python render.py panda.jpg rotate_left```
получаваме:

![Завъртяна на ляво панда](https://raw.githubusercontent.com/pepincho/Python-Course-FMI/master/01_task/panda_rotate_left.jpg)

Ако обаче декорираме ```rotate_left``` с ```@grayscale```:
```
@grayscale
def rotate_left(image):
    return list(zip(*image))[::-1]
```
резултатът ще бъде:

![Завъртяна на ляво черно-бяла панда](https://raw.githubusercontent.com/pepincho/Python-Course-FMI/master/02_challenge/panda_rotate_left.jpg)
