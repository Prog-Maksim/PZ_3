import os
import shutil

# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в PZ_7.1.py. Вывести в консоль информацию о размере
# файлов в папке test.

os.chdir('../../')
os.makedirs('test/test1', exist_ok=True)

file_from_pz6_1 = 'PZ_6/PZ_6.1.py'
file_from_pz6_2 = 'PZ_6/PZ_6.2.py'
file_from_pz7 = 'PZ_7/PZ_7.1.py'

shutil.move(file_from_pz6_1, 'test/')
shutil.move(file_from_pz6_2, 'test/')
shutil.move(file_from_pz7, 'test/test1/test.txt')

files_in_test = [f for f in os.listdir('test') if os.path.isfile(os.path.join('test', f))]
for file in files_in_test:
    file_size = os.path.getsize(os.path.join('test', file))
    print(f"Размер файла {file} в папке test: {file_size} байт")
