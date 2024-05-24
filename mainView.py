import tkinter
import deleteView
import deleteController
class View(tkinter.Frame):
    w_count = 0
    def __init__(self,main):
        self.main = main
        self.pos_words = tkinter.StringVar()
        self.e_words = tkinter.StringVar()
        self.pos_words.set("선택 목록: ")
        self.e_words.set("")
        super().__init__(main)
        self.ui_src(main)
        self.ui_grid()
        self.control = None
        
    def set_controller(self,controller):
        #print('call control')
        self.control = controller
        self.control.init_return()

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
        
    def data_setting(self,box_list):
        for i in range(len(box_list)):
            self.box.insert(0,box_list[i])
    
    def box_select_call(self,event):
        self.control.box_selec_return(self.box.curselection()[0])

    def box_select(self,detail_list,box_list,pos):
        print(detail_list, box_list)
        self.del_btn.config(state='active')
        self.detail_text.delete((1.0),"end")
        self.detail_text.insert((1.0),detail_list[box_list[pos]])
        self.pos_words.set("선택 목록: "+box_list[pos])
        #print(box_list[self.box.curselection()[0]])
    
    def data_in_call(self,event):
        self.control.data_in_return(self.insert.get())

    def data_in_call_b(self):
        self.control.data_in_return(self.insert.get())

    def data_in(self,text):
        self.e_words.set("")
        self.box.insert(0,text)

  
    def detail_in_call(self):
        self.control.detail_in_return(self.detail_text.get((1.0),'end'))

    def delete_call(self):
        self.control.delete_call_return()

    def delete_w_make(self):
        self.w_count+=1
        if self.w_count<2:
            self.delete_w = deleteView.DeleteW(self)
            self.d_controller = deleteController.Dcontroller(self,self.control,self.delete_w)
            self.delete_w.set_dcontroller(self.d_controller)
        

    def yes(self,box_pos):
        self.pos_words.set("선택 목록: ")
        self.box.delete(box_pos,box_pos)
        self.detail_text.delete((1.0),'end')

    def get_w_count(self,w_count):
        self.w_count = w_count

    def nope(self):
        pass