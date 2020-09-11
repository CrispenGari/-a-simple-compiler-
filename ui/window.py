
try:
    from tkinter import *
    from tkinter import messagebox, scrolledtext
    import tkinter.ttk as ttk
    from PIL import ImageTk, Image
    import os, subprocess
    from functions.functions import Function as funct_
except ImportError as e:
    print(e)
class Main:
    def __init__(self):
        pass
    def main(self):
        root = Tk()
        root.title("Programming Editor (Python)")
        root.resizable(False, False)
        window_width = 890
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height/2 -window_height/2)
        position_right = int(screen_width / 2 - window_width/2)
        root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        root.iconbitmap('./icons/main.ico')
        run_icon = ImageTk.PhotoImage(Image.open('./icons/run.png'))
        build_icon = ImageTk.PhotoImage(Image.open('./icons/build.png'))
        cmd_icon = ImageTk.PhotoImage(Image.open('./icons/cmd.png'))

        # useless Menues

        menubar = Menu(root)
        menu=menubar.add_cascade(label="File")
        menubar.add_cascade(label="Edit")
        menubar.add_cascade(label="Navigate")
        menubar.add_cascade(label="Code")
        menubar.add_cascade(label="Refactor")
        menubar.add_cascade(label="Run")
        menubar.add_cascade(label="Tools")
        menubar.add_cascade(label="VCS")
        menubar.add_cascade(label="Window")
        menubar.add_cascade(label="Help")
        def Key(event):
            if event.keycode ==13 or event.keysym =="Return" or event.char == "\r" :
                source_code = code_editor.get('0.0', END)
                lines = funct_.line_of_codes("", source_code,event.keysym )
                line_numbers['state'] = NORMAL
                line_numbers.delete('0.0', END)
                for i in range(1, lines+1):
                    line_numbers.insert(END, f'{i}\n')
                line_numbers['state'] = DISABLED
            elif event.keycode ==8 or event.keysym =="BackSpace" or event.char == "\x08":
                source_code = code_editor.get('0.0', END)
                lines = funct_.line_of_codes("", source_code, event.keysym)
                line_numbers['state'] = NORMAL
                line_numbers.delete('0.0', END)
                for i in range(1, lines + 1):
                    line_numbers.insert(END, f'{i}\n')
                line_numbers['state'] = DISABLED
            else:
                pass
        def run():
            source_code = code_editor.get('0.0', END)
            output_screen['state'] = NORMAL
            output_screen.delete('0.0', END)
            output_screen.insert(END, os.getcwd() + ">\n")
            raw_results = funct_.run_program("", source_code)
            results = str(raw_results).split('\n')
            for res in results:
                if str(exec(res, globals(), locals()))== "None" or str(exec(res)) is None or str(exec(res))  == None or not str(exec(res)) :
                   pass
                else:
                    output_screen.insert(END, str(exec(res)) + "\n")
            output_screen.insert(END,"\n")
            output_screen.insert(END, "Process finished with exit code 0. (output on the system console) \n ")
            output_screen['state'] = DISABLED
            return
        # Create  frames
        top_frame = Frame(root)
        Button(top_frame, text="compile",  font=("arial", 10, "bold"), width=90, relief=SOLID,bd=0,
               compound=LEFT, image=build_icon, command=run).grid(row=0, column=0, sticky=E, padx=2)
        Button(top_frame, text="run" ,font=("arial",10, "bold"), width=90,
               compound=LEFT, image=run_icon, relief=SOLID, bd=0, command=run).grid(row=0, column=1, sticky=E, padx=2)
        top_frame.grid(row=0,column=0, padx=3, pady=2)
        midle_frame = Frame(root)
        line_numbers = Text(midle_frame,  width=3, height=25, bg ="#0B1C1F", fg="green", font=("consolas",12 ),)
        line_numbers.insert(END, 1)
        line_numbers['state'] = DISABLED
        line_numbers.grid(row=0, column=0, sticky=E)
        code_editor= scrolledtext.ScrolledText(midle_frame, width=92, font=("consolas",12 ),
                                               height =25, bg ="#0B1C1F", fg="green", insertbackground="white")
        code_editor.grid(row=0, column=1)
        midle_frame.grid(row=1, column=0, sticky=W, padx=3, pady=2)
        Label(root, text="Output Console", font=("arial",10, "bold"), compound=LEFT, image=cmd_icon).grid(row=2, column=0, sticky=W)
        bottom_frame = Frame(root)
        output_screen=scrolledtext.ScrolledText(bottom_frame, width=95,
                                                font=("consolas",12 ),heigh=8, bg ="#0B1C1F", fg="green")
        output_screen.insert(END,os.getcwd()+">\n")
        output_screen['state'] = DISABLED
        output_screen.grid(row=0, column=0, sticky=W)
        bottom_frame.grid(row=3, column=0, padx=3, pady=2)
        code_editor.focus()
        # binding the enter key to listen to the change of lines
        code_editor.bind('<KeyPress>', Key)

        root.config(menu=menubar)
        root.mainloop(0)
