from __future__ import unicode_literals
from os import link
import youtube_dl
import tkinter as tk

window = tk.Tk() 
window.geometry("800x500")
window.title("Not Downloader")

window.configure(background="red")

window.grid_columnconfigure(0, weight=1) 


text = tk.Label(window, text="Welcome!", font=("Helvetica",15)) 
text.grid(row=0, column=0,  sticky="N", padx=20, pady=10)  
text2 = tk.Label(window, text="Please paste the youtube link", font=("Helvetica",8))    
text2.grid(row=2, column=0,  sticky="N", padx=20, pady=10)  


link = tk.StringVar
text_input= tk.Entry(textvariable=link)
text_input.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download():
    link = text_input.get() 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([link])

first_button = tk.Button(text="Download", command=download) 

first_button.grid(row=4, column=0, sticky="WE", padx=50, pady=50) 

if __name__ == "__main__":
    window.mainloop()
