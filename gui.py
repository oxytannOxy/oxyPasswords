from customtkinter import *
from tkinter import messagebox
from PIL import Image
import json
from worker import Worker

class Gui:

    def __init__(self, objectofworker: Worker):
        self.worker = objectofworker

        # Setup
        set_appearance_mode("System")  # Modes: system (default), light, dark
        set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.screen = CTk()
        self.screen.config(width=700, height=610,)
        self.screen.resizable(0, 0)
        self.screen.title("OxyPasswords")
        self.screen.iconbitmap("img/ico2.ico")

        self.screen.rowconfigure(1, weight=1)
        self.screen.rowconfigure(0, weight=1)
        self.screen.columnconfigure(0, weight=1)
        self.screen.columnconfigure(1, weight=1)

        # Frames

        # scrollbar frame
        self.frame1 = CTkFrame(master=self.screen,
                               width=150,
                               height=610,
                               border_color="black",)

        self.frame1.grid(column=0, row=0, sticky="NSEW")

        # home frame
        self.frame2 = CTkFrame(master=self.screen,
                               height=610,
                               width=550,
                               border_color="black",
                               border_width=5,)

        self.frame2.grid(column=1, row=0, sticky="NSEW",)

        # setting frame
        self.frame3 = CTkFrame(master=self.screen,
                               height=610,
                               width=550,
                               border_color="black",
                               border_width=5,)
        self.frame3.grid(column=1, row=0, sticky="NSEW",)

        # page frame
        self.frame4 = CTkFrame(master=self.screen,
                               height=610,
                               width=550,
                               border_color="black",
                               border_width=5,)
        self.frame4.grid(column=1, row=0, sticky="NSEW",)

        self.scrollerframe = CTkScrollableFrame(master=self.frame1, width=150, height=600)
        self.scrollerframe.grid()

        for frame in [self.frame2, self.frame3, self.frame4]:
            frame.grid_propagate(False)

        # creating.......
        self.set_scrollbar()
        self.homef()

        self.screen.mainloop()

    def homef(self,):

        def clear():
            website.delete(0, END)
            gmail.delete(0, END)
            password.delete(0, END)

        def save_pass():
            w = website.get()
            g = gmail.get()
            p = password.get()
            if w == "" or g == "" or p == "":
                messagebox.showinfo(title="Empty Error", message="Do not left Entries empty..")
            else:
                dic = {
                    w: {
                        "gmail": g,
                        "password": p
                    }
                }
                self.worker.save_password(pass_dict=dic)
                self.set_scrollbar()


        # hiding auther frames
        self.frame2.grid()
        self.frame3.grid_remove()
        self.frame4.grid_remove()

        def set_gen_pass():
            passw = self.worker.password_gen()
            password.delete(0, END)
            password.insert(0, passw)

        # logo
        logo = CTkImage(
            light_image=Image.open("img/ico2.png"),
            dark_image=Image.open("img/ico2.png"),
            size=(250, 250))

        logolabal = CTkLabel(master=self.frame2,
                             text="",
                             image=logo,

                             )
        logolabal.grid(column=1, row=1, padx=27, pady=(30, 40), )

        # inputs
        website = CTkEntry(master=self.frame2,
                           width=350)
        website.grid(column=1, row=2, pady=(0, 40))

        gmail = CTkEntry(master=self.frame2,
                         width=350)
        gmail.grid(column=1, row=3, pady=(0, 40))
        mail = self.worker.read_passwords_for_scrollbar()
        try:
            gmail.insert(0, string=mail[-1][1])
        except IndexError:
            pass

        password = CTkEntry(master=self.frame2,
                            width=350)
        password.grid(column=1, row=4, pady=(0, 40))

        # labels
        websiteL = CTkLabel(master=self.frame2, text="Website: ")
        websiteL.grid(column=0, row=2, sticky="N", padx=(20, 0))
        emailL = CTkLabel(master=self.frame2, text="Email: ")
        emailL.grid(column=0, row=3, sticky="N", padx=(20, 0))
        passwordL = CTkLabel(master=self.frame2, text="Password: ")
        passwordL.grid(column=0, row=4, sticky="N", padx=(20, 0))

        # buttons
        genpass = CTkButton(master=self.frame2,
                            text="Genpass",
                            corner_radius=5,
                            width=82,
                            height=30,
                            fg_color="#F0F0F0",
                            text_color="black",
                            hover_color="#808080",
                            command=set_gen_pass)
        genpass.grid(row=0, column=0, pady=(20, 0), padx=(20, 0))

        clear = CTkButton(master=self.frame2, text="Clear",
                          corner_radius=5,
                          width=35, height=30,
                          fg_color="#F0F0F0",
                          text_color="black",
                          hover_color="#808080",
                          command=clear)
        clear.grid(column=1, row=5, sticky="E", pady=(0, 20), padx=(20, 0))

        save = CTkButton(master=self.frame2,
                         text="Save",
                         corner_radius=5,
                         width=35, height=30,
                         fg_color="#F0F0F0",
                         text_color="black",
                         hover_color="#808080",
                         command=save_pass)
        save.grid(column=2, row=5, pady=(0, 20), sticky="E", padx=20)

        settingsI = CTkImage(
            light_image=Image.open("img/hi.png"),
            dark_image=Image.open("img/hi.png"),
            size=(25, 25))

        settings = CTkButton(master=self.frame2,
                             image=settingsI,
                             text="", width=20,
                             fg_color="#F0F0F0",
                             command=self.settingsf,
                             hover_color="#808080")

        settings.grid(column=1, row=0, sticky="E", pady=(20, 0), padx=(20, 0))

        homeI = CTkImage(
            light_image=Image.open("img/pp.png"),
            dark_image=Image.open("img/pp.png"),
            size=(25, 25))

        home = CTkButton(master=self.frame2, image=homeI, text="", width=20, fg_color="#F0F0F0", hover_color="#808080")
        home.grid(column=2, row=0, pady=(20, 0), sticky="E", padx=20)

    def settingsf(self):

        def save_settings():
            si = sinnature.get()
            n = numbers.get()
            sy = symbols.get()

            if si == "" or n == "" or sy == "":
                messagebox.showinfo(title="Empty Error", message="Do not left Entries empty..")
            else:
                dic = {
                    "settings": {
                        "signature": si,
                        "numbers": n,
                        "symbols": sy
                    }
                }
                self.worker.save_settings(set_dict=dic)

        def update_total(event=None):
            try:
                total.configure(text=f"Total characters: {len(sinnature.get()) + int(numbers.get()) + int(symbols.get())}",)

                total.grid(column=1, row=5, pady=(0, 20), padx=20, columnspan=2)
            except ValueError:
                pass

        # hiding auther frames
        self.frame3.grid()
        self.frame2.grid_remove()
        self.frame4.grid_remove()


        logo = CTkImage(
            light_image=Image.open("img/set.png"),
            dark_image=Image.open("img/set.png"),
            size=(250, 250))

        logolabal = CTkLabel(master=self.frame3,
                             text="",
                             image=logo,

                             )
        logolabal.grid(column=1, row=1, padx=27, pady=(30, 40), )

        # inputs

        with open("data/settings.json", "r") as data:
            d = json.load(data)
            sig = d["settings"]["signature"]
            sym = d["settings"]["symbols"]
            num = d["settings"]["numbers"]

        sinnature = CTkEntry(master=self.frame3,
                             width=350)
        sinnature.grid(column=1, row=2, pady=(0, 40))

        numbers = CTkEntry(master=self.frame3,
                           width=350)
        numbers.grid(column=1, row=3, pady=(0, 40))

        symbols = CTkEntry(master=self.frame3,
                           width=350)
        symbols.grid(column=1, row=4, pady=(0, 40))

        symbols.insert(0, sym)
        sinnature.insert(0, sig)
        numbers.insert(0, num)

        symbols.bind("<KeyRelease>", update_total)
        numbers.bind("<KeyRelease>", update_total)
        sinnature.bind("<KeyRelease>", update_total)

        # labels
        total = CTkLabel(master=self.frame3,
                         text=f"0",
                         font=CTkFont(weight="bold", family="Helvetica", size=18))
        total.grid(column=1, row=5, pady=(0, 20), padx=20, columnspan=2)

        ptitle = CTkLabel(master=self.frame3,
                          text="SETTINGS",
                          corner_radius=5,
                          width=35,
                          height=30,
                          fg_color="#F0F0F0",
                          text_color="Black",
                          font=CTkFont(weight="bold", family="Terminal", size=18))
        ptitle.grid(row=0, column=0, pady=(20, 0),)

        sinnatureL = CTkLabel(master=self.frame3, text="Signature: ")
        sinnatureL.grid(column=0, row=2, sticky="N", padx=(20, 0))
        numbersL = CTkLabel(master=self.frame3, text="Numbers(int): ")
        numbersL.grid(column=0, row=3, sticky="N", padx=(20, 0))
        symbolsL = CTkLabel(master=self.frame3, text="Symbols(int): ")
        symbolsL.grid(column=0, row=4, sticky="N", padx=(20, 0))

        # buttons

        save = CTkButton(master=self.frame3,
                         text="Save",
                         corner_radius=5,
                         width=35, height=30,
                         fg_color="#F0F0F0",
                         text_color="black",
                         hover_color="#808080",
                         command=save_settings)
        save.grid(column=2, row=5, pady=(0, 20), sticky="E", padx=20)

        settingsI = CTkImage(
            light_image=Image.open("img/hi.png"),
            dark_image=Image.open("img/hi.png"),
            size=(25, 25))

        settings = CTkButton(master=self.frame3, image=settingsI, text="", width=20, fg_color="#F0F0F0", hover_color="#808080" )

        settings.grid(column=1, row=0, sticky="E", pady=(20, 0), padx=(20, 0))

        homeI = CTkImage(
            light_image=Image.open("img/pp.png"),
            dark_image=Image.open("img/pp.png"),
            size=(25, 25))

        home = CTkButton(master=self.frame3,
                         image=homeI, text="",
                         width=20,
                         fg_color="#F0F0F0",
                         command=self.homef,
                         hover_color="#808080")
        home.grid(column=2, row=0, pady=(20, 0), sticky="E", padx=20)
        update_total()

    def passf(self, pass_data: tuple):

        def delete():
            yesno = messagebox.askyesno(title="Deleting", message=f"Do you want to delete {pass_data[0]}'s password")
            if yesno:
                key = pass_data[0]
                self.worker.delete(key)
                self.set_scrollbar()
                self.homef()
            elif not yesno:
                pass

        def copying():
            self.screen.clipboard_clear()
            self.screen.clipboard_append(pass_data[2])

        # hiding auther frames
        self.frame4.grid()
        self.frame3.grid_remove()
        self.frame2.grid_remove()

        website_name = pass_data[0]
        email_name = pass_data[1]
        password_name = pass_data[2]

        # main labals
        website = CTkLabel(master=self.frame4,
                           width=350,
                           text=website_name,
                           font=CTkFont(family="Terminal", size=18,))
        website.grid(column=1, row=1, pady=(0, 40), sticky="W")

        gmail = CTkLabel(master=self.frame4,
                         width=350,
                         text=email_name,
                         font=CTkFont(family="Terminal", size=18,))
        gmail.grid(column=1, row=2, pady=(0, 40), sticky="W")

        password = CTkLabel(master=self.frame4,
                            width=350,
                            text=password_name,
                            font=CTkFont(family="Terminal", size=18,))
        password.grid(column=1, row=3, pady=(0, 40), sticky="W")

        # labels
        websiteL = CTkLabel(master=self.frame4,
                            text="Website: ",
                            font=CTkFont(weight="bold", family="Helvetica", size=18))
        websiteL.grid(column=0, row=1, sticky="NE", padx=(20, 0))

        emailL = CTkLabel(master=self.frame4,
                          text="Email: ",
                          font=CTkFont(weight="bold", family="Helvetica", size=18))
        emailL.grid(column=0, row=2, sticky="NE", padx=(20, 0))

        passwordL = CTkLabel(master=self.frame4,
                             text="Password: ",
                             font=CTkFont(weight="bold", family="Helvetica", size=18))
        passwordL.grid(column=0, row=3, sticky="NE", padx=(20, 0))

        # buttons

        copy = CTkButton(master=self.frame4, text="Copy",
                         corner_radius=5,
                         width=35, height=30,
                         fg_color="#F0F0F0",
                         text_color="black",
                         hover_color="#808080",
                         command=copying)
        copy.grid(column=1, row=5, sticky="E", pady=(0, 20), padx=(20, 0))

        delete = CTkButton(master=self.frame4,
                           text="Delete",
                           corner_radius=5,
                           width=35, height=30,
                           fg_color="#F0F0F0",
                           text_color="black",
                           hover_color="#808080",
                           command=delete)
        delete.grid(column=2, row=5, pady=(0, 20), sticky="E", padx=20)

        settingsI = CTkImage(
            light_image=Image.open("img/hi.png"),
            dark_image=Image.open("img/hi.png"),
            size=(25, 25))

        settings = CTkButton(master=self.frame4,
                             image=settingsI,
                             text="", width=20,
                             fg_color="#F0F0F0",
                             command=self.settingsf,
                             hover_color="#808080")

        settings.grid(column=1, row=0, sticky="E", pady=(20, 30), padx=(20, 0))

        homeI = CTkImage(
            light_image=Image.open("img/pp.png"),
            dark_image=Image.open("img/pp.png"),
            size=(25, 25))

        home = CTkButton(master=self.frame4,
                         image=homeI, text="",
                         width=20,
                         fg_color="#F0F0F0",
                         command=self.homef,
                         hover_color="#808080")
        home.grid(column=2, row=0, pady=(20, 30), sticky="E", padx=20)

    def set_scrollbar(self):
        self.destroy_scrollbar_items()

        pass_lis = self.worker.read_passwords_for_scrollbar()

        # scroller bar
        def add_frames():
            frames_list = []
            for f in pass_lis:
                passwords = CTkButton(master=self.scrollerframe,
                                      fg_color="#F0F0F0",
                                      text_color="black",
                                      hover_color="#808080",
                                      text=f"{f[0].title()}\n{f[1].split("@")[0]}",
                                      command=lambda data=f: self.passf(data),
                                      )
                passwords.pack(pady=(10, 0))
                frames_list.append(passwords)
        try:
            add_frames()
        except Exception:
            pass

    def destroy_scrollbar_items(self):
        for widget in self.scrollerframe.winfo_children():
            widget.destroy()



