# pythonskillsharedownload
download skillshare tool.... i dont know who runs the api, but it gets results..


So basically install the script, either clone dir using git, or copy and paste into a .py file

run the code by either double clicking, or in cmd:
python skill.py [skillshare_url] [y or n for if you want mp4]

if you select no, it will download as m3u8, which needs vlc and wifi to play, but use nearly no space.

if you select yes, it will download using ffmpeg, so you must have that installed.



# automate has been addded

replace the string variable with HTML and it will auto parse the html to find the skillshare links and downloads as mp4
packages:
pip install bs4
pip install lmxl
