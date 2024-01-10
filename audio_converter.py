import subprocess
import os
import sys



print("Input complete path of folder that contains input files")
inp = input()
infolder = r"" + inp
print("Input complete path of folder that will contain output files")
out = input()
outfolder = r"" + out
print("Input complete file extension that should replace current file extension(include the period. Example: '.aiff'")
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
    new_filename = file[:-3] + fex
    new_filepath = f'"{outfolder}\{new_filename}"'
    old_filepath = f'"{infolder}\{file}"'
    convert_one_file(inputpath=old_filepath, outputpath=new_filepath)
    filenumber += 1
    sys.stdout.write('\r' + (f">>>>>>>>>{filenumber}/{total_files} files finished converting."))
    sys.stdout.flush()

