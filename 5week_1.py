import os

def folder_file(folder):
    for (root, directories, files) in os.walk( folder ):
        print(f'root : {root}')
        print(f'directories : {directories}')
        for file in files:
            print(f'파일 이름      {file}')
            print(f'파일 full path {os.path.join(root, file)}')

folder_file(r"C:\Users\airto\Desktop\NEST")