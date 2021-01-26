## this block of code is taken from (https://realpython.com/working-with-files-in-python/) tutorial
import os
import shutil
#src = 'C:\\Users\\tcl\\tsract_exp\\Bengali.traineddata'
#dest = 'C:\\Program Files\\Tesseract-OCR\\tessdata'
#shutil.copy(src, dest)

filenames = os.listdir('C:\\Program Files\\Tesseract-OCR\\tessdata')
print(filenames) # check that the file is added in this directory which was not present before.
