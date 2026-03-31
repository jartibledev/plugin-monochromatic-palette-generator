
from CTkColorPicker import *
import customtkinter as ctk
import colorsys
import os


class FloatSpinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                  step_size: int= 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.hover = "#7A7A7A"
        self.foreground = "transparent"


        self.configure(fg_color=("gray78", "gray28"))

        self.grid_columnconfigure((0, 2), weight=0)  
        self.grid_columnconfigure(1, weight=1) 

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6, fg_color=self.foreground, hover_color = self.hover ,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0, bg_color=self.foreground )
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button =ctk.CTkButton(self, text="+", width=height-6, height=height-6, fg_color=self.foreground, hover_color = self.hover,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        self.entry.insert(0, "0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) :
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))

class GeneratePalette :

    def __init__(self):
        self.listColorRgb = []     

    def Normalize(self, Value,Min,Max):
        Output = Value
        if Value > Max:
            Output = Max
        elif Value < Min:
            Output = Min
        return Output

    def createPalette (self, hexColorInput, numberColorsInput):
            hexColor = hexColorInput
            numberColors = numberColorsInput

            rgbColor = self.hexToRgb(hexColor)
            self.listColorRgb = self.monochromaticColor( rgbColor, numberColors )

            hexListColor = self.generateHexList(self.listColorRgb)
            print (hexListColor)

            return hexListColor
    
    def rgbToHex(self, r,g,b):
        return ('#{:02x}{:02x}{:02x}'). format(r, g, b)

    def hexToRgb(self, hexColor : str ):
            hexColor = hexColor.lstrip('#')
            return list(int(hexColor[i:i+2],16) for i in (0, 2, 4))

    def generateHexList( self, listColorsRgb ):
        mylistColorsRgb = listColorsRgb
        sortedListColorsRgb = self.sortByLuminance( mylistColorsRgb )
        listColorHex = []
        numbersColors = len(sortedListColorsRgb)
        for i in range(numbersColors) :
            listColorHex.append( self.rgbToHex(sortedListColorsRgb[i][0], sortedListColorsRgb[i][1], sortedListColorsRgb[i][2] ))
        return listColorHex
    
    def sortByLuminance(self, colores_rgb):
        def calcular_luminancia(rgb):
            r, g, b = rgb
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        return sorted(colores_rgb, key=calcular_luminancia, reverse=True)

    def monochromaticColor(self, ColorInput, numberColors):
        color = ColorInput
        color = list(colorsys.rgb_to_hsv(ColorInput[0] / 255, ColorInput[1] / 255, ColorInput[2] / 255))
        
        numberColors_selectionated = numberColors
        percentage_increment = 100 / numberColors_selectionated

        increment = [ 0, percentage_increment/100, numberColors_selectionated/100 ]
        result = []
        output = []
        for x in increment:
            for y in increment:
                result.append(list(map(lambda x: self.Normalize(round(x * 255),0,255), colorsys.hsv_to_rgb(color[0], self.Normalize(color[1],0,100) + x, self.Normalize(color[2] + y,0,100)))))
                result.append(list(map(lambda x: self.Normalize(round(x * 255),0,255), colorsys.hsv_to_rgb(color[0], self.Normalize(color[1],0,100) - x, self.Normalize(color[2] - y,0,100)))))
        [output.append(x) for x in result if x not in output]
        return output

    @property 
    def getRgbList(self):
        listSortedColor = self.sortByLuminance(self.listColorRgb) 

        return listSortedColor
    
    def getHexList(self):
        return self.generateHexList()
    
