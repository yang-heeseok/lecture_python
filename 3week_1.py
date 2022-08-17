import win32com.client as win32

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")

hwp.XHwpWindows.Item(0).Visible = True

# hwp.Open(r"C:\Users\airto\Desktop\hwpTest.hwp")
hwp.Open(r"C:/Users/airto/Desktop/test.hwpx")

count = 0

############################################
tourCtrl = hwp.HeadCtrl

while tourCtrl:
    if tourCtrl.CtrlID == "tbl":
        count += 1
    tourCtrl = tourCtrl.Next
############################################
        
print(f'이 문서의 미주는 {count} 개 입니다.')

hwp.Quit()