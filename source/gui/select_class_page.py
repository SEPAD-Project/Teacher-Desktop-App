from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkOptionMenu, CTkProgressBar, NORMAL, DISABLED
from main_page_teacher import main_page_func_teacher
import ast
from pathlib import Path
import sys
import threading
import time

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "database-code"))
from searching import get_class_name

class SelectClassPage(CTk):
    def __init__(self, udata):
        super().__init__()
        self.udata = udata
        print(udata[3])
        self.title("Select Class Page")
        self.geometry('650, 550')
        self.minsize(650, 550)
        
        # Main red frame
        self.main_frame = CTkFrame(master=self, border_color='red', border_width=2)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        # Elements frame
        self.element_frame = CTkFrame(master=self.main_frame, fg_color='transparent')
        self.element_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # GUI elements
        self.welcome_label = CTkLabel(master=self.element_frame, 
                                    text=f'Welcome {udata[0]} {udata[1]}', 
                                    font=('montserrat', 30, 'bold'))
        
        self.progress_bar = CTkProgressBar(master=self.element_frame, width=350)
        self.status_label = CTkLabel(master=self.element_frame, text="Initializing...")
        
        self.select_class_optionbox = CTkOptionMenu(master=self.element_frame, 
                                                  values=['processing ...'], 
                                                  height=40, 
                                                  width=350, 
                                                  font=('montserrat', 20, 'bold'),
                                                  )
        
        self.join_button = CTkButton(master=self.element_frame, 
                                   text='Join to Class', 
                                   font=('montserrat', 20, 'bold'), 
                                   height=30, 
                                   width=350, 
                                   border_color='white', 
                                   border_width=2,
                                   command=self.join_to_class)

        self.Retrying_button = CTkButton(master=self.element_frame, 
                                   text='Retrying', 
                                   font=('montserrat', 20, 'bold'), 
                                   height=30, 
                                   width=350, 
                                   border_color='white', 
                                   border_width=2,
                                   command=self.Retrying_func)
        
        self.exit_button = CTkButton(master=self.element_frame, 
                                    text='Exit', 
                                    font=('montserrat', 20, 'bold'), 
                                    height=30, 
                                    width=350, 
                                    fg_color='red', 
                                    hover_color='#6B0011', 
                                    border_color='white', 
                                    border_width=2, 
                                    command=self.destroy)

        # Layout
        self.welcome_label.grid(row=0, column=0, pady=20)
        self.progress_bar.grid(row=1, column=0, pady=20)
        self.status_label.grid(row=2, column=0)
        self.select_class_optionbox.grid(row=3, column=0, pady=20)
        self.join_button.grid(row=4, column=0)
        self.Retrying_button.grid(row=5, column=0, pady=20)
        self.exit_button.grid(row=6, column=0)

        # Start background processing
        threading.Thread(target=self.start_processing).start()

    def start_processing(self):
        self.join_button.configure(state=DISABLED,height=30,width=350)
        self.Retrying_button.configure(state=DISABLED,height=30,width=350)
        self.select_class_optionbox.configure(state=DISABLED)
        self.processing_thread = threading.Thread(target=self.Decryption_and_translate, daemon=True)
        self.processing_thread.start()

    def update_progress(self, value, text):
        self.progress_bar.set(value)
        self.status_label.configure(text=text)
        self.update_idletasks()

    def Decryption_and_translate(self):
        try:
            # Stage 1: Decryption
            self.after(0, self.update_progress, 0.3, "Decryption class data...")
            time.sleep(1)  # Simulate processing
            print(self.udata[3])
            print(type(self.udata[3]))
            if self.udata[3] != '[]':
                self.list_from_string = ast.literal_eval(self.udata[3])
                print(1)
                print(self.list_from_string)
                self.decrypted_list = [(str(int(code.split('#')[0], 16))+ '-' +(''.join(chr(int(h, 16) ^ ord('crax6ix'[i % len('crax6ix')])) for i, h in enumerate(code.split('#')[1].split('-'))))) for code in self.list_from_string]
                print(5)
                print(self.decrypted_list)
                # Stage 2: Translating
                self.after(0, self.update_progress, 0.6, "Translating class names...")
                time.sleep(1)  # Simulate processing
                self.school_name = {i.split('-')[0]:get_class_name(i.split('-')[0]) for i in self.decrypted_list} # code:name
                self.translated_list = [f"{self.school_name[i.split('-')[0]]}-{i.split('-')[1]}" for i in self.decrypted_list]
                print(9)
                print(self.translated_list)
                # Final stage
                self.after(0, self.update_progress, 1.0, "Loading completed!")
                time.sleep(0.5)
                self.select_class_optionbox.configure(state=NORMAL)
                self.select_class_optionbox.configure(values=self.translated_list)
                self.select_class_optionbox.set(self.translated_list[0])
                self.join_button.configure(state=NORMAL,height=30,width=350)
                self.Retrying_button.configure(state=NORMAL,height=30,width=350)
            
            else:
                self.after(0, self.update_progress, 1.0, "Loading completed!")
                # self.status_label.configure(text=f"FINISHED")
                self.select_class_optionbox.configure(state=NORMAL)
                self.select_class_optionbox.set('You don’t have any classes')
                self.select_class_optionbox.configure(state=DISABLED)
                self.Retrying_button.configure(state=NORMAL,height=30,width=350)
        
        except Exception as e:
            self.progress_bar.configure(progress_color="red")
            self.after(0, self.update_progress, 1.0, "CONNECTION ERROR OCCURED : CHECK YOUR INTERNET")
            self.status_label.configure(text="CONNECTION ERROR OCCURED : CHECK YOUR INTERNET", text_color= 'red')
            self.select_class_optionbox.configure(state=NORMAL)
            self.select_class_optionbox.set('ERROR')
            self.select_class_optionbox.configure(state=DISABLED)
            self.Retrying_button.configure(state=NORMAL,height=30,width=350)

    def join_to_class(self): # self.list_from_string
        class_id = self.select_class_optionbox.get()
        class_unic_code = self.list_from_string[self.translated_list.index(class_id)]
        school_code = [code for code, name in self.school_name.items() 
                      if name == class_id.split('-')[0]]
        if school_code:
            self.destroy()
            main_page_func_teacher(school_code[0], 
                                  class_id.split('-')[0], 
                                  class_id.split('-')[1],
                                  class_unic_code)

    def Retrying_func(self):
        def thread_handler():
            self.status_label.configure(text_color= 'white')
            self.progress_bar.configure(progress_color="#1f6aa5")
            self.Retrying_button.configure(state=DISABLED,height=30,width=350)
            self.join_button.configure(state=DISABLED,height=30,width=350)
            self.select_class_optionbox.configure(state=NORMAL)
            self.select_class_optionbox.set('Retrying ...')
            self.select_class_optionbox.configure(state=DISABLED)
            self.start_processing()

        threading.Thread(target=thread_handler).start()




    def run(self):
        self.mainloop()

def select_class_page_func(udata):
    app = SelectClassPage(udata)
    app.run()

if __name__ == '__main__':
    # For testing
    test_data = ("John", "Doe", "john@example.com", "['7b#52-42-54-4a', '7b#52-42-54-4a', '7b#52-42-54-4a']")
    select_class_page_func(test_data)