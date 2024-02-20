import os

def remove_string_from_filenames(directory_path, string_to_remove):
    # 1. گرفتن لیست فایل‌ها درون پوشه
    files = os.listdir(directory_path)

    # 2. حذف رشته مورد نظر از نام هر فایل
    for file_name in files:
        old_path = os.path.join(directory_path, file_name)
        
        # استفاده از replace برای حذف رشته مورد نظر
        new_name = file_name.replace(string_to_remove, "")
        new_path = os.path.join(directory_path, new_name)

        # 3. تغییر نام فایل
        os.rename(old_path, new_path)
        print(f"old name: {file_name}\nnew name: {new_name}\n")

def add_string_from_filenames(directory_path, new_name_prefix):
    # 1. گرفتن لیست فایل‌ها درون پوشه
    files = os.listdir(directory_path)

    # 2. تغییر نام هر فایل با افزودن پیشوند جدید
    for file_name in files:
        old_path = os.path.join(directory_path, file_name)
        new_name = f"{new_name_prefix}{file_name}"
        new_path = os.path.join(directory_path, new_name)

        # 3. تغییر نام فایل
        os.rename(old_path, new_path)
        print(f"old name: {file_name}\nnew name: {new_name}\n")

def replace_string_from_filenames(directory_path, old_name_str, new_name_str):
    # 1. گرفتن لیست فایل‌ها درون پوشه
    files = os.listdir(directory_path)

    # 2. تغییر نام هر فایل با افزودن پیشوند جدید
    for file_name in files:
        old_path = os.path.join(directory_path, file_name)
        new_name = file_name.replace(old_name_str,new_name_str)
        new_path = os.path.join(directory_path, new_name)

        # 3. تغییر نام فایل
        os.rename(old_path, new_path)
        print(f"old name: {file_name}\nnew name: {new_name}\n")

method = input("Enter number of operation\nconcat string : 1\nremove string : 2\nreplace string : 3\n")
print("\n"*2)

again = "1"

while again == "1" :
    
    while True : 
        directory_path = input("Enter your /path/folder/ : ")
        if method == "1":        
            user_string = input("The string you want to add: ")
            add_string_from_filenames(directory_path, user_string)
            break
        elif method == "2": 
            user_string = input("The string you want to remove: ")
            remove_string_from_filenames(directory_path, user_string)
            break
        elif method == "3": 
            old_name_str = input("Enter the old string you want to replace: ")
            new_name_str = input("Enter the new string : ")
            replace_string_from_filenames(directory_path,old_name_str,new_name_str)
            break

    again = input("Enter '1' for try again or press another key for exit : ")

