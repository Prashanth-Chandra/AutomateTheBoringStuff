import shelve
import pyperclip
import sys

clip = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower == 'save':
        clip[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower == 'delete':
        del clip[sys.argv[2]]

if len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        pyperclip.copy(str(clip.keys()))
    else:
        try:
            pyperclip.copy(str(clip[sys.argv[1]]))
        except:
            pyperclip.copy("ERROR : The keyword does not exist")
clip.close()