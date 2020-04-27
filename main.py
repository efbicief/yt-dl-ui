from tkinter import Tk, Entry, Label, Text, Button, StringVar, OptionMenu, _setit, font
import tkinter.font
from tkinter.filedialog import askdirectory
import import_locale
import get_os
import subprocess
import run_command
import threading


class App():

    def __init__(self):

        self.lang = import_locale.Locale().lang
        self.platform = get_os.get_platform()
        self.gui = Gui(self.lang, self.platform)


class Gui():

    def __init__(self, lang, platform):

        self.lang = lang

        master = Tk()
        master.wm_title(lang["wm_title"])
        master.geometry("1170x460")

        default_font = tkinter.font.nametofont("TkDefaultFont")
        default_font.config(size=15)
        master.option_add("*Font", default_font)

        self.urlent = Entry(width=75)
        self.fetchbtn = Button(text = lang["fetch_info"], width=24, command = self.fetch_info)

        self.dltype_ol = [ lang["audio_choice"], lang["video_choice"] ] #optionList
        self.dltype_cv = StringVar(master) #currentValue
        self.dltype_cv.set(lang["audio_choice"])
        self.dltype_cv.trace('w', self.dltype_change)
        self.dltype = OptionMenu(master, self.dltype_cv, *self.dltype_ol)

        self.dlformat_aol = ["m4a"] #audioOptionList TEMP
        self.dlformat_vol = ["mp4"] #videoOptionList TEMP
        self.dlformat_cv = StringVar(master) #currentValue TEMP
        self.dlformat_cv.set("m4a")
        self.dlformat = OptionMenu(master, self.dlformat_cv, *self.dlformat_aol)

        self.savelocbtn = Button(text = lang["save_loc_button"], command = self.choose_save_location)
        self.saveloclbl = Label(text = lang["default_save_loc_lbl"])
        self.gobtn = Button(text = lang["go_button"], command=self.start_download)

        self.dllist = Text(state="disabled", height=10)
        self.termout = Text(state="disabled", height=5)

        self.urlent.grid(column=0, row=0, columnspan = 3)
        self.fetchbtn.grid(column=3, row = 0)
        self.dltype.grid(column=0, row=1)
        self.dlformat.grid(column=1, row=1)
        self.dllist.grid(column=2, row=1, rowspan=2, columnspan=2)
        self.savelocbtn.grid(column=0, row=2)
        self.saveloclbl.grid(column=1, row=2)
        self.gobtn.grid(column=0, row=3, columnspan=2)
        self.termout.grid(column=2, row=3, columnspan=2)

        master.mainloop()
    
    def dltype_change(self, vartype, b, mode):
        if self.dltype_cv.get() == self.lang["audio_choice"]:
            self.dlformat_cv.set(self.dlformat_aol[0])
            self.dlformat['menu'].delete(0, 'end')
            for option in self.dlformat_aol:
                self.dlformat['menu'].add_command(label=option, command = _setit(self.dlformat_cv, option))
        else:
            self.dlformat_cv.set(self.dlformat_vol[0])
            self.dlformat['menu'].delete(0, 'end')
            for option in self.dlformat_vol:
                self.dlformat['menu'].add_command(label=option, command = _setit(self.dlformat_cv, option))
    
    def choose_save_location(self):
        self.savefolder = askdirectory()
        self.saveloclbl.config(text=self.savefolder)
    
    def fetch_info(self):
        #not win compatableas of yet, pls check and change
        link = self.urlent.get()
        run_command.run(["youtube-dl", "-e", link], "fetch_info.log", self.dllist)

    def start_download(self):
        #not win compatableas of yet, pls check and change
        dlformat = self.dlformat_cv.get()
        link = self.urlent.get()
        dlloc = self.savefolder + '/%(title)s.%(ext)s'
        command = ["youtube-dl", "-o", dlloc, "-f", dlformat, link]
        dlthread = threading.Thread(target=self.download_thread, args=(command, "download.log"))
        dlthread.start()

    def download_thread(self, command, log):
        run_command.run(command, log, self.termout)


if __name__ == "__main__":

    app = App()