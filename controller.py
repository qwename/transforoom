# This file is in the public domain.

import os
import logging
import time
import sys
from datetime import datetime

logging.basicConfig(filename='controller.log',level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

EXEVERS=False

def main():
    if sys.platform.startswith('win'):
        if EXEVERS:
            status = os.system("\"server.exe\" 2>> error.log")
        else:
            status = os.system("\"server.py\" 2>> error.log")
    else:
        status = os.system("python server.py")
    logging.info("Server stopped with a status code of: "+str(status))
    #             Windows               Linux
    if str(status)=="5" or str(status)=="1280":
        print str(datetime.today())+" [Controller] Server stopped."
        os._exit(0)
    elif str(status)=="10" or str(status)=="2560":
        print str(datetime.today())+" [Controller] Server restarted."
        status=""
        main()
    elif str(status)=="11" or str(status)=="2816":
        print str(datetime.today())+" [Controller] Server restarted to clear error log."
        if sys.platform.startswith('win'):
            os.system("del error.log")
        else:
            os.system("rm ./error.log")
        status=""
        main()
    elif str(status)=="12" or str(status)=="3072":
        print str(datetime.today())+" [Controller] Delayed restart. Restarting in 10 minutes."
        time.sleep(600)
        status=""
        main()
    elif str(status)=="13" or str(status)=="3328":
        print str(datetime.today())+" [Controller] Delayed restart. Restarting in 5 minutes."
        time.sleep(300)
        status=""
        main()
    elif str(status)=="14" or str(status)=="3584":
        print str(datetime.today())+" [Controller] Delayed restart. Restarting in 20 minutes."
        time.sleep(1200)
        status=""
        main()
    elif str(status)=="15": #Unused
        if EXEVERS:
            print str(datetime.today())+" [Controller] Transformice Server.exe missing."
        else:
            print str(datetime.today())+" [Controller] Transformice Server.py missing."
        time.sleep(10)
        status=""
        main()
    elif str(status)=="16" or str(status)=="4096":
        print str(datetime.today())+" [Controller] Kikoo.swf missing."
        time.sleep(10)
        status=""
        main()
    elif str(status)=="17" or str(status)=="4352":
        print str(datetime.today())+" [Controller] dbfile.sqlite empty/missing."
        time.sleep(10)
        status=""
        main()
    elif str(status)=="18": #Does not apply to linux
        print str(datetime.today())+" [Controller] uptime.exe missing."
        time.sleep(10)
        status=""
        main()
    elif str(status)=="19" or str(status)=="4864":
        if EXEVERS:
            print str(datetime.today())+" [Controller] Controller.exe renamed."
        else:
            print str(datetime.today())+" [Controller] Controller.py renamed."
        time.sleep(10)
        status=""
        main()
    elif str(status)=="20" or str(status)=="5120":
        #Server update.
        print str(datetime.today())+" [Controller] Server restarted for update."
        if EXEVERS:
            os.system("del \"Transformice Server.exe\"")
            os.system("rename \"UPDATE.DAT\" \"Transformice Server.exe\"")
        else:
            if sys.platform.startswith('win'):
                os.system("del \"Transformice Server.py\"")
                os.system("rename \"UPDATE.DAT\" \"Transformice Server.py\"")
            else:
                os.system("rm ./Transformice\\ Server.py")
                os.system("mv ./UPDATE.DAT ./Transformice\\ Server.py")
        status=""
        main()
    elif str(status)=="256":
        if not sys.platform.startswith('win'):
            print "A problem was found in the configuration, attempting to fix..."
            os.system("sudo touch /etc/authbind/byport/443")
            os.system("sudo chown administrator:administrator /etc/authbind/byport/443")
            os.system("sudo chmod 755 /etc/authbind/byport/443")
            print "Restart Controller.py and see if it works."
            os._exit(0)
        else:
            print str(datetime.today())+" [Controller] Server crashed, restarting in 10 seconds."
            time.sleep(10)
            status=""
            main()
    elif str(status)=="50":
        print str(datetime.today())+" [Controller] Invalid Name/Key."
        if sys.platform.startswith('win'):
            os.system("cmd")
        os._exit(0)
    elif str(status)=="51":
        print str(datetime.today())+" [Controller] Validation Failure."
        if sys.platform.startswith('win'):
            os.system("cmd")
        os._exit(0)
    elif str(status)=="52":
        print str(datetime.today())+" [Controller] Unable to connect to validation server."
        if sys.platform.startswith('win'):
            os.system("cmd")
        os._exit(0)
    elif str(status)=="53":
        print str(datetime.today())+" [Controller] Misc validation failure."
        if sys.platform.startswith('win'):
            os.system("cmd")
        os._exit(0)
    else:
        print str(datetime.today())+" [Controller] Server crashed, restarting in 10 seconds."
        time.sleep(10)
        status=""
        main()

if __name__ == '__main__':
    main()
