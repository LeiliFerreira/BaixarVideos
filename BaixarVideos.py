import pytube
from tkinter import*
from tkinter import messagebox

janela = Tk()
icone = PhotoImage(file='icone.png')
janela.iconphoto(False, icone)
janela.title("Baixar Vídeos do YouTube")
janela.geometry('474x265')
#janela.configure(background="FBF7BB")
janela.minsize(width=474, height=265)
janela.maxsize(width=474, height=265)

def download_video():
    url = input_url.get()
    resolution = StringVar()
    if(caixa_1 == True):
        resolution = "360"
    elif(caixa_2 == True):
        resolution = "720"

    if (url == ""):
        msg = "INSIRA A URL!"
        messagebox.showinfo('Aviso!', msg)
    else:
        itag = choose_resolution(resolution)
        video = pytube.YouTube(url)
        stream = video.streams.get_by_itag(itag)
        stream.download()
        return stream.default_filename

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    else:
        itag = 18
    return itag

label_url = Label(janela, text=" Insira a URL: ", font=("arial", 10, "bold"))
label_url.place(relx=0.07, rely=0.10)

input_url = Entry(janela, width=43)
input_url.place(relx=0.42, rely=0.10)

label_resolucao = Label(janela, text="   Escolha a resolução:", font=("arial", 10, "bold"))
label_resolucao.place(relx=0.00, rely=0.20)

valor_check = StringVar()
caixa_1 = Radiobutton(janela, variable=valor_check, value=1, text="360p", font=("arial", 10, "bold"))
caixa_1.place(relx=0.41, rely=0.20)

caixa_2 = Radiobutton(janela, variable=valor_check, value=2, text="720p", font=("arial", 10, "bold"))
caixa_2.place(relx=0.55, rely=0.20)
caixa_2.select()

download = Button(janela, text='DOWNLOAD', bg= '#054f77', fg='#ffffff', font=('arial', 8, "bold"), command=download_video)
download.place(relx=0.41, rely=0.50, relheight=0.13)

janela.mainloop()