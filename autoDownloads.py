from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time

class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for filename in os.listdir(downloads_PATH):
            filen = filename.lower()
            file_ext = '.'+filen.split(".")[-1]
            for folder in folder_exts:
                for ext in folder:
                    if file_ext == ext:
                        src_dest = downloads_PATH+slash+filename
                        new_dest = folder_PATH[folder_exts.index(folder)]+slash+filename
                        os.rename(src_dest,new_dest)
                        break
                    else:
                        pass

slash = '\ '.replace(' ','')

docu_ext = ['.doc','.docx','.html','.htm','.odt','.pdf','.xls','.xlsx','ods','.ppt','.pptx','.txt','.xls','.xlsx','.xlsb','.xlsm','.docx','.rtf','.csv']
pic_ext = ['.png','.jpg','.tif','.bmp','.gif','.eps','.raw', '.cr2', '.nef', '.orf', '.sr2','.tiff','.jpeg']
vid_ext = ['.mp4', '.m4a', '.m4v', '.f4v', '.f4a', '.m4b', '.m4r', '.f4b', '.mov','.3gp', '.3gp2', '.3g2', '.3gpp', '.3gpp2','.webm','.flv','.avi','.hdv']
music_ext = ['.mp3','.wav','.aac','.ac3','.wma','pcm']
folder_exts = [docu_ext, pic_ext,vid_ext,music_ext]

downloads_PATH = r'C:\Users\best.jonathan\Downloads' # Downloads folder default path
documents_PATH = r'C:\Users\best.jonathan\Documents'
pictures_PATH = r'C:\Users\best.jonathan\Pictures'
videos_PATH = r'C:\Users\best.jonathan\Videos'
music_PATH = r'C:\Users\best.jonathan\Music'
folder_PATH = [documents_PATH,pictures_PATH,videos_PATH,music_PATH]

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, downloads_PATH, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()