import os
import time

read_file_one = 'one.txt'
read_file_two = 'two.txt'

write_file = 'three.txt'

# добавил /n после первой строки в первом домументе
file = open(r'one.txt', "r+")
print(file.write('string - 1 \n'))
# двигаю курсор
file.close()

# Объединяю файлы в один
open(r'three.txt', 'w').write(open(r'one.txt', 'r+').read() + open(r'two.txt', 'r').read())

#Проверка на присутствие файла  three.txt
file_true = r'three.txt'

if os.path.exists(file_true):
    print('Файл :', file_true, 'существует')
    # Текущая дириктория
    print(os.getcwd())
    # Время последнего доступа
    access_time = os.path.getctime(file_true)
    print(time.strftime('Время последнего доступа к файлу :  ' + '%d.%m.%Y, %H:%M:%S', time.localtime(access_time)))

else:
    print('Такого файла не существует ! \n ytn')
