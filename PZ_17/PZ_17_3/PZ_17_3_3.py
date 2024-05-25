import os

# Найти файл с самым коротким именем в папке PZ_11
os.chdir('../../PZ_11')
shortest_name_file = min((f for f in os.listdir() if os.path.isfile(f)), key=len)
print("Файл с самым коротким именем:", os.path.basename(shortest_name_file))