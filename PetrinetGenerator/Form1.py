# Tkinterモジュールのインポート
import numpy as np
import tkinter
from tkinter import filedialog
import tkinter.ttk as ttk
import xml.etree.ElementTree as Et
# from numba import jit
import random
import statistics
import matplotlib.pyplot as plt
import os


# def makeloop():
def Vertexinfomation(vertex, hoge, hoge2):
    location = Et.SubElement(vertex, "location", {"x": "100"})
    location.set("y", "150")
    size = Et.SubElement(vertex, "size", {"width": "50"})
    size.set("height", "30")


# ％の入力フォーム周りの表示
def percentage(wheretab, xheight, yheight):
    Label_NoP = tkinter.Label(wheretab, text="%")
    Label_NoP.pack()
    Label_NoP.place(x=xheight + 15, y=yheight - 10)

    EditBox_NoP = tkinter.Entry(wheretab, width=3)
    EditBox_NoP.insert(tkinter.END, "")
    EditBox_NoP.pack()
    EditBox_NoP.place(x=xheight - 10, y=yheight - 10)


class maketab(ttk.Notebook):
    def __init__(self, master):  # 1 ボタンの設定
        super().__init__(master=None)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        note = ttk.Notebook(self)
        note.pack(expand=1, fill="both")
        note0 = InputTab(master=self)
        note1 = InputTab2(self)

        note.add(note0, text="入力")
        note.add(note1, text="生成設定")


class InputTab2(tkinter.Frame):

    def __init__(self, master):  # 1 ボタンの設定
        super().__init__(master)


