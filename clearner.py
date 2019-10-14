
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(trackingfol):
            i = 1
            if filename != 'kaustubh':
                 try:
                    updatedname = filename
                    ext = 'noname'
                    try:
                        ext = str(os.path.splitext(trackingfol+ '\\' + filename)[1])
                        path = extensionfol[ext]
                    except Exception:
                        ext = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    date=now.strftime("%d")

                    folderdest = extensionfol[ext]
                    
                    yeare = False
                    monthe = False
                    datee = False
                    for folderyear in os.listdir(extensionfol[ext]):
                        if folderyear == year:
                            folderdest = extensionfol[ext] + "\\" +year
                            yeare = True
                            for folmonth in os.listdir(folderdest):
                                if month == folmonth:
                                    folderdest = extensionfol[ext] + "\\" + year + "\\" + month
                                    monthe = True
                                    for foldate in os.listdir(folderdest):
                                        if date == foldate:
                                            folderdest = extensionfol[ext] + "\\" + year + "\\" + month + "\\" + date
                                            datee = True
                    if not yeare:
                        os.mkdir(extensionfol[ext] + "\\" + year)
                        folderdest = extensionfol[ext] + "\\" + year
                    if not monthe:
                        os.mkdir(folderdest + "\\" + month)
                        folderdest = folderdest + "\\" + month
                    if not datee:
                        os.mkdir(folderdest + "\\" + date)
                        folderdest = folderdest + "\\" + date


                    file_exists = os.path.isfile(folderdest + "\\" + updatedname)
                    while file_exists:
                        i += 1
                        updatedname = os.path.splitext(trackingfol+ '\\' + filename)[0] + str(i) + os.path.splitext(trackingfol+ '\\' + filename)[1]
                        updatedname = updatedname.split("\\")[4]
                        file_exists = os.path.isfile(folderdest + "\\" + updatedname)
                    src = trackingfol+ "\\" + filename

                    updatedname = folderdest + "\\" + updatedname
                    os.rename(src, updatedname)
                 except Exception:
                     print(filename)
extensionfol = {
    #PDF
    '.pdf' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\PDF",
    #Execution
    '.exe' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Applications",
    #Word
    '.docx' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\Word",
    '.doc' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\Word",
    '.odt' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\Word",
    #Text
    '.txt' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text",
    #Presentation
    '.ppt' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\PPT",
    '.pptx' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\PPT",
    '.odp' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\PPT",
    #Video
    '.avi' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Video",
    '.mkv' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Video",
    '.mov' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Video",
    '.mp4' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Video",
    '.mpg' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Video",
    '.mpeg' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Video",
    #Audio
    '.mp3' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Audio",
    '.wav' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Media\\Audio",
    #Images
    '.bmp' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Images",
    '.gif' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Images",
    '.jpg' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Images",
    '.jpeg' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Images",
    '.png' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Images",
    '.svg' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Images",
    #Compressed
    '.zip' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Compressed",
    #Excel
    '.xlsx' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\Excel",
    '.csv' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\Excel",
    '.xls' : "C:\\Users\\kaustubh\\Desktop\\kaustubh\\Text\\Microsoft\\Excel"

}



trackingfol = 'C:\\Users\\kaustubh\\Downloads'
folder_destination = 'C:\\Users\\kaustubh\\Desktop\\kaustubh'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, trackingfol, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
