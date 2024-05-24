import deleteView
class Dcontroller():
    def __init__(self,mainView,maincontrol,delete_w):
        self.delete_w = delete_w
        self.mainView = mainView
        self.maincontrol = maincontrol
        self.box_list = maincontrol.box_list
        self.detail_list = maincontrol.detail_list
        self.box_pos = maincontrol.box_pos
        self.w_count = self.mainView.w_count
        
    
    def yes_return(self): 
        self.box_list.reverse()
        del self.detail_list[self.box_list[self.box_pos]]
        del self.box_list[self.box_pos]
        self.box_list.reverse()      

        self.w_count = 0
        self.mainView.get_w_count(self.w_count)
        self.mainView.yes(self.box_pos) # to mainView
        self.maincontrol.get_d_info(self.detail_list,self.box_list,self.box_pos) # to mainControll
        self.delete_w.dquit() #to delete_window

    def nope_return(self):
        self.w_count = 0
        self.mainView.get_w_count(self.w_count)
        self.delete_w.dquit()
        
    
    