class GenerateDocumets:
    def __init__(self):
        pass
    
    def createDocument(self, listrgbColorInput : list , archiveNameInput : str ):
        listStringcolor = self.listToString(listrgbColorInput)
        verticalListColorRgb = self.lineFeed ( listStringcolor)

        archiveName = archiveNameInput 
        if not archiveName:
            archiveName = "Untitle"
        
        contentText = "Gimp  palette\nName: " + archiveName + "\n#" + "\n" + verticalListColorRgb 
        self.writeDocument( archiveName, contentText)
        
    def writeDocument(self, archiveName, contentText):
        folder =  r'C:\Users\Usuario\Desktop\prueba'
        fileName= archiveName + ".gpl"
        path= os.path.join(folder, fileName)

        with open(path, 'w', encoding='utf-8', ) as archive:
            archive.write(contentText)
        print(f"Document '{fileName} make succesfully.")
    
    def lineFeed (self, arrayStringColor):
        newArrayStringColor = arrayStringColor
        listStringColor = newArrayStringColor.split()
        lineFeed = "\n"
        arrayStringText = []

        for i, element in enumerate(listStringColor):
            arrayStringText.append(element)
            if (i + 1) % 3 == 0:
                arrayStringText.append(lineFeed)
            
            contentText = " ".join(arrayStringText)

        return contentText
        
    def listToString (self, listRgbColorInput):
            newListrgbColor = listRgbColorInput 
           
            flatStringColor = [elemento for sublist in newListrgbColor for elemento in sublist ]
            
            listStringColor =' '.join(map(str,flatStringColor))
            return listStringColor



class GUI (ctk.CTk) :
    def __init__(self):
        super().__init__()
       

          
        self.geometry("400x800")
        self.title("Palettte Generator")
        ctk.set_appearance_mode("dark")      


        

        self.stringVariableName = ctk.StringVar(self)
        self.infoWheelColor = ctk.CTkLabel (self, text="Select the color to create the palette:", text_color="#D4D4D4")
        self.infoWheelColor.pack(padx=20, pady=10)
        self.wheelColor = CTkColorPicker (self)
        self.wheelColor.pack(padx=20, pady=20)

        self.infoNamePalette = ctk.CTkLabel (self, text="Write the palette color:", text_color="#D4D4D4")
        self.infoNamePalette.pack(padx=20, pady=5)

        self.entryNamePalette = ctk.CTkEntry(self, textvariable= self.stringVariableName, width=200)
        self.entryNamePalette.pack(padx=30, pady=5)

        self.spinbox = FloatSpinbox(self, width=150, step_size=1)
        self.spinbox.pack(padx=20, pady=5)
        self.spinbox.set(0)

        self.generatePalete = GeneratePalette() 
        self.generateDocumets = GenerateDocumets()

        self.buttonCreatePalette = ctk.CTkButton(self, text="Generate Palette", text_color="#D4D4D4", command= self.crearPalette, fg_color="#585858" , hover_color="#7A7A7A")
        self.buttonCreatePalette.pack(padx=20, pady=5)

        self.buttonExportDocument = ctk.CTkButton(self, text="Export Palette as document", text_color="#D4D4D4", command= self.exportDocument, fg_color="#585858", hover_color="#7A7A7A" )
        self.buttonExportDocument.pack(padx=20, pady=5)


        self.colorFrame = ctk.CTkScrollableFrame(self, fg_color = "transparent", scrollbar_button_hover_color="#7A7A7A", label_text="Your palette", label_text_color="#D4D4D4")
        self.colorFrame.pack(pady=20)

        
    def createFrames (self, numberColors, hexListColor):
        myColorFrame = self.colorFrame
        for widget in myColorFrame.winfo_children():
            widget.destroy()

        for i in range(numberColors):
            colorLabel = ctk.CTkLabel(myColorFrame,text_color="black", text=hexListColor[i], fg_color=hexListColor[i], width=100, height=50)
            colorLabel.pack(padx=30, pady=5)
    
    def crearPalette (self):
        color = self.wheelColor.get()
        number = self.spinbox.get()
        hexListColorInput = self.generatePalete.createPalette(hexColorInput= color , numberColorsInput=number)
        self.createFrames (numberColors = number, hexListColor=hexListColorInput  )

    def exportDocument(self):
        name = self.entryNamePalette.get()
        listColorRgb = self.generatePalete.getRgbList
        self.generateDocumets.createDocument(listrgbColorInput=listColorRgb, archiveNameInput=name)    

    def getNumber (self):
        number = self.spinbox.get()
        return number

app = GUI()
app.mainloop()

