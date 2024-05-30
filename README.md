# SoobMemos
- Language : Python3.8
- Library : Tkinter, os, getpass
---
## Design Pattern
- MVC기반

![image](https://github.com/125bn3cowpFDC/memo_toy/assets/170291905/f4c6e538-f94c-48c2-9e5c-027291a4b0e1)

- data - 저장 된 데이터 공간 <독립적, 자체 변형x>
- MainView - 메인 ui 속성 정의 및 배치 <독립적, 자체 변형x, controller변형 금지>
- DeleteView - 삭제 재확인 ui 정의 및 배치 <독립적, 자체 변형x, controller변형 금지>
- MainViewController - MainView 이벤트 발생 시 이벤트 발생 값 참조 후 MainView 변경
- DeleteViewController - DeleteView 이벤트 발생 시 이벤트 발생 값 참조 후 DeleteView 변경



! **view의 변화:  이벤트(view) → 데이터 및 view 변경 요소 결정(controller) → 변화(view)**
```
#one of call controller from view
def data_in_call(self,event):
    self.control.data_in_return(self.insert.get())

#one of data update in controller
def data_in_return(self,text):
    if text != "":
        self.box_list.append(text)
        self.detail_list[text] =""
        self.view.data_in(text)

#one of data update view from controller
def data_in(self,text):
    self.e_words.set("")
    self.box.insert(0,text)
```
---
## UI in each View
mainview
```
def ui_src(self,window):
    
    #insert
    self.insert = tkinter.Entry(window,width=25,textvariable=self.e_words)
    self.insert.bind("<Return>", self.data_in_call)
    self.insert_btn = tkinter.Button(window, text='입력',width=6,command=self.data_in_call_b)
    #list
    self.box = tkinter.Listbox(window,width=25,height=8)
    self.box.bind("<Double-Button-1>", self.box_select_call)
    self.del_btn = tkinter.Button(window, text='삭제',width=6,state='disabled',command=self.delete_call)
    #details
    self.detail_label = tkinter.Label(window,textvariable=self.pos_words)
    self.detail_text = tkinter.Text(window,width=25,height=15)
    self.detail_save = tkinter.Button(window, text='저장', width=6,command=self.detail_in_call)

    
    
def ui_grid(self):        
    self.insert.grid(row=0,column=0)
    self.insert_btn.grid(row=0,column=1)
    self.box.grid(row=1,column=0)
    self.del_btn.grid(row=1,column=1)
    self.detail_label.grid(row=2,column=0)
    self.detail_save.grid(row=3,column=1)
    self.detail_text.grid(row=3,column=0)
```
subview(warning)
```
class DeleteW (tkinter.Toplevel):
    def __init__(self,main):
        super().__init__(main)
        self.geometry("200x80")
        self.title("삭제")
        self.wm_attributes('-toolwindow','True')
        self.y_btn = tkinter.Button(self, text='삭제',width=6,command=self.yes_call)     
        self.n_btn = tkinter.Button(self, text='취소',width=6,command=self.nope_call)   
        self._label = tkinter.Label(self,text="정말로 삭제 하시겠습니까?")
        self.y_btn.place(x=20,y=40)
        self.n_btn.place(x=130,y=40)
        self._label.place(x=30,y=10)
```
