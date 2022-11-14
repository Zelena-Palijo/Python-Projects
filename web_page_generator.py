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
        self.default_btn.grid(row=3, column=0, padx=(200,0), pady=(0,15))
        
        #Label for custom entry
        self.label_entry = Label(text = "Enter custom text or click the Default HTML page button")
        self.label_entry.grid(row=0, column=0, columnspan=3, padx=(0,0), pady=(10,10))
        #Creates entry for custom text
        self.custom_entry = Entry(width = 75, bg="black")
        #Positions entry in GUI
        self.custom_entry.grid(row=1, column=0, columnspan=3, padx=(0,0), pady=(10,10))
        

        #Creates button for submitting custom text
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=3, column=1, padx=(10,10),pady=(0,15))

      
        
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


    def customHTML(self): #function for custom HTML
        htmlText = self.custom_entry.get()
        print(htmlText)
        htmlFile = open("custom_index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        filepath = "file:/Users/zelenakpalijo/Documents/GitHub/Python-Projects/" + "custom_index.html"
        #need edit for opening in MacOS, need file path of index.html
        webbrowser.open_new_tab(filepath)
        print(htmlFile.read())

        #if working with windows, no need to include file path, instead just use
        #webbrowser.open_new_tab("custom_index.html")



           
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
