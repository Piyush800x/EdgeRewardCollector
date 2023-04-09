import os
from tkinter import TclError
import base64
from secret import data
from tkinter import Tk, Label, StringVar, messagebox, IntVar, LEFT, RIGHT
from tkinter.ttk import Button, Entry, Checkbutton
import webbrowser
from time import sleep
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
from keys import verify_key, checkforupdate_list, local_list
from win32api import GetSystemMetrics
import psutil
import subprocess
from datetime import datetime


width, height = GetSystemMetrics(0), GetSystemMetrics(1)
checkforupdate_list()
keyword = local_list
l = len(keyword)
icon = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAMMOAADDDgAAAAAAAAAAAACwtrv/sbe9/7G3vf+xt73/s7m+/7e9w/++xMr/xMrQ/8TK0P/Bx83/wMbM/7/GzP/Ax83/wsnQ/8TL0f/DytD/wsnP/7/GzP+8w8n/vMLI/7zCyP+7wcf/uL7E/7O6v/+yuL3/r7a7/7C2vP+utLn/p62y/6Sprv+ip6z/pKmv/7K5vv+yuL7/s7m//7S6wP+0u8D/t73D/7/GzP/FzNL/xczS/8PK0P/ByM7/wsnP/8LJz//DytD/xczS/8XM0v/EytH/v8bM/77Fy/++xcv/vMPJ/7rBxv+4vsT/tbzB/7O5v/+wtrv/sLa7/660uv+pr7X/pauw/6Oprv+lqq//srm+/7O5v/+2vcL/uL/F/7i/xP+7wcf/vsXL/8XM0v/I0Nb/yM/V/8XM0v/FzNL/xczS/8XN0//HztT/yM/V/8bN0//Cyc//wMfN/8DHzf++xcv/u8LI/7i/xP+1vML/s7q//7K4vf+yub7/srm+/6+1uv+qsLX/qK6z/6essv+zub//tbzB/7i+xf+1ucH/sbS9/7Gzvf+4vMT/vcHK/8LGz//DyND/vsHK/77Byv+6vcf/xszT/8LHz/++wcv/vcHK/7u/x/+0tsD/s7W//7O1v/+ytL7/sLO8/6+yuv+wtLv/r7S7/6uttv+wtLz/q662/6yyuP+qsLb/qrC2/7W7wf+4vsT/t7zD/4p7kv+IeZH/kIOZ/5GEm/+Cbor/l4uh/4p6k/+LfJT/jn+X/41+lv+sqLf/oput/5+Wqf+ViJ7/j4GY/5WKn/+UiJ3/mY+j/4+BmP+RhZv/oJuq/5iSov+XkKH/iHqR/4NzjP+JfJL/r7S6/62zuP+rsbb/uL7E/7m/xf+4vcT/hXSO/4RyjP+Nfpb/jH2V/4BriP+elKj/koSc/5KEnP+Jd5L/jX2W/6yot/+imq3/oJeq/5SHnv+PgJj/pZ+w/6KbrP+norL/jX6W/5KGnP+emKn/jH+V/5CFmv+IepH/fmyG/4d4kP+yt73/sbe8/6qwtv+5wMb/vMLI/73Dyf+ys73/srW+/7Kyvf+4usT/v8LM/8XK0//Gy9T/w8XP/8LEzv+/wMv/y9DY/8XJ0v+/wcz/v8LM/8DDzf/DyND/wcbO/8LGzv+3uMP/uLrF/7S1wP+trbj/sLK8/6ustv+qrLX/rK63/7m/xf+0usD/rLO4/7vCx/+9xMr/vsXL/8HIzv/ByM7/xMzR/8jP1f/N1dv/0dje/9LZ4P/T2uD/1Nvi/9Pa4P/S2eD/0djf/9DY3v/Q2N7/ztbc/8zT2v/K0df/yM/V/8jP1f/Iz9X/xMvR/8DHzf+9xMn/usHG/7i+xP+2vcL/tr3C/7O5v/+utLr/vcPJ/77Fy//Cyc//xMvR/8XM0v/GzdT/ydDX/83U2v/P1tz/0dnf/9Pb4v/U2+L/09rh/9HZ3//R2N//0Nfe/8DCzf/N09r/zdTb/8rS2P/J0Nb/yM/V/8jP1f/FzNL/wcjO/7/Fy/+8wsj/uL/E/7e+w/+4v8T/tr3C/6+2u//Ax83/wcjO/8XM0v/HztT/x87V/8jP1f/K0df/ztXb/9DY3v/T2+H/1Nzi/9Tc4v/V3uP/09vh/9LZ4P/T2+H/s7G//8TI0f/Q2N7/ztbc/8vT2f/M09n/zNPZ/8fP1f/Ey9H/wcfN/77Fyv+7wcf/usHG/7i/xf+2vcL/sri9/8LJz//Ey9H/xs3T/8jQ1v/J0Nb/ytHY/8zT2f/Q193/0trg/9be5P/R19//vb3K/6mitP+Uhp7/h3WQ/56UqP+nn7H/mo6k/5KDm/+po7T/xsvT/83V2//L0tn/ydDX/8bN0//DytD/wMfN/73Dyf+8w8n/usDG/7a9wv+zur//xczS/8bN0//Iz9X/ytHX/8rS2P/M09n/zdTa/9DY3v/Jztb/qaK0/35nhv9gP2b/VjJb/1QvWf9TLVj/VTBa/1w5Yf9XMlz/Uy1Y/1o3X/9zWXr/p6Cy/8vS2P/K0df/ydDW/8bN0//Cyc//v8bM/7/Fy/+9w8n/usDG/7e+w//GzdT/yM/V/8nQ1v/L0tj/zNPZ/83U2v/O1dz/0dnf/7+/zP9+Z4b/VjFb/1QvWf9VMFr/VTBa/1UwWv9VMFr/VS9a/1UwWv9VMFr/VS9a/1MtWP9dO2L/pJ2v/8zU2f/J0Nb/x87U/8XM0v/DytD/wcjO/7/GzP+7wsj/uL7E/8fO1P/J0Nb/y9LY/8zT2v/O1dv/z9bc/9DX3v/S2eD/1Nzi/87U3P+OfJf/VjFb/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1QuWf9jRGn/rqq5/8nQ1v/Iz9X/x87U/8XM0v/Cyc//v8bM/7zDyf+5v8X/yM/V/8nR1//N1Nr/ztXb/8/W3f/Q197/0djf/9LZ4P/V3eP/x8rU/3JXef9UL1n/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VC9Z/35ohv+6ucb/zNPZ/8nQ1//J0Nb/yM/V/8TL0f/ByM7/vsXL/7vBx//J0Nf/y9LZ/87V2//P193/0Nje/9HY3//R2d//09vh/8zR2f+FcI3/VC9Z/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9ULlj/hHCM/8/V3P/O1dz/y9LZ/8vS2P/K0df/x87V/8bN0//Cyc//v8bM/8zT2f/O1dv/0Nfd/9HY3//S2eD/09rh/9Pa4f/U2+L/kYGa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9ZNV7/nJCm/87V2//M1Nr/zNPZ/8rS2P/J0Nb/xs3T/8LJz/+/xsz/y9PZ/87V2//P1t3/0djf/9Pa4f/U2+L/1d3j/8HBzf9lRmz/VC5Z/1UwWv9VMFr/VTBa/1UvWf9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1MtWP9xV3j/ys/X/8/W3f/N1Nv/y9PZ/8nR1//Iz9X/w8rQ/8HIzv/N1Nr/z9bc/9DY3v/S2eD/09vh/9Tc4//W3uT/lYef/1QuWf9VMFr/VTBa/1QvWf9YNF3/Xz5l/1UwWv9VMFr/VTBa/1UwWv9VMFr/VTBa/1UwWv9VMFr/VC9Z/2FAZ/+5uMb/0tng/87V3P/N1Nr/y9LY/8nQ1v/GzdP/w8rQ/87W3P/Q2N7/0trg/9Pb4f/U3OL/19/l/8PF0P9oSm//VC5Z/1QuWf9TLVj/WTVe/5B/mv9/aYf/Uy1Y/1UwWv9VMFr/VTBa/1UvWv9ZNl//VjFb/1UwWv9VMFr/Uy5Y/4d0kP/P1t3/z9bd/83V2//M09n/ydDW/8fO1P/GzdP/0Nje/9LZ4P/T2+H/1Nzi/9Xd4//M0dr/gmyK/1YyW/9bOGD/aEpv/3ddfv+qobX/193l/4t5lP9TLVj/VTBa/1UwWv9VMFr/WTVe/5yOpv99ZoX/Uy5Y/1MtWP9TLVf/WjZf/6egsv/R2N7/z9bc/83U2//L0tj/yM/W/8bN1P/R2N//0trg/9Tb4v/V3eP/1t7l/8bI0/+spbf/sKq8/7u4x//Mz9n/1dvj/9zk6v/d5uz/nY+n/1MuWP9VMFr/VTBa/1MuWP+CbIr/197l/83R2/+ajKT/jXuW/5SEnf+Gco//i3mU/8HDzv/Q2N7/ztbc/8zT2f/J0Nf/x87U/9La4P/U3OL/1d3j/9be5P/X3uX/2ODn/9vj6f/c5Or/3eXr/93l6//d5Ov/2+Pq/93l7P+4tMT/YD5l/1QvWf9VMFr/VTBa/6ykt//f6O7/3eXr/9zk6//b4un/2eLo/9be5P/Q197/z9Xd/9DY3v/P1t3/zdTa/8nQ1//Iz9X/09vh/9bd5P/X3uX/19/l/9ff5v/Y4Of/2uHo/9ri6f/c4+r/3OTr/9zk6//c5Or/3OTq/9vj6v+LeJT/Uy1Y/1QuWf9wU3b/zM7Z/97m7f/d5ez/3OTq/9ri6f/Y4Of/19/l/9Xc4//T2uH/0djf/8/W3f/N1Nv/ydHX/8fO1f/V3OP/1t7l/9jf5v/Y3+b/2eDn/9nh6P/a4un/2+Pq/9zk6//d5ev/3eXs/93k6//d5Ov/3+ft/6acsf9XMlz/Uy5Y/5yOpv/g6O7/3eXs/93l7P/c5Or/2+Pq/9ri6f/Y4Ob/1dzj/9La4P/Q197/z9bd/83U2v/L0tj/yM/V/9bd5P/Y3+b/2eHo/9nh6P/Z4ej/2uLp/9vj6v/c5Ov/3eXr/97l7P/e5ez/3uXs/93l7P/e5u3/09bg/3FVeP9oSW7/yMnV/97m7f/d5ez/3eTr/9zk6v/b4+r/2uLo/9jf5v/V3eP/09rh/9DY3v/Q197/ztXc/8zT2f/J0Nf/1t7l/9jg5//a4ej/2+Lp/9vi6f/b4+r/3OTr/93l6//d5ez/3uXs/97m7f/e5u3/3uXs/97l7P/f5+7/mImi/5yOpv/f5+7/3eXr/93k6//c5Ov/3OPq/9vj6f/a4uj/2eDn/9fe5f/U3OL/0tng/9HY3//P193/zNPZ/8rR1//X3+b/2eDn/9ri6f/b4+r/3OTq/9zk6v/d5Ov/3eXs/97l7P/e5u3/3+bt/9/m7f/e5u3/3ubt/9/o7v/FxdL/ycvX/9/n7v/d5ez/3eTr/9zk6//c5Or/2+Pq/9ri6f/a4uj/19/m/9Xd4//T2+H/0tng/9DY3v/N1Nr/ytHY/9ng5//Z4ej/2+Lp/9zj6v/d5ev/3eXs/97l7P/e5ez/3ubt/97m7f/f5+7/3+fu/97m7f/e5u3/3+bt/97l7f/e5ez/3ubt/97l7P/d5ev/3eTr/9zk6//c5Ov/2+Pq/9nh6P/X3+X/1d3j/9Pb4f/S2uD/0Nje/83V2//L0tj/2eHn/9ri6P/b4+r/3OTr/93l7P/e5ez/3uXs/97m7f/f5u3/3+fu/9/n7v/f5+7/3+fu/9/n7v/f5+7/3+fu/9/n7v/f5+3/3uXs/93l7P/d5ev/3OTq/9zk6v/b4+r/2uLo/9ff5v/V3eT/09vh/9La4P/Q2N7/ztXb/8zT2f/a4ej/2uLp/9zj6v/d5Ov/3uXs/97m7f/e5u3/3+fu/9/n7v/f5+7/4Ojv/+Do7//g6O//3+fu/9/n7v/f5+7/3+fu/9/n7v/e5u3/3uXs/93l6//c5Or/3OPq/9vj6v/b4+n/2ODn/9Xd5P/U2+L/0tng/9DY3v/O1tz/zdTb/9ri6P/b4un/3OTq/93l6//e5u3/3ubt/9/n7v/f5+7/4Ojv/+Do7//h6fD/4enw/+Do7//g6O//4Ojv/+Do7//f5+7/3+fu/9/n7f/e5uz/3eXr/93k6//c4+r/3OPq/9vj6f/Z4Of/1t7k/9Tb4v/S2eD/0Nje/8/W3P/N1Nv/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
icon_decoded = base64.b64decode(icon)

