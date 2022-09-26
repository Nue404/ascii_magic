import ascii_magic
import argparse
import sys

try :
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='path', help='example : yourpath/img.png')

    arg = parser.parse_args()
    img = arg.path
    if not arg.path:
        sys.exit('Masukin path gambarnya cok\nContoh: ascii.py -p yourpath/img.png')
        
    nuexploit = ascii_magic.from_image_file(img)
    ascii_magic.to_terminal(nuexploit)
    print('Succes Convert Image To ASCII Art\nVisit: nuexploit.or.id')
except Exception as error:
    print('Error nih!', error)