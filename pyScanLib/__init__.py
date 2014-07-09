import sys
import unitConverter  # Contains unit converting functions ie millimeter to inch (mmToInch) etc


platform = sys.platform

if platform == "win32":
    import twainLib

    class pyScanLib(twainLib.twainLib, unitConverter.unitConverter):
        pass

elif platform == "linux":
    import saneLib

    class pyScanLib(saneLib.saneLib, unitConverter.unitConverter):
        pass

else:
    raise Exception("UnknownPlatform")
