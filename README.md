# launch_parser
Простой парсер для .launch-файлов

## Описание

Данная библиотека предоставляет возможности для парсинга .launch файлов, получения, изменения и сохранения аргументов из них

## Использование

### LaunchParser

Класс **LaunchParser** парсит xml-файл и находи в нем все элементы, имеющие тег **arg**. 
```python
parser = LaunchParser(file, rules)
args = parser.get_args()
```
Здесь **file** - имя .launch-файла, **rules**-список, содержащий правила, по которым нужно выполнить парсинг. Для получения данного списка правил необходимо использовать
класс **LaunchDescription**. 
Функция **get_args** возвращает список объектов типа **Argument** для дальнейшей работы с ними.

### LaunchDescription

Класс **LaunchDescription** считывает описания .launch-файлов из файла и позволяет получить список правил для последующего парсинга.
```python
description = LaunchDescription(descriprion_filename)
rules = description.get_file_description(launch_filename)
```
Здесь **descriprion_filename** - имя файла, содержащего описания, **launch_filename** - имя .launch-файла, парсинг которого будет производиться.

### Argument

Класс **Argument** позволяет получать значение аргумента, выполнять запись а также производить проверку.
Данный класс имеет дочерние классы:
* ArgumentBool - логические аргументы
* ArgumentStr - строковые аргументы
* ArgumentInt - целочисленные аргументы
* ArgumentFloat - аргументы с плавающей точкой
* ArgumentEnum - перечисления

Методы класса **Argument**:
* get - получить значение
* get_name - получить имя аргумента
* get_datatype - получить тип данных аргумента
* set - записать значение
