from pyScanLib import pyScanLib

pyScanLib = pyScanLib()

scanners = pyScanLib.getScanners()
print scanners
pyScanLib.setScanner(scanners[0])

# Below statement must be run after setScanner()
pyScanLib.setDPI(300)

# Set Area in Pixels
width = pyScanLib.pixelToInch(128) 
height = pyScanLib.pixelToInch(128)
pyScanLib.setScanArea(width=width,height=height) #(left,top,width,height)

# Set Area in centimeter
width = pyScanLib.cmToInch(10) 
height = pyScanLib.cmToInch(10)
pyScanLib.setScanArea(width=width,height=height) #(left,top,width,height)

#A4 Example
#pyScanLib.setScanArea(width=8.26,height=11.693) #(left,top,width,height) in Inches

pyScanLib.setPixelType("color") #bw/gray/color

PIL = pyScanLib.scan()
PIL.save("image2.jpg")
pyScanLib.closeScanner() # unselect selected scanner in setScanners()
pyScanLib.close() # Destory whole class