import sys,os
import importlib
dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)

import settings

def run_notify():
    for i in settings.NOTIFY_TYPE:
        modulename,claname=i.rsplit(".", 1)
        print(modulename,claname)
        mod=importlib.import_module(modulename)
        cla=getattr(mod,claname)
        obj=cla()
        obj.send()






