import subprocess
import sys
import os

cwd = os.getcwd()

infolder = cwd + "\inputs"
outfolder = cwd + "\outputs"
print (infolder + " -> " + outfolder)
print("Input complete file extension that should replace current file extension(dont include the period. Example: 'aiff', not '.aiff'")
fex = input()

wavfiles = os.listdir(infolder)
def convert_one_file(inputpath, outputpath):
    command = f"ffmpeg -n -i {inputpath} -write_id3v2 1 -c:v copy {outputpath} -loglevel 1"
    res = subprocess.Popen((command))
    res.wait()
    
total_files = len(wavfiles)
global filenumber
filenumber = 0

for file in wavfiles:
    new_filename = '.'.join(file.split(".")[:-1]) + "." + fex
    new_filepath = f'"{outfolder}\{new_filename}"'
    old_filepath = f'"{infolder}\{file}"'
    convert_one_file(inputpath=old_filepath, outputpath=new_filepath)
    filenumber += 1
    sys.stdout.write('\r' + (f">>>>>>>>>{filenumber}/{total_files} files finished converting."))
    sys.stdout.flush()

