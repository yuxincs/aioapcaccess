"""Sample raw status and its parsed dict."""
from collections import OrderedDict

SAMPLE_STATUS = (
    b"\x00"
    b"\x18APC      : 001,051,1148\n\x00"
    b"'DATE     : 2016-02-09 21:13:11 +0000  \n\x00"
    b"\x16HOSTNAME : localhost\n\x00"
    b"*VERSION  : 3.14.12 (29 March 2014) redhat\n\x00"
    b"\x13UPSNAME  : netrack\n\x00"
    b"\x1eCABLE    : Custom Cable Smart\n\x00"
    b"\x1fDRIVER   : APC Smart UPS (any)\n\x00"
    b"\x17UPSMODE  : Stand Alone\n\x00"
    b"'STARTTIME: 2016-02-09 16:06:47 +0000  \n\x00"
    b"\x1aMODEL    : SMART-UPS 1400\n\x00"
    b"\x18STATUS   : TRIM ONLINE \n\x00"
    b"\x17LINEV    : 247.0 Volts\n\x00"
    b"\x17LOADPCT  : 9.3 Percent\n\x00"
    b"\x17LOADPCT  : 9.3 Percent Load Capacity\n\x00"
    b"\x19BCHARGE  : 100.0 Percent\n\x00"
    b"\x19TIMELEFT : 128.0 Minutes\n\x00"
    b"\x15MBATTCHG : 5 Percent\n\x00"
    b"\x15MINTIMEL : 3 Minutes\n\x00"
    b"\x15MAXTIME  : 0 Seconds\n\x00"
    b"\x17MAXLINEV : 250.9 Volts\n\x00"
    b"\x17MINLINEV : 247.0 Volts\n\x00"
    b"\x17OUTPUTV  : 218.4 Volts\n\x00"
    b"\x10SENSE    : High\n\x00"
    b"\x15DWAKE    : 0 Seconds\n\x00"
    b"\x17DSHUTD   : 180 Seconds\n\x00"
    b"\x15DLOWBATT : 2 Minutes\n\x00"
    b"\x17LOTRANS  : 196.0 Volts\n\x00"
    b"\x17HITRANS  : 253.0 Volts\n\x00"
    b"\x18RETPCT   : 15.0 Percent\n\x00"
    b"\x12ITEMP    : 30.6 C\n\x00"
    b"\x17ALARMDEL : Low Battery\n\x00"
    b"\x16BATTV    : 27.6 Volts\n\x00"
    b"\x13LINEFREQ : 50.0 Hz\n\x00"
    b"\x1dLASTXFER : High line voltage\n\x00"
    b"\rNUMXFERS : 0\n\x00"
    b"\x15TONBATT  : 0 Seconds\n\x00"
    b"\x15CUMONBATT: 0 Seconds\n\x00"
    b"\x0fXOFFBATT : N/A\n\x00"
    b"\x0eSELFTEST : NO\n\x00"
    b"\x0fSTESTI   : 336\n\x00"
    b"\x16STATFLAG : 0x0500000A\n\x00"
    b"\x10DIPSW    : 0x00\n\x00"
    b"\x10REG1     : 0x00\n\x00"
    b"\x10REG2     : 0x00\n\x00"
    b"\x10REG3     : 0x00\n\x00"
    b"\x14MANDATE  : 07/13/99\n\x00"
    b"\x18SERIALNO : GS9229021308\n\x00"
    b"\x14BATTDATE : 13/11/15\n\x00"
    b"\x15NOMOUTV  : 230 Volts\n\x00"
    b"\x16NOMBATTV : 24.0 Volts\n\x00"
    b"\rEXTBATTS : 0\n\x00"
    b"\x13FIRMWARE : 70.11.I\n\x00"
    b"'END APC  : 2016-02-09 21:13:26 +0000  \n\x00"
    b"\x00"
)

PARSED_DICT = OrderedDict(
    [
        ("APC", ("001,051,1148", None)),
        ("DATE", ("2016-02-09 21:13:11 +0000", None)),
        ("HOSTNAME", ("localhost", None)),
        ("VERSION", ("3.14.12 (29 March 2014) redhat", None)),
        ("UPSNAME", ("netrack", None)),
        ("CABLE", ("Custom Cable Smart", None)),
        ("DRIVER", ("APC Smart UPS (any)", None)),
        ("UPSMODE", ("Stand Alone", None)),
        ("STARTTIME", ("2016-02-09 16:06:47 +0000", None)),
        ("MODEL", ("SMART-UPS 1400", None)),
        ("STATUS", ("TRIM ONLINE", None)),
        ("LINEV", ("247.0", "Volts")),
        ("LOADPCT", ("9.3", "Percent Load Capacity")),
        ("BCHARGE", ("100.0", "Percent")),
        ("TIMELEFT", ("128.0", "Minutes")),
        ("MBATTCHG", ("5", "Percent")),
        ("MINTIMEL", ("3", "Minutes")),
        ("MAXTIME", ("0", "Seconds")),
        ("MAXLINEV", ("250.9", "Volts")),
        ("MINLINEV", ("247.0", "Volts")),
        ("OUTPUTV", ("218.4", "Volts")),
        ("SENSE", ("High", None)),
        ("DWAKE", ("0", "Seconds")),
        ("DSHUTD", ("180", "Seconds")),
        ("DLOWBATT", ("2", "Minutes")),
        ("LOTRANS", ("196.0", "Volts")),
        ("HITRANS", ("253.0", "Volts")),
        ("RETPCT", ("15.0", "Percent")),
        ("ITEMP", ("30.6", "C")),
        ("ALARMDEL", ("Low Battery", None)),
        ("BATTV", ("27.6", "Volts")),
        ("LINEFREQ", ("50.0", "Hz")),
        ("LASTXFER", ("High line voltage", None)),
        ("NUMXFERS", ("0", None)),
        ("TONBATT", ("0", "Seconds")),
        ("CUMONBATT", ("0", "Seconds")),
        ("XOFFBATT", ("N/A", None)),
        ("SELFTEST", ("NO", None)),
        ("STESTI", ("336", None)),
        ("STATFLAG", ("0x0500000A", None)),
        ("DIPSW", ("0x00", None)),
        ("REG1", ("0x00", None)),
        ("REG2", ("0x00", None)),
        ("REG3", ("0x00", None)),
        ("MANDATE", ("07/13/99", None)),
        ("SERIALNO", ("GS9229021308", None)),
        ("BATTDATE", ("13/11/15", None)),
        ("NOMOUTV", ("230", "Volts")),
        ("NOMBATTV", ("24.0", "Volts")),
        ("EXTBATTS", ("0", None)),
        ("FIRMWARE", ("70.11.I", None)),
        ("END APC", ("2016-02-09 21:13:26 +0000", None)),
    ]
)
