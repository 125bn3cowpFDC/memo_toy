import os, getpass, pickle

class Data:
    def __init__(self) -> None:
        self.memo_data = self.make_dir()+"\\soobmemp.pickle"
        self.detail_list = self.open_file(self.memo_data)
    
    #confirm direction
    def make_dir (self):
        user_name = getpass.getuser()
        data_place = "c:\\users\\"+user_name+"\\Soobmemo"
        if not os.path.isdir(data_place):
            os.mkdir(data_place)
        else:
            pass

        return data_place

    #make file
    def open_file(self,memo_data):
        if not os.path.isfile(memo_data):
            detail_list = {} 
            with open(memo_data,'wb') as fw:
                pickle.dump(detail_list, fw)
            return detail_list
        else:
            with open(memo_data, 'rb') as fr:
                detail_list = pickle.load(fr)
            return detail_list