class InputTab(tkinter.Frame):
    def __init__(self, master):  # 1 ボタンの設定
        super().__init__(master, height=400, width=400)
        # Filename入力
        self.Filenamelabel = tkinter.Label(self, text=u'FileName', font=("u", 10), height=1)
        self.Filenamelabel.place(x=10, y=40)

        self.Filename = tkinter.Entry(self, width=15, validate="focusout",
                                      validatecommand= self.Rangeloop)
        self.Filename.place(x=80, y=40)
        # プレース数
        self.Label_NoP = tkinter.Label(self, text=u'NumberofPlace')
        self.Label_NoP.place(x=10, y=70)


        self.EditBox_NoP = tkinter.Entry(self, width=8, validate="focusout", validatecommand=self.Rangeloop)
        self.EditBox_NoP.place(x=100, y=70)

        # トランジション数
        self.Label_NoT = tkinter.Label(self, text=u'NumberofTransition')
        self.Label_NoT.place(x=180, y=70)

        self.EditBox_NoT = tkinter.Entry(self, width=8, validate="focusout", validatecommand=self.Rangeloop)
        self.EditBox_NoT.place(x=300, y=70)

        # ジェネレートボタン
        self.StartButton = tkinter.Button(self, text='Generate', command=self.MakeXml_main)
        self.StartButton.place(x=300, y=300)

        self.label1_1 = tkinter.Label(self, text="About vertices and Loops", font=("", 16), height=1)
        self.label1_1.place(x=0, y=5)

        # ループ規模の範囲
        self.rangeloop = tkinter.Label(self, text="≦Range of Loop size≦", font=("u", 10), height=1)
        self.rangeloop.place(x=40, y=110)
        self.rangeloop.config(state="disable")

        self.rangeloopbox_Min = tkinter.Entry(self, width=4, validate="focusout", validatecommand=self.CommonPath)
        self.rangeloopbox_Min.place(x=15, y=110)
        self.rangeloopbox_Min.config(state="disable")

        self.rangeloopbox_Max = tkinter.Entry(self, width=4, validate="focusout", validatecommand=self.CommonPath)
        self.rangeloopbox_Max.place(x=175, y=110)
        self.rangeloopbox_Max.config(state="disable")

        self.notifymax = tkinter.Label(self, font=("", 13))
        self.notifymax.place(x=330, y=110)

        self.label1_1 = tkinter.Label(self, text="Common path", font=("", 16), height=1)
        self.label1_1.place(x=0, y=160)
        # 共通路の出口数の範囲

        self.BFV = tkinter.Label(self, text="Branch Factor Variance(BFV)", font=("u", 10), height=1)
        self.BFV.place(x=20, y=200)
        self.BFV.config(state="disable")

        # BFV関連
        global vari
        vari = tkinter.StringVar()
        self.BFVisAvailableBox = ttk.Combobox(self,
                                              values=[
                                                  "Available",
                                                  "NotAvailable"
                                              ], width=12, textvariable=vari)
        self.BFVisAvailableBox.place(x=200, y=200)
        # self.BFVisAvailableBox.current(1)
        self.BFVisAvailableBox.config(state="disable")
        self.BFVisAvailableBox.bind("<<ComboboxSelected>>", self.BFVCombo)

        self.DoF = tkinter.Label(self, text="Degree of freedom", font=("u", 10), height=1)
        self.DoF.place(x=20, y=240)
        self.DoF.config(state="disable")

        self.DegreeofFreedomEntry = tkinter.Entry(self, width=4)
        self.DegreeofFreedomEntry.place(x=140, y=240)
        self.DegreeofFreedomEntry.config(state="disable")

        self.BV = tkinter.Label(self, text="Branch Variance ", font=("u", 10), height=1)
        self.BV.place(x=20, y=280)
        self.BV.config(state="disable")

        self.BranchVarianceEntry = tkinter.Entry(self, width=4)
        self.BranchVarianceEntry.place(x=120, y=280)
        self.BranchVarianceEntry.config(state="disable")



    def Rangeloop(self):
        # まずは入力解禁される条件
        global Filename
        PlaceValue = self.EditBox_NoP.get()
        # print(PlaceValue)
        TransitionValue = self.EditBox_NoT.get()
        Filename = self.Filename.get()
        # print(TransitionValue)
        if PlaceValue != "" and TransitionValue != "" and Filename !="":
            self.rangeloop.config(state="normal")
            self.rangeloopbox_Min.config(state="normal")
            self.rangeloopbox_Max.config(state="normal")

            # 最大、最小のデフォルト値設定

            # 最初に値の削除(これをしないと前の値が残ってしまう)

            self.Default_max = tkinter.StringVar()

            if PlaceValue >= TransitionValue:
                self.Default_max.set(str(int(TransitionValue) * 2 // 10))
            else:
                self.Default_max.set(str(int(PlaceValue) * 2 // 10))

            # ユーザーに最大値がいくらまで可能か知らせる
            self.notifyRange = tkinter.Label(self, text="Max up to", font=("", 13), height=1)
            self.notifyRange.place(x=250, y=110)
            # self.rangeloopbox_Max.insert(tkinter.END, Default_max)
            self.notifymax["text"] = self.Default_max.get()

        return True

    def CommonPath(self):
        RangeminValue = self.rangeloopbox_Min.get()
        RangemaxValue = self.rangeloopbox_Max.get()

        if RangemaxValue != "" and RangeminValue != "":
            self.BV.config(state="normal")
            self.BFVisAvailableBox.config(state="normal")
            self.BFV.config(state="normal")
            self.BranchVarianceEntry.config(state="normal")
            # 前に残っていたデータの削除

        return True

    def BFVCombo(self, *args):
        print(vari.get())
        if vari.get() == "Available":
            self.DegreeofFreedomEntry.config(state="normal")
            self.DegreeofFreedomEntry.delete(0, tkinter.END)
            self.DoF.config(state="normal")

        else:

            self.DegreeofFreedomEntry.config(state="disable")
            self.DegreeofFreedomEntry.delete(0, tkinter.END)
            self.DoF.config(state="disable")

    # 入力された情報に基づいてxmlファイル生成

    def MakeXml_main(self):

        Count = 1
        i = 0

        iDirPath = filedialog.askdirectory(initialdir="/")
        print(iDirPath + "/" + Filename + str(i) + ".xml")
        while i < Count:
            if Count == 1:
                self.makeXml(iDirPath + "/" + Filename + ".xml")
            else:
                self.makeXml(iDirPath + "/" + Filename + str(i) + ".xml")
            i += 1

        if (vari.get() == "NotAvailable"):
            print("ブランチ分散:無")
            print("ブランチ数:" + str(self.BranchVarianceEntry.get()))
        else:
            print("ブランチ分散:有")

        print("ループサイズ(最小):" + str(self.rangeloopbox_Min.get()) + "ループサイズ(最大):" + str(self.rangeloopbox_Max.get()))
        print("CP数（中央値)" + str(statistics.median(CPcountlis)))

    def makeXml(self, path):
        global Vernumlist
        global Vernum
        global Vertransitionlist
        global VT2
        global CPcountlis
        global pltlist
        pltlist = []
        Vernum = 1
        Vernumlist = []
        Vertransitionlist = []
        CPexit_graph = []
        VT2 = []
        CPcountlis = []

        petrinet = Et.Element("petrinet")  # Root要素の作成
        page = Et.SubElement(petrinet, "page", {"id": "page0"})
        page.set("name", "a")

        # 記録用
        SiphonCount = 0
        CPCount = 0

        Loopsize = random.randint(int(self.rangeloopbox_Min.get()), int(self.rangeloopbox_Max.get()))
        makefirstloop(Loopsize, page)

        # カイ二乗分布に従うかどうか

        # 共通路出口数の平均をばらつかせるかどうか(BFV)
        DegreeofFreedom = 0
        if vari.get() == "NotAvailable":
            Normalvariance = 0
        else:
            Normalvariance = 1
            DegreeofFreedom = int(self.DegreeofFreedomEntry.get())

        while len(Vernumlist) <= int(self.EditBox_NoP.get()) + int(self.EditBox_NoT.get()):
            CPEnt = random.choice(Vertransitionlist)
            CPdist = 3
            Currentver = CPEnt

            CPEnt, CPexit = makecp()

            CPexit_population = np.random.normal(0, Normalvariance) ** 2
            for i in range(DegreeofFreedom):
                CPexit_population += np.random.normal(0, Normalvariance) ** 2

            CPexit_population += int(self.BranchVarianceEntry.get())
            CPexit_graph.append(int(CPexit_population))

            while CPexit_population - 1 > 0:
                Loopsize = random.randint(int(self.rangeloopbox_Min.get()), int(self.rangeloopbox_Max.get()))
                makeloop(CPexit, CPEnt, Loopsize, page)
                CPexit_population = CPexit_population - 1
                SiphonCount = SiphonCount + 1

            CPCount = CPCount + 1
            # 共通路生成
            # CPEnt = random.choice(Vertransitionlist)
            # CPdist = 3
            # while CPdist > 0:
            # currentverの初期値はCPEntである
            # currentverの一個後の要素xをvernumlistから参照

            # もしxがvernumlistにおいて存在すれば、1個進む
            # xがなければCurrentverをCPexiとし、whileから抜ける

        # 保存
        print("サイフォン数:" + str(SiphonCount))
        print("共通路数:" + str(CPCount))
        CPcountlis.append(CPCount)
        plt.hist(CPexit_graph, 20, ec='black')
        plt.title(
            "Scale:" + str(int(self.EditBox_NoP.get()) + int(self.EditBox_NoT.get())) + "DoF:" + str(DegreeofFreedom),
            fontsize=20)
        plt.show()
        Data = Et.ElementTree(petrinet)  # Root要素を指定
        Data.write(path, encoding='UTF-8')

    # 上流(Place,Transition)の値が変更されたとき


def makecp():
    CPEnt = random.choice(Vertransitionlist)
    CPdist = 3
    Currentver = CPEnt
    while True:
        # currentverの一個後の要素xをvernumlistから参照
        CurrentIndex = Vernumlist.index(Currentver)
        if Vernumlist[CurrentIndex] != '＊' and Vernumlist[-1] != Currentver:
            Vernumlist[CurrentIndex] = '＊'
            NextIndex = CurrentIndex + 1
            Nextver = Vernumlist[NextIndex]

            if Currentver in Vertransitionlist:
                Vertransitionlist.remove(Currentver)

        else:
            CPexit = Currentver
            break
        if CPdist <= 1 or Nextver == '＊':
            break
        Currentver = Nextver
        CPdist = CPdist - 1

    CPexit = Currentver

    return CPEnt, CPexit


def makeloop(Startver, Endver, Loopsize, page):
    # 初期条件:Startverがプレースかトランジションか
    Numberofmake = 0
    global Vernum
    FirstVernum = Vernum
    if Startver in VT2:
        PorT = "Place"
        PorT = makevertex(PorT, page, Vernum + 2)
        arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 1)})
        makearc(arc, Startver, Vernum + 2)
        while True:
            Vernum = Vernum + 2
            PorT = makevertex(PorT, page, Vernum + 2)
            arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 1)})
            makearc(arc, Vernum, Vernum + 2)
            Numberofmake = Numberofmake + 1
            if Numberofmake >= Loopsize - 1:
                break

    else:
        PorT = "Transition"
        PorT = makevertex(PorT, page, Vernum + 2)
        arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 1)})
        makearc(arc, Startver, Vernum + 2)
        while True:
            Vernum = Vernum + 2
            PorT = makevertex(PorT, page, Vernum + 2)
            arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 1)})
            makearc(arc, Vernum, Vernum + 2)
            Numberofmake = Numberofmake + 1
            if Numberofmake >= Loopsize - 1:
                break

    if PorT == "Place":
        Vernum = Vernum + 2
        PorT = makevertex(PorT, page, Vernum + 2)
        arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 1)})
        makearc(arc, Vernum, Vernum + 2)

    arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 3)})
    makearc(arc, Vernum + 2, Endver)
    Vernum = Vernum + 3

    # else:
    #     while Numberofmake <= Loopsize:
    #         # maketransition
    #         transition = Et.SubElement(page, "transition", {"id": "id" + str(Vernum)})
    #         transition.set("name", str(Vernum))
    #         transition.set("portir", "None")
    #         Vertexinfomation(transition, 222, 221)
    #         Vernumlist.append("id" + str(Vernum))
    #         Vertransitionlist.append("id" + str(Vernum))
    #         Vernum = Vernum + 1
    #         # makeplace
    #         place = Et.SubElement(page, "place", {"id": "id" + str(Vernum)})
    #         place.set("name", str(Vernum))
    #         place.set("initialmarking", "0")
    #         place.set("portdir", "None")
    #         place.set("capacity", "0")
    #         Vertexinfomation(place, 222, 221)
    #         Vernumlist.append("id" + str(Vernum))
    #         Numberofmake += 2
    #         if Numberofmake > Loopsize:
    #             break
    #     Vernum = Vernum + 1

    return


