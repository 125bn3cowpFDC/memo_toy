import pickle
class Controller:
    def __init__(self,model, view,main) -> None:
        self.main = main
        self.model = model
        self.view = view
        self.deleteView = None
        self.detail_list = self.model.detail_list
        self.box_list = list(self.detail_list.keys())
        self.box_pos = 0

    def init_return(self):
        self.view.data_setting(self.box_list)
    
    def box_selec_return(self,pos):
        self.box_pos = pos
        self.box_list.reverse()
        self.view.box_select(self.detail_list,self.box_list,self.box_pos)
        self.box_list.reverse()

    def data_in_return(self,text):
        if text != "":
            self.box_list.append(text)
            self.detail_list[text] =""
            self.view.data_in(text)
        
    def detail_in_return(self,details):
        self.box_list.reverse()
        if details != "":
            self.detail_list[self.box_list[self.box_pos]] = details
        self.box_list.reverse()
        
    def delete_call_return(self):
        self.view.delete_w_make()

    def get_d_info(self,detail_list,box_list,box_pos):
        self.box_pos = box_pos
        self.detail_list = detail_list
        self.box_list = box_list


    def quit_return(self):
        with open(self.model.memo_data,'wb') as fw:
            pickle.dump(self.detail_list, fw)
        
