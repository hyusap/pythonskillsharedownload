import requests, json, re, os, sys

if len(sys.argv) == 1:
	url = input("url? ")
	
elif len(sys.argv) == 2: 
	url = sys.argv[1]
	mp4 = input("mp4 y or n")
else:
	url = sys.argv[1]
	mp4 = sys.argv[2]

id = re.findall("\d\d\d+", url)[0]
print(id)
api = requests.get("https://skillshare-flask.herokuapp.com/get_videos_list/"+id)
#print(api.text)
y = json.loads(api.text)
print()
list = y["video_list"]
for i in list:
	vid = i["video_url"]
	print(vid)
	if mp4 == "y":
		os.system(f"ffmpeg -i {vid} -c copy -bsf:a aac_adtstoasc {i['file_name'].replace(' ', '')}.mp4")
	else:
		os.system(f"wget -O {i['file_name'].replace(' ', '')}.m3u8 {vid}")
