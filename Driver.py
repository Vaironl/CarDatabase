'''
Created on May 25, 2014

@author: Vairon
'''
# tutorial: http://wiki.wxpython.org/AnotherTutorial

from DBConnection import *
import sys
import wx


# init the connection to the database
carDatabase = 'carlist.db'
initConnection(carDatabase)

def initCar(_make, _model, _year, _hp, _engine, _trans):
    car_make = _make
    car_model = _model
    car_year = _year
    car_horsepower = _hp
    car_engine = _engine
    car_transmission = _trans
    
    thisCar = [car_make, car_model, car_year, car_horsepower, car_engine, car_transmission]
    
    return thisCar



# addCar(carDatabase, initCar("Subaru", "WRX", "2010", "250", "2.0L Boxer Engine", "6-speed"))
# addCar(carDatabase, initCar("Scion", "FRS", "2012", "200", "2.0L Boxer Engine", "6-speed"))

class Example(wx.Frame):
    
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(800, 600))
        
        self.InitUI()
        self.Centre()
        self.Show()
        
        
    def InitUI(self):
        self.carListID = []
        self.carlist = []
        
        #=================================================
        # Menu Bar
        #=================================================
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        fitemSaveCar = fileMenu.Append(wx.ID_SAVE, 'Save Car', 'Save Car')
        
        fileMenu.AppendSeparator()
        
        fitemAddCar = fileMenu.Append(wx.ID_ADD, 'Add Car', 'Add Car')
        fitemRemoveCar = fileMenu.Append(wx.ID_REMOVE, 'Remove Car', 'Remove Car')
        fitemQuit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnAdd, fitemAddCar)
        self.Bind(wx.EVT_MENU, self.OnRemove, fitemRemoveCar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitemQuit)
        self.Bind(wx.EVT_MENU, self.SaveCar, fitemSaveCar)
        
        
        #=================================================
        # Main Panel
        #=================================================
        
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Car Name')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        
        # combo box
        self.cb = wx.ComboBox(panel, -1, choices=self.carlist,style=wx.CB_READONLY)
        self.UpdateCarList()
        self.cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        hbox1.Add(self.cb, flag = wx.Left)
        
        stID = wx.StaticText(panel,label='Car ID')
        hbox1.Add(stID, flag = wx.LEFT, border = 10)
        
        self.IDValue = wx.TextCtrl(panel)
        self.IDValue.SetEditable(editable = False)
        hbox1.Add(self.IDValue, flag = wx.LEFT, border = 10)
        
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Car Make')
        hbox2.Add(st2)
        
        self.makeTC = wx.TextCtrl(panel)
        hbox2.Add(self.makeTC, proportion =0, flag = wx.RIGHT | wx.LEFT, border = 10)
        vbox.Add(hbox2, flag= wx.EXPAND |wx.LEFT | wx.TOP, border=10)


        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Car Model')
        hbox3.Add(st3)
        self.modelTC = wx.TextCtrl(panel)
        hbox3.Add(self.modelTC, proportion =0, flag = wx.RIGHT | wx.LEFT, border = 10)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label='Car Year')
        hbox4.Add(st4)
        self.yearTC = wx.TextCtrl(panel)
        hbox4.Add(self.yearTC, proportion =0, flag = wx.RIGHT | wx.LEFT, border = 10)
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st5 = wx.StaticText(panel, label='Car Horsepower')
        hbox5.Add(st5)
        self.horsepowerTC = wx.TextCtrl(panel)
        hbox5.Add(self.horsepowerTC, proportion =0, flag = wx.RIGHT | wx.LEFT, border = 10)
        vbox.Add(hbox5, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st6 = wx.StaticText(panel, label='Car Engine')
        hbox6.Add(st6)
        self.engineTC = wx.TextCtrl(panel)
        hbox6.Add(self.engineTC, proportion =0, flag = wx.RIGHT | wx.LEFT, border = 10)
        vbox.Add(hbox6, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        st7 = wx.StaticText(panel, label='Car Transmission')
        hbox7.Add(st7)
        self.transmissionTC = wx.TextCtrl(panel)
        hbox7.Add(self.transmissionTC, proportion =0, flag = wx.RIGHT | wx.LEFT, border = 10)
        vbox.Add(hbox7, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        self.partList = wx.ListCtrl(panel, -1, style = wx.LC_REPORT)
        self.partList.InsertColumn(0, 'Part Name', width = 150)
        self.partList.InsertColumn(1, 'Notes/Description', width = 400)
        hbox8.Add(self.partList, proportion = 1, flag = wx.EXPAND | wx.TOP, border = 10)
        vbox.Add(hbox8, flag = wx.EXPAND)
        
        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        self.addPart = wx.Button(panel, wx.ID_EXECUTE,'+ Car Part')
        hbox9.Add(self.addPart, proportion =1)
        self.partName = wx.TextCtrl(panel)
        self.partNotes = wx.TextCtrl(panel)
        self.partName.SetHint("Part/Mod Name")
        self.partNotes.SetHint("Part/Mod Notes")
        hbox9.Add(self.partName)
        hbox9.Add(self.partNotes)
        vbox.Add(hbox9)
        
        
        self.Bind(wx.EVT_BUTTON, self.InsertCarPart, self.addPart)
        
        panel.SetSizer(vbox)

    
    def InsertCarPart(self,e):
        tempName = self.partName.GetValue()
        tempNotes = self.partNotes.GetValue()
        tempID = self.IDValue.GetValue()
        if(tempName and tempNotes and tempID):
            addCarPart(tempID, tempName, tempNotes)
            self.UpdateCarParts()
            
        
    def SaveCar(self,e):
        if(self.makeTC.GetValue() and self.modelTC.GetValue()):
            addCar(initCar(self.makeTC.GetValue(), self.modelTC.GetValue(), self.yearTC.GetValue(), self.horsepowerTC.GetValue(), self.engineTC.GetValue(), self.transmissionTC.GetValue()))
            self.UpdateCarList()
            self.clearAllTC()
    
    def OnQuit(self, e):
        self.Close()
        
    def OnAdd(self, e):
        self.clearAllTC()
        
    def OnRemove(self, e):
        carID = self.IDValue.GetValue()
        if carID > 0:
            removeCar(str(carID))
            self.UpdateCarList()
            self.clearAllTC()
            
        
    def OnSelect(self,e):
        car = selectCar(self.carListID[e.GetInt()])
        #0 = ID, 1 = Make, 2 = Model, 3 = Year, 4 = Horsepower, 5= Engine, 6 = Transmission
        self.IDValue.SetValue(str(car[0]))
        self.makeTC.SetValue(car[1])
        self.modelTC.SetValue(car[2])
        self.yearTC.SetValue(car[3])
        self.horsepowerTC.SetValue(car[4])
        self.engineTC.SetValue(car[5])
        self.transmissionTC.SetValue(car[6])
        self.UpdateCarParts()
        

                
    def UpdateCarParts(self):
        carParts = fetchCarParts(self.IDValue.GetValue())
        if carParts:
            self.partList.ClearAll()
            for i in carParts:
                print i
                index = self.partList.InsertStringItem(sys.maxint,i[1])
                self.partList.SetStringItem(index,1,i[2])
        
    
    def clearAllTC(self):
        self.IDValue.Clear()
        self.makeTC.Clear()
        self.modelTC.Clear()
        self.yearTC.Clear()
        self.horsepowerTC.Clear()
        self.engineTC.Clear()
        self.transmissionTC.Clear()
        self.partList.ClearAll()
        self.cb.SetSelection(-1)
        
    def UpdateCarList(self):
        temp = listCars()
        self.carListID = []
        self.carlist = []
        for car in temp:
            self.carListID.append(car[0])
            self.carlist.append(car[1] + " " + car[2])
            
        self.cb.SetItems(self.carlist)

def main():
    ex = wx.App()
    Example(None, title='Size')
    ex.MainLoop()

if __name__ == '__main__':
    main()



'''
selection = 0
while selection != 6:
    
    selection = int(raw_input("1. Add car, 2. See car and mods, 3. Add Auto Part/Mods, 4. Remove Car, 5. Clear All Cars, 6. Exit\n"))
            
    elif(selection == 3):
        #add autopart
        addCarPart()
            
    elif(selection == 5):
        print "Deleting all cars"
        clearAllValues()
    
print "Thanks for using this program"
'''
