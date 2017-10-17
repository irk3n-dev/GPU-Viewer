import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

FrameBufferList = ["vid","vdep", "vt", "xsp", "bfsz", "lvl", "rt", "db", "stereo", "rsz", "gsz", "bsz", "asz", "flt", "srgb", "aux", "depth", "stcl",
                   "acr", "acg", "acb", "aca", "msnum", "msbufs","caveats"]

def FrameBuffer(button):

    def GLXFB(button, value):
        FB_Store.clear()
        TreeFB.set_model(FB_Store)
        if value == 1:
            os.system(
                "glxinfo | awk '/GLX Visuals.*/{flag=1;next}/GLXFBConfigs.*/{flag=0}flag' | awk '/----.*/{flag=1;next}flag' > .Temp/FrameBufferGLXVisual.txt")

            list = []
            with open(".Temp/FrameBufferGLXVisual.txt", "r") as file1:
                for line in file1:
                    list.append(line.split())

            for i in range(len(list)-1):
                    FB_Store.append([list[i][0],list[i][1],list[i][2],list[i][3],list[i][4],list[i][5],list[i][6],list[i][7],list[i][8],list[i][9],list[i][10],list[i][11],list[i][12],list[i][13],list[i][14],list[i][15],list[i][16],list[i][17],list[i][18],list[i][19],list[i][20],list[i][21],list[i][22],list[i][23],list[i][24]])

            label = "%d GLX Visuals"%(len(list)-1)
            button.set_label(label)

        if value == 2:

            os.system(
                "glxinfo | awk '/GLXFBConfigs.*/{flag=1;next}flag' | awk '/----.*/{flag=1;next}flag' > .Temp/FrameBufferGLXFBconfigs.txt")

            list = []
            with open(".Temp/FrameBufferGLXFBconfigs.txt", "r") as file1:
                for line in file1:
                    list.append(line.split())

            for i in range(len(list)-1):
                if list[i][6] == "r" or list[i][6] == "c":
                    pass
                else:
                    list[i].insert(6," ")
                FB_Store.append([list[i][0],list[i][1],list[i][2],list[i][3],list[i][4],list[i][5],list[i][6],list[i][7],list[i][8],list[i][9],list[i][10],list[i][11],list[i][12],list[i][13],list[i][14],list[i][15],list[i][16],list[i][17],list[i][18],list[i][19],list[i][20],list[i][21],list[i][22],list[i][23],list[i][24]])

            label = "%d  GLXFBConfigs"%(len(list)-1)
            button.set_label(label)

    FBWin = Gtk.Window()
    FBWin.set_title("GLX Frame Buffer Configuration")
    FBWin.set_size_request(1050, 500)
    FBGrid = Gtk.Grid()
    FBWin.add(FBGrid)
    FBGrid.set_border_width(20)
    FBGrid.set_row_spacing(30)
    FBGLXButton = Gtk.RadioButton("GLX Visuals")
    FBGLXButton.connect("clicked", GLXFB, 1)
    FBGrid.add(FBGLXButton)
    FBConfigButton = Gtk.RadioButton.new_from_widget(FBGLXButton)
    FBConfigButton.set_label("GLXFBConfigs")
    FBConfigButton.connect("clicked",GLXFB,2)
    FBGrid.attach_next_to(FBConfigButton, FBGLXButton, Gtk.PositionType.RIGHT, 1, 1)
    FBFrame = Gtk.Frame()

    FB_Store = Gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
    TreeFB = Gtk.TreeView(FB_Store, expand=True)
    TreeFB.set_property("enable-grid-lines",3)

    FBGLXButton.set_active(False)

    for i, column_title in enumerate(FrameBufferList):
        FBrenderer = Gtk.CellRendererText(font="Helvetica 11")
        FBrenderer.set_alignment(0.5, 0.5)
        column = Gtk.TreeViewColumn(column_title, FBrenderer, text=i)
        column.set_alignment(0.5)
        column.set_property("min-width", 35)
        TreeFB.append_column(column)

    FBScrollbar = Gtk.ScrolledWindow()
    FBScrollbar.set_vexpand(True)
    FBScrollbar.add(TreeFB)
    FBFrame.add(FBScrollbar)
    FBGrid.attach_next_to(FBFrame, FBGLXButton, Gtk.PositionType.BOTTOM, 25, 1)

    FBWin.show_all()

    #Gtk.main()
