pyScanLib
=============================

An combination of Twain and SANE API

Requirements:
------------
* Python 2.6/2.7 (Windows) 
* Python 2.6-3.4 (Linux)
* SANE API for Linux, Mac OS
* TWAIN API for Win32

Functions:
------------
* pyScanLib() - Main Class
* getScanners() - Return Scanner with Name
* setScanners(scannerName)
* setDPI(dpi)
* setScanArea(left,top,width,height) - For scanning selected Area size in Inches
* getScannerSize() - Return scanner size eg. (left, top, right, bottom)
* setPixelType("color") - bw (Black & White), gray and color
* scan() - Start Scanning
* closeScanner() - Unselect selected scanner
* close() - Destory connected API Class

Special Function:
----------------
* pixelToInch(pixel) - Convert Pixel(s) to Inch(es)
* cmToInch(cm) - Convert Centimeter(s) to Inch(es)
* inchTomm(inch) - Convert Inch(es) to Millimeter(s)
* mmToInch(mm) - Convert Millimeter(s) to Inch(es)

Library Installation:
------------------
- Linux or Mac OS
 * brew install sane-backends
 * pip install python-sane
- Windows
 * Download and install twain from [TWAIN PyPI](https://pypi.python.org/pypi/twain)

Example:
------------
        
        from pyScanLib import pyScanLib

        ls = pyScanLib() # load scanner library
        devices = ls.getScanners()
        ls.setScanner(devices[0])

        ls.setDPI(300)
        
        # A4 Example
        ls.setScanArea(width=8.26,height=11.693) # (left,top,width,height) in inches

        ls.setPixelType("color") # bw/gray/color

        pil = ls.scan()
        pil.show()
        pil.save("scannedImage.jpg")
        
        ls.closeScanner() # unselect selected scanner, set in setScanners()
        ls.close() # Destory whole class
        
Detail Example:
------------
Check [exampleUsage.py](exampleUsage.py) in repo

Notice:
------------
* Known to work on Linux (Python 3.4) [Pull #1](https://github.com/soachishti/pyScanLib/pull/1)
* Known to work on Mac OS [Pull #2](https://github.com/soachishti/pyScanLib/pull/2)
* Not tested on Linux by author, however work perfect on Windows.

TODO:
-------
* Implement scanPreview()

License:
------------
pyScanLib uses BSD 2-Clause License.
