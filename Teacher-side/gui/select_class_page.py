from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkOptionMenu
from main_page_teacher import main_page_func_teacher
import ast
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "database-code"))
from searching import get_class_name

class SelectClassPage(CTk):
    def __init__(self, udata):
        super().__init__()
        self.udata = udata
        self.title("Select Class Page")
        self.geometry('700x500')
        self.minsize(700, 500)
        # main red frame
        self.main_frame = CTkFrame(master=self, border_color='red', border_width=2)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        #elements frame for holdign eveything in center 
        self.element_frame = CTkFrame(master=self.main_frame, fg_color='transparent')
        self.element_frame.place(relx=0.5, rely=0.5, anchor='center')
        # elements 
        print(udata[3])
        self.list_from_string = ast.literal_eval(udata[3])
        # self.translated_list = [f'{str(int(i.split('#')[0], 16))}-{str(chr(i.split('#')[1]))}' for i in self.list_from_string]
        self.decrypted_list = [(str(int(code.split('#')[0], 16))+ '-' +(''.join(chr(int(h, 16) ^ ord('crax6ix'[i % len('crax6ix')])) for i, h in enumerate(code.split('#')[1].split('-'))))) for code in self.list_from_string]
        print(self.decrypted_list)
        self.school_name = {i.split('-')[0]:get_class_name(i.split('-')[0]) for i in self.decrypted_list} # code:name
        self.translated_list = [self.school_name[i.split('-')[0]]+'-'+i.split('-')[1] for i in self.decrypted_list]
        self.welcome_label = CTkLabel(master=self.element_frame, text=f'Welcom {udata[0]} {udata[1]}', font=('montserrat', 30, 'bold'))
        self.select_calss_optionbox = CTkOptionMenu(master=self.element_frame, values=self.translated_list, height=40, width=150, font=('montserrat', 20, 'bold'))
        self.join_button = CTkButton(master=self.element_frame, text='Join to Class', font=('montserrat', 20, 'bold'), height=30, width=250, border_color='white', border_width=2, command=self.join_to_class)
        self.exit_button = CTkButton(master=self.element_frame, text='Exit', font=('montserrat', 20, 'bold'), height=30, width=250, fg_color='red', hover_color='#6B0011', border_color='white', border_width=2, command=lambda: self.destroy())

        # placing elements in element_frame      
        self.welcome_label.grid(row=0, column=0 ,sticky='n')
        self.select_calss_optionbox.grid(row=1, column=0, pady=90)
        self.join_button.grid(row=2, column=0)
        self.exit_button.grid(row=3, column=0, pady=(10,0))

    def join_to_class(self):
        class_id = self.select_calss_optionbox.get()
        self.destroy()
        school_code = [i for i in self.school_name if self.school_name[i] == class_id.split('-')[0] ] # self.school_name[self.[class_id.split('-')[0]]]
        print(school_code[0])
        main_page_func_teacher(school_code[0], class_id.split('-')[0], class_id.split('-')[1])


    def run(self):
        self.mainloop()


def select_class_page_func(udata):
    app = SelectClassPage(udata)
    app.run()


if __name__ == '__main__' : 
    select_class_page_func()
