import zipfile
import os

def zip_dir(zip_name, dir_path):
    r""" 
    dir_path와 같은 위치에, zip_name을 가진 .zip 폴더 생성.
    - zip_name : 압축할 이름
    - dir_path : 대상 폴더 path
    => 비밀번호를 넣고 싶다.
    """
    print(f"name : {zip_name}, path : {dir_path}")
    zip_path = os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)), zip_name + '.zip')
    new_zips = zipfile.ZipFile(zip_path, 'w')
    dir_path = dir_path + '/'
 
    # 이 폴더 안의 모든 파일을 압축
    for (root, directory, files) in os.walk(dir_path):
        for file in files:
            print(file)
            path = os.path.join(root, file)
            # 압축할 파일 경로, 압축 파일 안에서 사용할 상대경로, 압축 타입(일반 압축)
            new_zips.write(
                path, arcname = os.path.relpath(
                    os.path.join(root, file), 
                    dir_path
                ), 
                compress_type = zipfile.ZIP_DEFLATED
            )
 
    new_zips.close()

zip_name = 'zip_테스트'
dir_path = r"C:\Users\airto\Desktop\00_groupStudy"
zip_dir(zip_name, dir_path)