from tkinter import *
from tkinter import ttk

I=   ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
II=  ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
III= ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
IV=  ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
V=   ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']

plug_board={}
colours={'red':[],'blue':[],'green':[],'yellow':[],'SeaGreen1':[],'purple':[],'pink':[],'slate grey':[],'turquoise':[],'dark slate grey':[]}
connected=[]

alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ETW=     ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L']
rotor_1= []
rotor_2= []
rotor_3= []
UKW=     ['I', 'M', 'E', 'T', 'C', 'G', 'F', 'R', 'A', 'Y', 'S', 'Q', 'B', 'Z', 'X', 'W', 'L', 'H', 'K', 'D', 'V', 'U', 'P', 'O', 'J', 'N']

rotor_choice=[['I'],['II'],['III']]
letters=[]
pos=[]

r1Shift=0
r2Shift=0
r3Shift=0

for x in I:
    rotor_1.append(x)
for x in II:
    rotor_2.append(x)
for x in III:
    rotor_3.append(x)

def rotate_3(rotor_3_label,where,which,output):
    global r1Shift
    global r2Shift
    global r3Shift
    if(where == 'encrypt'):
        if(r1Shift%26==0 and r2Shift%26==0):
            for i in range(25):
                a = rotor_3.pop()
                rotor_3.insert(0,a)
            r3Shift+=1
            if(r3Shift%26==0):
                r3Shift=0
            rotor_3_label.configure(text=rotor_3[0])
    elif(where=='rotor'):
        if(len(output['text'])==0):
            if(which=='down'):
                for i in range(25):
                    a = rotor_3.pop()
                    rotor_3.insert(0,a)
                r3Shift+=1
                if(r3Shift%26==0):
                    r3Shift=0
                rotor_3_label.configure(text=rotor_3[0])
            else:
                for i in range(1):
                    a = rotor_3.pop()
                    rotor_3.insert(0,a)
                r3Shift+=25
                if(r3Shift>26):
                    r3Shift=r3Shift%26
                rotor_3_label.configure(text=rotor_3[0])
        else:
            pass
    return r3Shift

def rotate_2(rotor_2_label,where,which,output):
    global r1Shift
    global r2Shift
    if(where == 'encrypt'):
        if(r1Shift%26==0):
            for i in range(25):
                a = rotor_2.pop()
                rotor_2.insert(0,a)
            r2Shift+=1
            if(r2Shift%26==0):
                r2Shift=0
            rotor_2_label.configure(text=rotor_2[0])
    elif(where=='rotor'):
        if(len(output['text'])==0):
            if(which=='down'):
                for i in range(25):
                    a = rotor_2.pop()
                    rotor_2.insert(0,a)
                r2Shift+=1
                if(r2Shift%26==0):
                    r2Shift=0
                rotor_2_label.configure(text=rotor_2[0])
            else:
                for i in range(1):
                    a = rotor_2.pop()
                    rotor_2.insert(0,a)
                r2Shift+=25
                if(r2Shift>26):
                    r2Shift=r2Shift%26
                rotor_2_label.configure(text=rotor_2[0])
        else:
            pass
    return r2Shift

def rotate_1(rotor_1_label,where,which,output):
    global r1Shift
    if(where == 'encrypt'):
        for i in range(25):
            a = rotor_1.pop()
            rotor_1.insert(0,a)
        r1Shift+=1
        if(r1Shift%26==0):
            r1Shift=0
        rotor_1_label.configure(text=rotor_1[0])
    elif(where=='rotor'):
        if(len(output['text'])==0):
            if(which=='down'):
                for i in range(25):
                    a = rotor_1.pop()
                    rotor_1.insert(0,a)
                r1Shift+=1
                if(r1Shift%26==0):
                    r1Shift=0
                rotor_1_label.configure(text=rotor_1[0])
            else:
                for i in range(1):
                    a = rotor_1.pop()
                    rotor_1.insert(0,a)
                r1Shift+=25
                if(r1Shift>26):
                    r1Shift=r1Shift%26
                rotor_1_label.configure(text=rotor_1[0])
        else:
            pass
    return r1Shift

