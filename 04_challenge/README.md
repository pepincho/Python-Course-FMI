Задачата е да напишете функция def stats(path_to_directory), която връща следния речник:

{
    'classes': брой класове,  # int (default 0)
    'functions': брой функции,  # int (default 0)
    'unpleasant_functions': ['[path/to/file.py]#[function_name]', ...]  # list (default [])
}
Представляващ статистика, касаеща всички .py файлове намиращи се в зададената директория.

Неприятна функция наричаме функция с 3 или повече нива на влагане вътре в нея. За ниво на влагане се броят:

if / else
while
for
with
try/except
Например функцията:

def unpleasant_one():
    for x in ["smiling", "girl"]:
        for y in ["cool", "long beard", "boy"]:
            if x == 'girl' and y == 'long beard':
                print("А {} {}!".format(y, x))
Е "неприятна" понеже има 3 нива на влагане в себе си.

NOTE:

Няма да имате функции, дефинирани в тялото на функции
Методите на класовете ги разглеждаме като функции
Ако path_to_directory не е валиден, хвърляйте NotADirectoryError
Ако имаме:
path_to_directory=/baba
вътре в baba директория baba
във вътрешната baba файл baba.py
в baba.py, неприятна фунцкия с име "baba"
то стринга "/baba/baba/baba.py#baba", трябва да бъде в unpleasant_functions.

