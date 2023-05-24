# flac2alac_ffmpeg
This is a simple script written with the assistance of AI in Python.

**Please backup all files before executing any type of conversion script, I am not responsible for you losing your files**

It bulk converts FLAC files into ALAC files for iPod and other media devices.

You will need to install Python & FFMPEG to your computer and ensure that both are accessable from the Terminal/CMD

## Install Links
[ffmpeg](https://ffmpeg.org/)

  &nbsp;&nbsp;&nbsp;&nbsp;[ffmpeg documentation](https://ffmpeg.org/documentation.html)
  
[python for Windows](https://www.python.org/downloads/windows/)

[python for MacOS](https://www.python.org/downloads/macos/)

[python for Other Platforms](https://www.python.org/download/other/)

---

### Script in motion

Use the `python3 flac2alac.py` command in terminal, you will be prompted to enter the path of the folder where your FLAC files reside. [^1]
  
  <img width="602" alt="ss01" src="https://github.com/HH-Point/flac2alac_ffmpeg/assets/63919543/9e99b4be-32eb-43dd-98cf-6b10ab4c1bad">

**script running**

  <img width="602" alt="ss03" src="https://github.com/HH-Point/flac2alac_ffmpeg/assets/63919543/97cbffe2-86df-4d53-a1b7-3cf1091a20c0">
  
**script completed**

  <img width="558" alt="ss04" src="https://github.com/HH-Point/flac2alac_ffmpeg/assets/63919543/4ff726b1-7aee-4521-ae60-ab7fe4ae87d2">

Files are auto placed inside a subdirectory called *ALAC* which ensures easy organization. [^2]

  <img width="739" alt="Screenshot 2023-05-24 at 9 41 38 AM" src="https://github.com/HH-Point/flac2alac_ffmpeg/assets/63919543/cfa94dfa-a9be-4054-b407-08acda3cc03d">


[^1]: Ensure you are in the same directory as where you are keeping the file | ex: `/Users/HH-Point/Downloads/flac2alac.py`
[^2]: I'm still working on getting ffmpeg to pass along metadata correctly from the original files, sadly I'm running into errors where not everything is getting passed in conversion. I recommend using a tool like [MusicBrainz Picard](https://picard.musicbrainz.org/) to ensure you're getting metadata for your music, I find this to be more reliable than most other methods
