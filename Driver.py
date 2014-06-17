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
            size=(600, 400))
        
        self.InitUI()
        self.Centre()
        self.Show()
        
        
    def InitUI(self):
        temp = listCars()
        self.carlist = []
        self.carListID = []
        for car in temp:
            self.carListID.append(car[0])
            self.carlist.append(car[1] + " " + car[2])
        
        #=================================================
        # Menu Bar
        #=================================================
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitemAddCar = fileMenu.Append(wx.ID_ADD, 'Add Car', 'Add Car')
        fitemRemoveCar = fileMenu.Append(wx.ID_REMOVE, 'Remove Car', 'Remove Car')
        fitemQuit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnAdd, fitemAddCar)
        self.Bind(wx.EVT_MENU, self.OnRemove, fitemRemoveCar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitemQuit)
        
        
        #=================================================
        # Main Panel
        #=================================================
        
        panel = wx.Panel(self)
        
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Car Name')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        
                    
        # combo box
        cb = wx.ComboBox(panel, -1, choices=self.carlist,
            style=wx.CB_READONLY)
        hbox1.Add(cb, flag = wx.Left)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        
        
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        
        vbox.Add((-1, 10))
        
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Car information')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(self.tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
            border=10)

        vbox.Add((-1, 25))


        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        panel.SetSizer(vbox)

        
    def OnQuit(self, e):
        self.Close()
        
    def OnAdd(self, e):
        print "Adding Car"
        
    def OnRemove(self, e):
        print "Remove Car"
        
    def OnSelect(self,e):
        car = selectCar(self.carListID[e.GetInt()])
        
        carInfo = ""
        
        for i in range(1,len(car)):
            carInfo+= car[i]+" "
            
        self.tc2.SetValue(carInfo)

        
        

            
            
#=============================================================            
        self.Show()

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
    
    if(selection == 1):
        print "adding car\n"
        make = raw_input("What is the car make? ")
        model = raw_input("What is the car model? ")
        year = raw_input("What is the car year? ")
        horsepower = raw_input("What is the car horsepower? ")
        engine = raw_input("What is the car engine? ")
        trans = raw_input("What is the car transmission? ")
        
        if(make or model):
            addCar(initCar(make, model, year,horsepower, engine, trans))            
        else:
            print "Could not add car. The make and model information must be filled in."
        
    elif(selection == 2):
        for car in listCars():
            print car
            print fetchCarParts(car[0])
            
    elif(selection == 3):
        #add autopart
        addCarPart()
            
    elif(selection == 4):
        for car in listCars():
            print car
        remove = int(raw_input("Which car would you like to remove (Number)?"))
        removeCar(remove)
            
    elif(selection == 5):
        print "Deleting all cars"
        clearAllValues()
    
print "Thanks for using this program"
'''