def makefirstloop(size, page):
    global Vernum
    PorT = "Transition"
    Numberofmake = 0
    PorT = makevertex(PorT, page, Vernum)
    while True:
        PorT = makevertex(PorT, page, Vernum + 2)
        arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 1)})
        makearc(arc, Vernum, Vernum + 2)

        if Numberofmake >= size - 1:
            break
        Vernum = Vernum + 2
        Numberofmake = Numberofmake + 1

    if PorT == "Place":
        Vernum = Vernum + 2
        PorT = makevertex(PorT, page, Vernum + 2)
        arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 1)})
        makearc(arc, Vernum, Vernum + 2)
    arc = Et.SubElement(page, "arc", {"id": "id" + str(Vernum + 3)})
    makearc(arc, Vernum + 2, 1)
    Vernum = Vernum + 3

    return


def makevertex(PorT, page, Vernum):
    global Vernumlist
    global Vertransitionlist
    global VT2
    if PorT == "Transition":
        transition = Et.SubElement(page, "transition", {"id": "id" + str(Vernum)})
        transition.set("name", str(Vernum))
        transition.set("portir", "None")
        Vertexinfomation(transition, 222, 221)
        Vertransitionlist.append(str(Vernum))
        VT2.append(str(Vernum))
        PorT = "Place"
    else:

        place = Et.SubElement(page, "place", {"id": "id" + str(Vernum)})
        place.set("name", str(Vernum))
        place.set("initialmarking", "0")
        place.set("portdir", "None")
        place.set("capacity", "0")
        Vertexinfomation(place, 222, 221)
        PorT = "Transition"

    Vernumlist.append(str(Vernum))
    return PorT


