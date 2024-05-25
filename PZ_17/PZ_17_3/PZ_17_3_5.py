import os

# удалить файл test.txt.
test_file_path = '../../test/test1/test.txt'

os.remove(test_file_path)
print("Файл test.txt удален")