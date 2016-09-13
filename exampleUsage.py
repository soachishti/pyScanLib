from pyScanLib import pyScanLib

#======================================================================
#	Name:	    saneLib
#   Location:   https://github.com/soachishti/pyScanLib
#	License:    BSD 2-Clause License
#======================================================================

ls = pyScanLib()

scanners = pyScanLib.getScanners()
print scanners

ls.setScanner(scanners[0])

# Below statement must be run after setScanner()
ls.setDPI(300)

print ls.getScannerSize() # (left,top,width,height)

# Set Area in Pixels
# width = ls.pixelToInch(128) 
# height = ls.pixelToInch(128)
# ls.setScanArea(width=width,height=height) # (left,top,width,height)

# Set Area in centimeter
# width = ls.cmToInch(10) 
# height = ls.cmToInch(10)
# ls.setScanArea(width=width,height=height) # (left,top,width,height)

# A4 Example
ls.setScanArea(width=8.26,height=11.693) # (left,top,width,height) in Inches

ls.setPixelType("color") # bw/gray/color

pil = ls.scan()
pil.show()
pil.save("scannedImage.jpg")

ls.closeScanner() # unselect selected scanner in setScanners()
ls.close() # Destory whole class