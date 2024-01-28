''' 
    If you are bored you can use this program to found someting to do.
    API: https://www.boredapi.com/api/activity
'''
from tkinter import Tk, Label, Button, messagebox
import requests

class DoSometing():
    ''' This class include the interface of the program and the API request handle.'''
    def __init__(self):
        ''' Initailaize the tkinter instance.'''
        self.win = Tk()

    def do_request(self):
        '''Do the request when the button is pressed and print it on a message box.'''
        response = requests.get('https://www.boredapi.com/api/activity', timeout=30)
        decoded_response = response.json()
        pop_up_title = decoded_response['type']
        pop_up_message = decoded_response['activity']
        messagebox.showinfo(pop_up_title, pop_up_message)

    def interface(self):
        ''' This function defines the main interface of the program.'''
        self.win.title("Want to do something?")
        width = 300
        height = 60
        
        # The next lines are used to center the window.
        width_scr = self.win.winfo_screenwidth()
        height_scr = self.win.winfo_screenheight()
        x = int((width_scr/2) - (width/2))
        y = int((height_scr/2) - (height/2))
        self.win.geometry(f"{width}x{height}+{x}+{y}")
        
        # Window content.
        main_message = Label(self.win, text="Press to found someting to do!", font=("bold", 10))
        main_message.pack(pady=3)
        btn = Button(self.win, text="Search", command=self.do_request)
        btn.pack(pady=2)
        self.win.mainloop()

    def __call__(self):
        self.interface()

def main():
    '''Execute the class to do someting.'''
    bored = DoSometing()
    bored()

if __name__ == '__main__':
    main()
