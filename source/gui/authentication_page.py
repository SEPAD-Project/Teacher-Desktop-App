from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkCheckBox, CTkTabview, CTkOptionMenu
from threading import Thread
from tkinter import messagebox
import sys
from requests import get, exceptions
from pathlib import Path

# System paths
sys.path.append(str(Path(__file__).resolve().parent.parent))
# imports after path configuration
from backend.login_page_db import check_auth
from backend.register_back import register_btn_func

from select_class_page import select_class_page_func

class TeacherSideAppLoginPage(CTk):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_window()

    def init_ui(self):
        """Initialize all UI components"""
        self.main_frame = CTkFrame(master=self, border_color='red', border_width=2)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        # Creating GUI elements in a separate thread
        Thread(target=self.create_widgets, daemon=True).start()

    def setup_window(self):
        """Configure main window settings"""
        self.geometry('600x500')
        self.minsize(600, 500)
        self.title('Teacher Side Login Page')

    def create_widgets(self):
        """Create and arrange GUI elements"""

        self.tabv = CTkTabview(self.main_frame)
        self.tabv.add('Login')
        self.tabv.add('Register')
        self.tabv.set('Login')
        self.tabv.pack(padx=20, pady=20,fill='both', expand=True)

        self.login_frame = self.tabv.tab('Login')
        self.register_frame = self.tabv.tab('Register')

        self.login_element_frame = CTkFrame(master=self.login_frame, fg_color='transparent')
        self.login_element_frame.place(relx=0.5, rely=0.45, anchor='center')

        self.register_element_frame = CTkFrame(master=self.register_frame, fg_color='transparent')
        self.register_element_frame.place(relx=0.5, rely=0.45, anchor='center')

        # List of Login GUI elements
        elements_login = [
            CTkLabel(master=self.login_element_frame, text="Login Page", font=('montserrat', 26, 'bold')),
            CTkLabel(master=self.login_element_frame, text='USERNAME', font=('montserrat', 20)),
            CTkLabel(master=self.login_element_frame, text='PASSWORD', font=('montserrat', 20)),
            CTkEntry(master=self.login_element_frame, placeholder_text='username', width=180, height=38, 
                    font=('montserrat', 15, 'bold'), corner_radius=10),
            CTkEntry(master=self.login_element_frame, placeholder_text='password', show="*", width=180, height=38,
                    font=('montserrat', 15, 'bold'), corner_radius=10),
            CTkCheckBox(master=self.login_element_frame, text='I agree to Terms and Conditions',
                       font=('montserrat', 15), corner_radius=20, onvalue='on', offvalue='off'),
            CTkButton(master=self.login_element_frame, text="Login", font=('montserrat', 20, 'bold'),
                     corner_radius=10, command=self.handle_login)
        ]

        # Positioning settings
        grid_config = [
            (0, 0, {'columnspan': 2, 'pady': (20,0)}),
            (1, 0, {'padx': (0,40), 'pady': (40,15)}),
            (2, 0, {'padx': (0,40), 'pady': (0,15)}),
            (1, 1, {'padx': (40,0), 'pady': (40,15)}),
            (2, 1, {'padx': (40,0), 'pady': (0,15)}),
            (3, 0, {'pady': (0,15), 'columnspan': 2}),
            (4, 0, {'columnspan': 2, 'sticky': 'ew'})
        ]

        # Placing elements in the grid
        for element, (row, col, kwargs) in zip(elements_login, grid_config):
            element.grid(row=row, column=col, **kwargs)

        # Assignment to class variables
        (self.login_text, self.username_lbl, self.password_lbl, 
         self.username_entry, self.login_password_entry, self.checkbox, 
         self.login_btn) = elements_login


        # List of Register GUI elements
        elements_register = [
            CTkLabel(master=self.register_element_frame, text="Register Page", font=('montserrat', 26, 'bold')),
            CTkLabel(master=self.register_element_frame, text='NAME', font=('montserrat', 20)),
            CTkLabel(master=self.register_element_frame, text='PASSWORD', font=('montserrat', 20)),
            CTkLabel(master=self.register_element_frame, text='NATIONAL CODE', font=('montserrat', 20)),

            CTkEntry(master=self.register_element_frame, placeholder_text='first name', width=105, height=38, 
                    font=('montserrat', 15, 'bold'), corner_radius=10),
            CTkEntry(master=self.register_element_frame, placeholder_text='last name', width=105, height=38,
                    font=('montserrat', 15, 'bold'), corner_radius=10),
            CTkEntry(master=self.register_element_frame, placeholder_text='national code', width=220, height=38,
                    font=('montserrat', 15, 'bold'), corner_radius=10),
            CTkEntry(master=self.register_element_frame, placeholder_text='password', show="*", width=220, height=38,
                    font=('montserrat', 15, 'bold'), corner_radius=10),
            CTkLabel(master=self.register_element_frame, text='Lesson', 
                    font=('montserrat', 20)),
            CTkOptionMenu(master=self.register_element_frame, 
                        values=['Math', 'Geo', 'Biology']),
            CTkCheckBox(master=self.register_element_frame, text='I agree to Terms and Conditions',
                       font=('montserrat', 15), corner_radius=20, onvalue='on', offvalue='off'),
            CTkButton(master=self.register_element_frame, text="Register", font=('montserrat', 20, 'bold'),
                     corner_radius=10, command=self.handle_register)
        ]

        # Positioning settings
        grid_config = [
            (0, 0, {'columnspan': 3, 'pady': (20,0)}),                 # register page
            (1, 0, {'padx': (0,40), 'pady': (20,0), 'sticky': 'w'}), # name
            (2, 0, {'padx': (0,40), 'pady': (10,0), 'sticky': 'w'}),  # password
            (3, 0, {'padx': (0,40), 'pady': (10,0), 'sticky': 'w'}),  # national code
            (1, 1, {'pady': (20,0), 'sticky': 'w'}),                 # first name
            (1, 2, {'pady': (20,0), 'sticky': 'e'}),                 # last name
            (3, 1, {'pady': (10,0), 'columnspan': 2}), # national code
            (2, 1, {'pady': (10,0), 'columnspan': 2}), # password
            (4, 0, {'pady': (10,0), 'padx': (0,40), 'sticky': 'w'}),
            (4, 1, {'pady': (10,0), 'columnspan': 2, 'sticky': 'wnse'}),
            (5, 0, {'pady': (10,0), 'columnspan': 3}),                  # terms and conditions
            (6, 0, {'pady': (10,0), 'columnspan': 3, 'sticky': 'ew'})  # register button
        ]

        # Placing elements in the grid
        for element, (row, col, kwargs) in zip(elements_register, grid_config):
            element.grid(row=row, column=col, **kwargs)

        # Assignment to class variables
        (self.register_text, self.name_text, self.password_register_lbl, self.natoinal_code_register_lbl,
        self.first_name_entry, self.last_name_entry, self.national_code_entry, self.password_entry,self.lesson_text,
        self.lesson_optionbox, self.checkbox_register, self.register_btn) = elements_register

    def handle_register(self):
        self.toggle_register_button(state='disabled')
        
        def register_thread_handler():
            result = register_btn_func(first_name=self.first_name_entry.get().strip(),
                              last_name=self.last_name_entry.get().strip(),
                              national_code=self.national_code_entry.get().strip(),
                              password=self.password_entry.get().strip(),
                              lesson=self.lesson_optionbox.get().strip())
            if result == 'exist':
                messagebox.showerror('Register Error', f'Your National code "{self.national_code_entry.get().strip()}" is already exists')
            elif result == 'registered':
                messagebox.showinfo('Successful registration ', f'You have successfully registered !')
            elif result == 'Fill in all the fields':
                messagebox.showerror('Register Error', f'Fill in all the fields !')
            elif result == 'error':
                messagebox.showerror('Register Error', 'An Error occured !')
            self.toggle_register_button()
        
        if self.checkbox_register.get() == 'on':
            Thread(target=register_thread_handler).start()
        
        else:
            self.show_error("Agreement Error", "You must agree to the terms and conditions!")
            self.toggle_register_button()
                

    def handle_login(self):
        """Manage login process with threading"""
        self.toggle_login_button(state='disabled')
        
        try:
            Thread(target=self.login_workflow, daemon=True).start()
        except Exception as e:
            self.show_error("Thread Error", f"Error starting thread: {str(e)}")
            self.toggle_login_button()

    def login_workflow(self):
        """Main login process flow"""
        try:
            # Checking the internet connection
            if not self.check_internet():
                return

            # Initial validation
            if not self.validate_inputs():
                return

            # Authentication
            auth_result = self.authenticate_user()
            self.after(0, self.process_auth_result, auth_result)

        except Exception as e:
            self.show_error("Login Error", str(e))
            self.toggle_login_button()

    def validate_inputs(self):
        """Validate user inputs"""
        username = self.username_entry.get().strip()
        password = self.login_password_entry.get().strip()
        
        if not all([username, password]):
            self.show_error("Input Error", "Username and password cannot be empty!")
            self.toggle_login_button()
            return False
        
        if self.checkbox.get() != 'on':
            self.show_error("Agreement Error", "You must agree to the terms and conditions!")
            self.toggle_login_button()
            return False
        
        return True

    def check_internet(self):
        """Check internet connection"""
        try:
            get('https://google.com', timeout=5)
            return True
        except exceptions.ConnectionError:
            self.show_error("Connection Error", "No internet connection!")
            self.toggle_login_button()
            return False

    def authenticate_user(self):
        """Authenticate user credentials"""
        try:
            return check_auth(
                self.username_entry.get().strip(),
                self.login_password_entry.get().strip(),
                'teacher'
            )
        except Exception as e:
            self.show_error("Authentication Error", str(e))
            return (False, None)

    def process_auth_result(self, result):
        """Process authentication result"""
        success, user_data = result
        
        if success:
            self.destroy()
            self.handle_post_login(user_data)
        else:
            self.show_error("Login Failed", "Invalid username or password!")
            self.toggle_login_button()

    def handle_post_login(self, user_data):
        """Handle post-login operations"""
        try:
            select_class_page_func(user_data)

        except Exception as e:
            self.show_error("File Error", f"{str(e)}")
            sys.exit(1)

    def toggle_login_button(self, state='normal'):
        """Toggle login button state"""
        self.login_btn.configure(state=state, text="Login" if state == 'normal' else "Processing...")

    def toggle_register_button(self, state='normal'):
        """Toggle Register button state"""
        self.register_btn.configure(state=state, text="Register" if state == 'normal' else "Processing...")

    
    def show_error(self, title, message):
        """Show error message dialog"""
        self.after(0, lambda: messagebox.showerror(title, message))

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    app = TeacherSideAppLoginPage()
    app.run()