def encrypt(self,rotor_1_label,rotor_2_label,rotor_3_label,output):
    if(len(letters)==0):
        pos.append(rotor_1[0])
        pos.append(rotor_2[0])
        pos.append(rotor_3[0])

    letter = self.value
    letters.append(letter)
    r1Shift=rotate_1(rotor_1_label,'encrypt','down',output)
    r2Shift=rotate_2(rotor_2_label,'encrypt','down',output)
    r3Shift=rotate_3(rotor_3_label,'encrypt','down',output)

    if(letter == ' '):
        pass
    else:
        if(letter in plug_board):
            letter = plug_board[letter]

        letter = ETW[alphabet.index(letter)]
        letter_i = alphabet.index(letter)
        letter = rotor_1[(letter_i)%26]
        letter_i = alphabet.index(letter)
        letter = rotor_2[(letter_i-r1Shift)%26]
        letter_i = alphabet.index(letter)
        letter = rotor_3[(letter_i-r2Shift)%26]
        letter_i = alphabet.index(letter)
        letter = UKW[(letter_i-r3Shift)%26]
        letter_i = alphabet.index(letter)
        letter = UKW[(letter_i)%26]
        letter_i = UKW.index(letter)
        letter = alphabet[(letter_i+r3Shift)%26]
        letter_i = rotor_3.index(letter)
        letter = alphabet[(letter_i+r2Shift)%26]
        letter_i = rotor_2.index(letter)
        letter = alphabet[(letter_i+r1Shift)%26]
        letter_i = rotor_1.index(letter)
        letter = alphabet[(letter_i)%26]
        letter_i = ETW.index(letter)
        letter = alphabet[(letter_i)%26]
        if(letter in plug_board):
            letter = plug_board[letter]
    return letter

def rotor_1_pick(val,rotor_1_label,output):
    global rotor_1
    if(len(output['text'])==0):
        rotor_1.clear()
        for i in globals()[str(val)]:
            rotor_1.append(i)
        rotor_1_label.configure(text=rotor_1[0])
        rotor_choice[0].clear()
        rotor_choice[0].append(str(val))
def rotor_2_pick(val,rotor_2_label,output):
    global rotor_2
    if(len(output['text'])==0):
        rotor_2.clear()
        for i in globals()[str(val)]:
            rotor_2.append(i)
        rotor_2_label.configure(text=rotor_2[0])
        rotor_choice[1].clear()
        rotor_choice[1].append(str(val))
def rotor_3_pick(val,rotor_3_label,output):
    global rotor_3
    if(len(output['text'])==0):
        rotor_3.clear()
        for i in globals()[str(val)]:
            rotor_3.append(i)
        rotor_3_label.configure(text=rotor_3[0])
        rotor_choice[2].clear()
        rotor_choice[2].append(str(val))
def Reset(rotor_1_label,rotor_2_label,rotor_3_label,output):
    global r1Shift, r2Shift, r3Shift, rotor_1, rotor_2, rotor_3
    rotor_1.clear()
    rotor_2.clear()
    rotor_3.clear()
    for x in globals()[rotor_choice[0][0]]:
        rotor_1.append(x)
    for x in globals()[rotor_choice[1][0]]:
        rotor_2.append(x)
    for x in globals()[rotor_choice[2][0]]:
        rotor_3.append(x)
    rotor_1_label.configure(text=rotor_1[0])
    rotor_2_label.configure(text=rotor_2[0])
    rotor_3_label.configure(text=rotor_3[0])
    r1Shift = 0
    r2Shift = 0
    r3Shift = 0
def Print(self,output,rotor_1_label,rotor_2_label,rotor_3_label):
    letter = encrypt(self,rotor_1_label,rotor_2_label,rotor_3_label,output)
    output.configure(text='{}{}'.format(output['text'],letter))
    root.clipboard_clear()
    root.clipboard_append(output['text'])

