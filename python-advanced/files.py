# # opening and reading files/folders

# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()

# import os

# os.getcwd()
# # list everything in dir. Can pass a dir as a string to see more specific file types
# os.listdir()

# # move files
# import shutil

# shutil.move('practice.txt', 'C:\Users\crash\onedrive\desktop\python-course')

# # delete file
# os.unlink(path) # deletes file at the path provided
# os.rmdir(path) # deletes a folder at the path provided
# shutil.remtree(path) #most dangerous as it will remove allt he files and folders in the path 

# # one deleted, the methods cannot be reversed

# # pip install send2trash is a safer module to use so the deleted files arent permantly removed
# os.getcwd()
# file_path = 'C:\Users\crash\onedrive\desktop\python-course\python-basics'
# for folder, sub_folders, files in os.walk(file_path):
#     print(f"Currently looking at: {folder}")
#     print("\n")
#     print('The subfolders are: ')
#     for sub_fold in sub_folders:
#         print(f"Subfolders: {sub_fold}")

#     print('\n')
#     print('the files are: ')
#     for f in files:
#         print(f"File: {f}")
#     print('\n')