def makearc(arc, Source, Target):
    arc.set("source", "id" + str(Source))
    arc.set("target", "id" + str(Target))
    arc.set("delay", "0")
    arc.set("weight", "1")
    points = Et.SubElement(arc, "points")
    point = Et.SubElement(points, "point", {"x": "100"})
    point.set("y", "150")
    point = Et.SubElement(points, "point", {"x": "100"})
    point.set("y", "150")


if __name__ == "__main__":
    root = tkinter.Tk()
    # ウィンドウの名前を設定
    root.title("demo_Tkinter")
    # ウィンドウの大きさを設定
    root.geometry("400x400")
    # タブの作成
    maketab(root)

    # tab1

    # プレース数

    # tab2 各要素の割合
    # canvas = tkinter.Canvas(tab2, bg="white", width=400, height=100)
    # canvas.place(x=0, y=20)
    #
    # img = ImageTk.PhotoImage(file="place.png")
    # canvas.create_image(50, 50, image=img)
    # percentage(tab2, 50, 140)
    #
    # img2 = ImageTk.PhotoImage(file="1to1tran.bmp")
    # canvas.create_image(150, 50, image=img2)
    # percentage(tab2, 150, 140)
    #
    # twooneplace = ImageTk.PhotoImage(file="2to1place.bmp")
    # canvas.create_image(250, 50, image=twooneplace)
    # percentage(tab2, 250, 140)
    #
    # twoonetran = ImageTk.PhotoImage(file="2to1tran.bmp")
    # canvas.create_image(350, 50, image=twoonetran)
    # percentage(tab2, 350, 140)
    #
    # canvas = tkinter.Canvas(tab2, bg="white", width=400, height=100)
    # canvas.place(x=0, y=160)
    #
    # onetwoplace = ImageTk.PhotoImage(file="1to2place.bmp")
    # canvas.create_image(50, 50, image=onetwoplace)
    # percentage(tab2, 50, 280)
    #
    # onetwotran = ImageTk.PhotoImage(file="1to2tran.bmp")
    # canvas.create_image(150, 50, image=onetwotran)
    # percentage(tab2, 150, 280)
    #
    # twotwoplace = ImageTk.PhotoImage(file="2to2place.bmp")
    # canvas.create_image(250, 50, image=twotwoplace)
    # percentage(tab2, 250, 280)
    #
    # twotwotran = ImageTk.PhotoImage(file="2to2tran.bmp")
    # canvas.create_image(350, 50, image=twotwotran)
    # percentage(tab2, 350, 280)
    # イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
    root.mainloop()

# 画像表示
