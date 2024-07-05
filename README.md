### Hexlet tests and linter status:
[![Actions Status](https://github.com/sva24/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sva24/python-project-50/actions)
[![Github Actions Status](https://github.com/sva24/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/hexlet-boilerplates//sva24/python-project-50)
### Code Climate maintainability and test coverage:
[![Maintainability](https://api.codeclimate.com/v1/badges/020fc5d7072cab8e21cf/maintainability)](https://codeclimate.com/github/sva24/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/020fc5d7072cab8e21cf/test_coverage)](https://codeclimate.com/github/sva24/python-project-50/test_coverage)


### 🖥️ Вычислитель отличий
Вычислитель отличий – программа, которая определяет разницу между двумя структурами данных. 

Возможности утилиты:

Поддержка разных входных форматов: yaml, json
Генерация отчета в виде plain text, stylish и json

## 🔨 Минимальные требования
python >=3.10  
pytest-cov >= 5.0.0  
pyyaml >= 6.0.1  

## 🛠️ Установка
git clone https://github.com/sva24/python-project-50.git  
cd python-project-50
make install  
make build   
make package-install


## 💡 Запуск утилиты:

- `gendiff -h`
  Запускает справку по утилите:

usage: gendiff.cmd [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output

- `gendiff file1.json file2.json`
Запускает сравнение двух файлов. Форматер по умолчанию указан 'stylish'.

- `gendiff -f plain file1.json file2.json`
Запускает сравнение двух файлов с форматером 'plain'. Отражает ситуацию, словно мы объединили второй объект с первым.

- `gendiff -f json file1.json file2.json`
Запускает сравнение двух файлов с форматером 'json'. Выводит сравнение в формате JSON.


## 📺 Запись демонстрации работы программы:

## Плоские файлы JSON
[![asciicast](https://asciinema.org/a/c2P7s1rGdb7qo5nNroghUrv3r.svg)](https://asciinema.org/a/c2P7s1rGdb7qo5nNroghUrv3r)

##  Плоские файлы YAML
[![asciicast](https://asciinema.org/a/lTi3WnUhmbEa00HIshMGqhTz6.svg)](https://asciinema.org/a/lTi3WnUhmbEa00HIshMGqhTz6)

## Файлы JSON и YAML с вложенной структурой
[![asciicast](https://asciinema.org/a/od3RZ3QppXcxK3Nu2WvwJ6dAK.svg)](https://asciinema.org/a/od3RZ3QppXcxK3Nu2WvwJ6dAK)

## Плоский формат plain
[![asciicast](https://asciinema.org/a/ESeW3HKqfBmzVlL0m0wCILrSG.svg)](https://asciinema.org/a/ESeW3HKqfBmzVlL0m0wCILrSG)

## Формат JSON
[![asciicast](https://asciinema.org/a/e9kauiqyzTr7Hok4YHmS5oDxV.svg)](https://asciinema.org/a/e9kauiqyzTr7Hok4YHmS5oDxV)