count = 0
global user_inp
global check_var


class Activation:

    def check_licence_status(self) -> bool:
        current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        check = data.find_one({"uuid": current_machine_id})
        try:
            if check.get("licence"):
                return True
        except Exception:
            return False

    def register(self):
        self.root = Tk()
        self.root.geometry("360x180")
        self.root.title("Reward Collector")
        self.root.protocol('WM_DELETE_WINDOW', lambda: [self.root.destroy(), exit(0)])
        self.root.resizable(False, False)
        self.user_input = StringVar()
        self.root.iconbitmap(rf"{icon_decoded}")

        label1: Label = Label(self.root, text="Enter key")
        label1.pack(pady=5)
        entry: Entry = Entry(self.root, textvariable=self.user_input, width=40)
        entry.pack(pady=5)

        btn1: Button = Button(self.root, text="Activate", command=self.activate)
        btn1.pack()

        btn2: Button = Button(self.root, text="Purchase", command=lambda:
        webbrowser.open("https://discord.gg/YFkwJkU2px"))
        btn2.pack()
        messagebox.showinfo("Reward Collector", "Licence format must be XXXX-XXXX-XXXX-XXXX-XXXX")

        self.root.mainloop()

    def activate(self):
        lisense: str = self.user_input.get()
        if verify_key(lisense):
            dic = {
                "uuid": subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip(),
                "licence": lisense,
                "date": f"{datetime.today()}"
            }
            data.insert_one(dic)
            messagebox.showinfo("Reward Collector", "Licence has successfully activated.\nRestarting application.")
            self.root.destroy()
            main()
        elif not verify_key(lisense):
            messagebox.showerror("Reward Collector", "Licence is not valid or registered to another device\n"
                                                     "Try to contact your seller\nCheck licence format")


