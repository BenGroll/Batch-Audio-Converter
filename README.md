# Batch-Audio-Converter

# What does it do?
This script allows you to batch-convert a list of audiofiles into another file type, e.g: a Folder full of .wav files can be converted into a Folder of .aiff files using just a single command.

# Requirements:
python has to be installed

ffmpeg has to be installed

How to install FFMPEG on Windows
https://www.wikihow.com/Install-FFmpeg-on-Windows

How to install FFMPEG on Mac
run *brew install ffmpeg* in your terminal

How to install FFMPEG on Linux
run *sudo apt install ffmpeg* in your terminal

# type *ffmpeg -version* in your terminal to check if its installed

# USAGE
1. Clone this repo or download and unpack the zip
2. Copy all your original files into the "inputs" folder (back them up somewhere else before using the converter in case something goes wrong
3. In the repo directory open a terminal/cmd
4. In the terminal type 'python convert.py' and press Enter
5. You will be asked to input the file extension you want the future files to have. E.g. aiff,
  Note that you should not include the leading period in the extension, e.g.: type 'aiff', not '.aiff'
6. Press Enter. The Script will now process all your files, displaying progress. DONT CLOSE THE SCRIPT WHILE ITS RUNNING
