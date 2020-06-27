from bs4 import BeautifulSoup
import urllib.request
import requests
import time
from tkinter import *

url = "https://www.reddit.com/r/Showerthoughts/top/?sort=top&t=day"

response = requests.get(url, headers = {'User-agent': 'db'})

soup = BeautifulSoup(response.text, "html.parser")

result = soup.findAll("h3", class_="_eYtD2XCVieq6emjKBH3m")

thoughtArray = []
index = 0

for a in result:
    thoughtArray.append(a.text)

def main():
    global root
    global quote
    global index
    
    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.config(background='black')
    root.title('Shower Thoughts')
    root.geometry('500x100')
    root.bind('q', lambda event:root.destroy())
    
    quote = Label(root, text='n', wraplength=500, fg='white', bg='black', font='Helvetica 10 bold')
    quote.place(anchor=CENTER, relx=0.5, rely=0.7)

    title = Label(root, text='Shower Thoughts', fg='yellow', bg='black', font='Helvetica 10 bold')
    title.place(anchor=CENTER, relx=0.5, rely=0.25)

    #stop = Label(root, text='Press Q to quit', fg='yellow', bg='black', font='Helvetica 10 bold')
    #stop.place(anchor=CENTER, relx=0.5, rely=0.25)
    b = Button(root, text='quit', command = exit)
    b.pack(anchor=NE)
    root.after(1000, UpdateValue, index)
    

    root.mainloop()


def UpdateValue(index):
    quote['text'] = thoughtArray[index]
    quote['wraplength'] = root.winfo_width()
    #print(root.winfo_width())
    if index < len(thoughtArray)-1:
        index+=1
    else:
        index=0
    root.after(15000, UpdateValue, index)
    

if __name__=='__main__':
    main()
