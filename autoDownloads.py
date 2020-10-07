from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time

class MyHandler(FileSystemEventHandler):
    i = 1

# The following block works as the observer event. - When a change is observed in the downloads folder, it will convert the filename to lowercase & grab the file extension for each file (everything following '.').
    # After grabbing the extension, it will compare the ext to all of the ones found in each specific folder. If the Ext is not found in the array, it will skip to the next. If NO match
    # is found, it will leave the file in the downloads folder (odds are these are one-off programs / installers and can be deleted by the user on their own.

    def on_modified(self, event):
        try:
            for filename in os.listdir(downloads_PATH):
                filen = filename.lower()
                file_ext = '.'+filen.split(".")[-1]
                for folder in folder_exts:
                    for ext in folder:
                        if file_ext == ext:
                            src_dest = downloads_PATH+slash+filename
                            new_dest = folder_PATH[folder_exts.index(folder)]+slash+filename
                            os.rename(src_dest,new_dest) # Renames the file's path to the proper folder's name
                            break
                        else:
                            pass
        except:
            pass

slash = '\ '.replace(' ','') # setting up small variable to allow a '\' to be used alone.

# These arrays are the possible extensions that could be found based on what folder they should go through. Used on (line 18, 38)

docu_ext = ['.doc','.docx','.html','.htm','.odt','.pdf','.xls','.xlsx','ods','.ppt','.pptx','.txt','.xls','.xlsx','.xlsb','.xlsm','.docx','.rtf','.csv']
pic_ext = ['.png','.jpg','.tif','.bmp','.gif','.eps','.raw', '.cr2', '.nef', '.orf', '.sr2','.tiff','.jpeg']
vid_ext = ['.mp4', '.m4a', '.m4v', '.f4v', '.f4a', '.m4b', '.m4r', '.f4b', '.mov','.3gp', '.3gp2', '.3g2', '.3gpp', '.3gpp2','.webm','.flv','.avi','.hdv']
music_ext = ['.mp3','.wav','.aac','.ac3','.wma','pcm']
folder_exts = [docu_ext, pic_ext,vid_ext,music_ext]

# These are the paths to each specific folder. More can be added if needed.

downloads_PATH = r'<insert PATH>' # Downloads folder default path
documents_PATH = r'<insert PATH>'
pictures_PATH = r'<insert PATH>'
videos_PATH = r'<insert PATH>'
music_PATH = r'<insert PATH>'
folder_PATH = [documents_PATH,pictures_PATH,videos_PATH,music_PATH]

# This tells the observer which folder to watch (downloads) and starts the observer.

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, downloads_PATH, recursive=True)
observer.start()

# This try statement keeps the observer watching the folder.

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()