#-----------------------------------------------------------------------
# This python script watches for new files in the folder "wav_files".
# When there is a new file, the python script "send-to-pd.py" is launched.
# Code inspired from:
# https://pythonhosted.org/watchdog/quickstart.html#quickstart (simple example)
# https://stackoverflow.com/questions/18599339/python-watchdog-monitoring-file-for-changes
#
__author__      = "Anna Xambo"
__date__        = "March 15 2018"
__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

import os
import subprocess
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from threading import Timer

class ChangeHandler(FileSystemEventHandler): # testing events
    def on_any_event(self, event):
        print(event)

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print "Created!"
        t = Timer(10.0, ticktack)
        t.start()
    # def on_modified(self, event):
    #     print "Modified!"
    #     t = Timer(10.0, ticktack)
    #     t.start()

def ticktack():
    print "tick tack 2"
    subprocess.Popen(["python", "send-to-pd.py"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else 'wav_files'
    event_handler = LoggingEventHandler()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
