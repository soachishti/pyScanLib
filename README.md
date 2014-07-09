pyScanLib
=============================

An combination of Twain and SANE API

Requirements:
------------
* Python 2.*
* SANE API for Linux
* Twain Lib for Win32

Functions:
------------
* pyScanLib() - Main Class
* getScanners() - Return Scanner with Name
* setScanners(scannerName)
* setDPI(dpi)
* setScanArea(left,top,width,height) - For scanning selected Area size in Inches
* setPixelType("color") - bw (Black & White), gray and color
* scan() - Start Scanning
* closeScanner() - Unselect selected scanner
* close() - Destory connected API Class

Special Function:
----------------
* pixelToInch(pixel) - Convert Pixel(s) to Inch(es) using DPI from setDPI() or default 200
* cmToInch(cm) - Convert Centimeter(s) to Inch(es)
* inchTomm(inch) - Convert Inch(es) to Millimeter(s)
* mmToInch(mm) - Convert Millimeter(s) to Inch(es)

Example:
------------
        
        from includes.scannerLib import scanLib

        loadScanner = scanLib()
        scanners = loadScanner.getScanners()
        loadScanner.setScanner(scanners[0])

        loadScanner.setDPI(300)
        loadScanner.setScanArea(width=512,height=512) #(left,top,width,height)
        loadScanner.setPixelType("color") #bw/gray/color

        PIL = loadScanner.scan()
        PIL.save("scanImage.jpg")
        loadScanner.closeScanner() # unselect selected scanner in setScanners()
        loadScanner.close() # Destory whole class
        
Detail Example:
------------
Check [exampleUsage.py](blob/master/exampleUsage.py) in repo