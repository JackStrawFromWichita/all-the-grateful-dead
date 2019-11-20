from internetarchive import get_item
from internetarchive import download
from internetarchive import search_items
import time as t

#-----------------------------------------------------------------------------------------------------------------------

# START TIME OF JOB

start = t.time()

#-----------------------------------------------------------------------------------------------------------------------

# READ CSV FILE INTO LIST

f = open(r"H:\14000.csv") # PATH TO CSV FILE
x = f.readlines()
f.close()

with open(r"H:\14000.csv") as f:
    x = f.read().splitlines()

#-----------------------------------------------------------------------------------------------------------------------

# DOWNLOAD ALL 14000 GRATEFUL DEAD SHOWS AT ONCE

for a in x:
    download(a, verbose=True, glob_pattern='*.mp3', destdir=r"C:\Users\username\Desktop\gd") # LOCAL DIRECTORY TO SAVE FILES

#-----------------------------------------------------------------------------------------------------------------------

# END TIME OF JOB

end = t.time()
print('time to complete: ' + str((end - start) / 60) + ' minutes')

#-----------------------------------------------------------------------------------------------------------------------