def PlugCon(self,output):
    if(len(output['text']) == 0):
        for i in colours:
            if(len(colours[i])==1):
                self.button.configure(bg=i)
                colours[i].append(self.value)
                connected.append(self.value)
                plug_board[colours[i][0]] = colours[i][1]
                plug_board[colours[i][1]] = colours[i][0]
                break
            elif(len(colours[i])==0):
                self.button.configure(bg=i)
                colours[i].append(self.value)
                connected.append(self.value)
                break


class NewKey(Tk):
    def __init__(self,x,y,Main,n,output,rotor_1_label,rotor_2_label,rotor_3_label):
        self.button = Button(Main, text=alphabet[n],command=lambda:Print(self,output,rotor_1_label,rotor_2_label,rotor_3_label), width=16, height=8)
        self.button.grid(row=y, column=x, sticky=W+E)
        self.value = alphabet[n]
class NewPlug(Tk):
    def __init__(self,x,y,Main,n,output):
        self.button = Button(Main, text=alphabet[n], width=16, height=8, command=lambda:PlugCon(self,output))
        self.button.grid(row=y, column=x)
        self.value = alphabet[n]
class Window(Tk):
    def __init__(self):

        Tk.__init__(self)
        Tk.wm_title(self,'Enigma')
        Main = Frame(self, bg='dark grey')
        Main.pack(fill='both', expand=True, side='top')

        rotor_frame = Frame(Main, bg='grey30')
        rotor_frame.pack(fill='both', expand=True, side='top')
        rotor_frame.grid_propagate(0)
        keys_frame = Frame(Main, bg='light grey', height=100)
        keys_frame.pack(fill='both', expand=True, side='top')
        keys_frame.grid_propagate(0)
        plug_frame = Frame(Main, bg='grey30')
        plug_frame.pack(fill='both', expand=True,side='top')
        plug_frame.grid_propagate(0)

        drop_1_str = StringVar()
        drop_2_str = StringVar()
        drop_3_str = StringVar()
        rotor_1_drop = ttk.OptionMenu(rotor_frame, drop_1_str,'I','I','II','III','IV','V', command=lambda x :rotor_1_pick(x,rotor_1_label,output))
        rotor_1_drop.grid(row=0, column=4, padx=30, pady=3)
        rotor_2_drop = ttk.OptionMenu(rotor_frame, drop_2_str,'II','I','II','III','IV','V', command=lambda x :rotor_2_pick(x,rotor_2_label,output))
        rotor_2_drop.grid(row=0, column=3, padx=30, pady=3)
        rotor_3_drop = ttk.OptionMenu(rotor_frame, drop_3_str,'III','I','II','III','IV','V', command=lambda x :rotor_3_pick(x,rotor_3_label,output))
        rotor_3_drop.grid(row=0, column=2, padx=30, pady=3)
        outLabel = Label(rotor_frame, text='Output:', bg='light grey')
        outLabel.grid(row=0, column=6)
        left_gap = Frame(rotor_frame, bg='grey30', width=400)
        left_gap.grid(row=1, column=0)
        ETW_bar = Frame(rotor_frame, bg='dark grey', width=80, height=235)
        ETW_bar.grid(row=1, column=1, padx=30)
        rotor_1_bar = Frame(rotor_frame, bg='dark grey', width=50, height=200)
        rotor_1_bar.grid(row=1, column=4, padx=30)
        rotor_2_bar = Frame(rotor_frame, bg='dark grey', width=50, height=200)
        rotor_2_bar.grid(row=1, column=3, padx=30)
        rotor_3_bar = Frame(rotor_frame, bg='dark grey', width=50, height=200)
        rotor_3_bar.grid(row=1, column=2, padx=30)
        UKW_bar = Frame(rotor_frame, bg='dark grey', width=80, height=235)
        UKW_bar.grid(row=1, column=5, padx=30)
        output = Label(rotor_frame, bg='light grey', width=50, height=14)
        output.grid(row=1, column=6, padx=50)

        mess = Label(left_gap, text='You cannot alter rotor and plugboard settings once you start typing!', bg='light grey')
        mess.pack(padx=15)

        rotor_1_label = Label(rotor_1_bar, text=rotor_1[0], width=6, height=5)
        rotor_1_label.grid(row=1, column=0, sticky=N+E+S+W)
        gap = Button(rotor_1_bar, text='/\\', bg='dark grey', width=6, height=4, command=lambda:rotate_1(rotor_1_label,'rotor','up',output))
        gap.grid(row=0, column=0, sticky=N+E+S+W)
        gap = Button(rotor_1_bar, text='\\/', bg='dark grey', width=6, height=4, command=lambda:rotate_1(rotor_1_label,'rotor','down',output))
        gap.grid(row=2, column=0, sticky=N+E+S+W)

        rotor_2_label = Label(rotor_2_bar, text=rotor_2[0], width=6, height=5)
        rotor_2_label.grid(row=1, column=0, sticky=N+E+S+W)
        gap = Button(rotor_2_bar, text='/\\', bg='dark grey', width=6, height=4, command=lambda:rotate_2(rotor_2_label,'rotor','up',output))
        gap.grid(row=0, column=0, sticky=N+E+S+W)
        gap = Button(rotor_2_bar, text='\\/', bg='dark grey', width=6, height=4, command=lambda:rotate_2(rotor_2_label,'rotor','down',output))
        gap.grid(row=2, column=0, sticky=N+E+S+W)

        rotor_3_label = Label(rotor_3_bar, text=rotor_3[0], width=6, height=5)
        rotor_3_label.grid(row=1, column=0, sticky=N+E+S+W)
        gap = Button(rotor_3_bar, text='/\\', bg='dark grey', width=6, height=4, command=lambda:rotate_3(rotor_3_label,'rotor','up',output))
        gap.grid(row=0, column=0, sticky=N+E+S+W)
        gap = Button(rotor_3_bar, text='\\/', bg='dark grey', width=6, height=4, command=lambda:rotate_3(rotor_3_label,'rotor','down',output))
        gap.grid(row=2, column=0, sticky=N+E+S+W)

        keyboard_label = Label(keys_frame, text='Keyboard', bg='light grey')
        keyboard_label.grid(row=0, column=0)
        x=0
        y=1
        n=0
        for i in range(1,27):
            if(i%13==1):
                y+=1
                x=0
            new=NewKey(x,y,keys_frame,n,output,rotor_1_label,rotor_2_label,rotor_3_label)
            x+=1
            n+=1
        reset_frame = Frame(keys_frame, bg='red')
        reset_frame.grid(row=4, columnspan=13, sticky=W+E+N+S)
        keyboard_button_clear = Button(reset_frame, text='Clear', height=5, width=112, command=lambda:output.configure(text=' '))
        keyboard_button_clear.grid(row=0,column=0,sticky=W+E)
        keyboard_button_reset = Button(reset_frame, text='Reset', height=5, width=112, command=lambda:Reset(rotor_1_label,rotor_2_label,rotor_3_label,output))
        keyboard_button_reset.grid(row=0,column=1,sticky=W+E)

        plug_label = Label(plug_frame, text='Plug Board', bg='grey30')
        plug_label.grid(row=0, column=0)
        plug_label = Label(plug_frame, text='Max: 10', bg='grey30')
        plug_label.grid(row=0, column=1)
        x=0
        y=1
        n=0
        for i in range(1,27):
            if(i%13==1):
                y+=1
                x=0
            new=NewPlug(x,y,plug_frame,n,output)
            x+=1
            n+=1


root = Window()
root.geometry('1586x900')
root.mainloop()

























