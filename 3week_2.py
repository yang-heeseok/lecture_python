import win32com.client as win32
import PySimpleGUI as sg

sg.theme("GrayGrayGray")

layout = [
    [
        sg.Text('작업할 파일 : ', size=(15,1)),
        sg.Input(size=(55, 20), key="-FILE-" , change_submits=True), 
        sg.FilesBrowse(file_types=(("hwp Files", "*.hwp"), ("hwpx Files", "*.hwpx")))
    ],
    [sg.Button('Ok'), sg.Button('Exit')],
]

window = sg.Window('지식쟁이 파이썬 공부', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event in ('Ok'):
        hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
        hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
        hwp.XHwpWindows.Item(0).Visible = True
        hwp.Open(values['-FILE-'])
        count = 0
        tourCtrl = hwp.HeadCtrl
        while tourCtrl:
            if tourCtrl.CtrlID == "en":
                count += 1
            tourCtrl = tourCtrl.Next
                
        print(f'이 문서의 미주는 {count} 개 입니다.')
        hwp.Quit()
        
window.close()



