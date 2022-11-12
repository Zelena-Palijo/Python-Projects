import tkinter as tk
from tkinter import *
import tkinter.filedialog
import webbrowser
import os

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #Creates button for default HTML page
        self.default_btn = Button(self.master, text="Default HTML Page", width = 30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #Creates button for submitting custom text
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2)
        self.custom_btn.grid(row=2, column=2, padx=(10,40),pady=(0,15))

        #Creates 

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html","w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        filepath = "file:/Users/zelenakpalijo/Documents/GitHub/Python-Projects/" + "index.html"
        #need edit for opening in MacOS, need file path of index.html
        webbrowser.open_new_tab(filepath)

        #if working with windows, no need to include file path, instead just use
        #webbrowser.open_new_tab("index.html")
        


           
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
