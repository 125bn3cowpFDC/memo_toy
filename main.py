import tkinter
import myData
import mainView
import mainController

class Main(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("230x380+0+0")
        self.title("SoobMemo")
        self.wm_attributes('-toolwindow','True')
        self.protocol("WM_DELETE_WINDOW", self.quit)
        
        data = myData.Data()
        
        view = mainView.View(self)
        view.grid(row=0,column=0) 

        self.controller = mainController.Controller(data,view,self)
        view.set_controller(self.controller)
        
    def quit(self):
        self.controller.quit_return()
        self.destroy()
        
if __name__ == '__main__':
    main = Main()
    main.mainloop()