import pandas as pd

def ex_read():
    file_path = r"C:\Users\airto\Desktop\study_test.xlsx"   # 파일 path
    st_name = '테스트'  # sheet 이름
    df = pd.read_excel(file_path, engine = "openpyxl", sheet_name=st_name)
    print(df)   # 확인하기

def ex_write():
    values = [
        [
            ['a','John Smith', '123 Main St.', 234],
            ['a','Jane Doe', '456 Maple Ave.', 228],
            ['a','Joe Schmo', '789 Broadway', 251]
        ],
        ['a','name', 'address', 'age']
    ]
    file_path = r"C:\Users\airto\Desktop\study_test.xlsx"   # 파일 path
    st_name = '테스트' # sheet 이름
    df_add = pd.DataFrame(values[0], columns = values[1])
    with pd.ExcelWriter(file_path, mode='w', engine='openpyxl') as writer:
        df_add.to_excel(writer, index=False, sheet_name=st_name)

ex_write()
# ex_read()