import os
import os.path


def get_sql_files(files):
    find_sql_files_list = list()
    for file in files:
        if file.endswith(".sql"):
            find_sql_files_list.append(file)
    return find_sql_files_list


def search_in_file(migrations_path, find_files_list):
    find_files_list = find_files_list[:]
    for file in find_files_list:
        with open(os.path.join(migrations_path, file)) as f:
            data = f.read()
            if user_input.lower() in data:
                find_files_list.append(file)
            find_files_list.remove(file)
    return find_files_list


local_path = os.path.dirname(os.path.realpath(__file__))
migrations_path = os.path.join(local_path, 'Migrations')

files = os.listdir(migrations_path)

find_files_list = get_sql_files(files)

while len(find_files_list) > 1:
    user_input = input("Введите строку:")
    find_files_list = search_in_file(migrations_path, find_files_list)
    for file in find_files_list:
        print(file)
    print("Всего: ", len(find_files_list))



