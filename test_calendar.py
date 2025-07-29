from tkinter import Tk
from tkcalendar import Calendar

root = Tk()
cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(pady=20)
root.mainloop()
