import tkinter
import customtkinter
from pytube import YouTube


def Startdownload():
    try:
        ytLink = link.get()
        print(f"Attempting to download video from: {ytLink}")
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        print("Downloading video...")
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!", text_color="green")

    except Exception as e:
        finishLabel.configure(text=f"An error occurred: {e}", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a YouTube Link", font=("Arial", 18))
title.pack(padx=20, pady=20)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(
    app, width=400, height=40, textvariable=url_var, font=("Arial", 14)
)
link.pack(padx=20, pady=10)

finishLabel = customtkinter.CTkLabel(app, text="", font=("Arial", 14))
finishLabel.pack(pady=10)

pPercentage = customtkinter.CTkLabel(app, text="0%", font=("Arial", 14))
pPercentage.pack(pady=10)

progressBar = customtkinter.CTkProgressBar(app, width=500, height=20)
progressBar.set(0)
progressBar.pack(padx=20, pady=20)

download = customtkinter.CTkButton(
    app,
    text="Download",
    command=Startdownload,
    width=200,
    height=40,
    font=("Arial", 14),
)
download.pack(pady=20)

app.mainloop()
