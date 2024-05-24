import tkinter
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

    
    def set_dcontroller(self,dcontroller):
        self.dcontroller = dcontroller
    
    def yes_call(self):
        self.dcontroller.yes_return()

    def nope_call(self):
        self.dcontroller.nope_return()

    def dquit(self):
        self.destroy()
    