# NEW CODE
def window_start():
    app = Application().start("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    sleep(2)
    click(button="left", coords=(int(width - (width*51.6/100)), int(height - (height*85.3/100))))  # Search bar
    sleep(1)

    global user_inp
    global check_var
    top = Tk()
    top.title("Reward Collector")
    top.geometry("270x160")
    top.protocol('WM_DELETE_WINDOW', lambda: [top.destroy(), exit_browser(), exit(0)])
    top.resizable(False, False)
    user_inp = IntVar()
    check_var = IntVar()
    top.iconbitmap(rf"{icon_decoded}")

    label2: Label = Label(top, text="How many search do you want? ")
    label2.pack(pady=10)
    entry1: Entry = Entry(top, textvariable=user_inp)
    entry1.pack(pady=10, padx=10)
    checkbutton: Checkbutton = Checkbutton(top, text="Remove this search history", offvalue=0, onvalue=1, width=20,
                                           variable=check_var)
    checkbutton.pack()
    btn3: Button = Button(top, text="Yes", command=lambda: [top.destroy(), start()])
    btn3.pack(side=LEFT, padx=25)
    btn4: Button = Button(top, text="No", command=lambda: [top.destroy(), exit_browser(), exit(0)])
    btn4.pack(side=RIGHT, padx=25)
    top.attributes('-topmost', True)

    top.mainloop()


def search():
    global count
    if count == l:
        exit(0)
    else:
        send_keys(keyword[count])
        sleep(1)
        send_keys('{ENTER}')
        sleep(2)
        click(button="left", coords=(int(width - (width * 71.7 / 100)),
                                     int(height - (height * 90 / 100))))  # MAIN WIN SEARCH BAR
        for i in range(len(keyword[count])):
            send_keys('{BACK}')
        count += 1


def exit_browser():
    # FULLY EXIT EDGE BROWSER
    CREATE_NO_WINDOW = 0x08000000
    pids = []
    for i in psutil.process_iter():
        if "msedge.exe" in i.name():
            pids.append(i.pid)
    for i in range(len(pids)):
        subprocess.call(f"taskkill /PID {pids[i]} /f", creationflags=CREATE_NO_WINDOW)


def remove_history():
    sleep(1)
    exit_browser()
    sleep(1)
    # REMOVE HISTORY FILE
    h_dir = os.path.expanduser('~')
    path = os.path.join(h_dir, "AppData\\Local\\Microsoft\\Edge\\User Data\\Default", "History")
    try:
        os.remove(path)
    except FileNotFoundError:
        messagebox.showerror("Reward Collector", "History file not found")


def start():
    try:
        user_inp.get()
        if user_inp.get() == 0:
            return messagebox.showerror("Reward Collector",
                                        "Input must be a positive number!\nTry Again!") and restart()
        for i in range(0, user_inp.get() + 1):
            search()
        if check_var.get() == 1:
            remove_history()
        exit_app()
    except TclError:
        return messagebox.showerror("Reward Collector", "Input must be a positive number!\nTry Again!") and restart()


def exit_app():
    sleep(1)
    exit_browser()
    messagebox.showinfo("Reward Collector", "Script complete!")
    exit(0)


def restart():
    sleep(1)
    exit_browser()
    main()


def main():
    act = Activation()
    if act.check_licence_status() is True:
        window_start()
    elif act.check_licence_status() is False:
        act.register()


if __name__ == '__main__':
    main()
