import requests, json, re, os, sys, shutil
from bs4 import BeautifulSoup


loop = 1
string = """html"""
soup = BeautifulSoup(string, "lxml")
links = soup.select("a")
alreadydone = []
for link in links:
	try:
		linkhref = link.get("href")
		if re.findall("\d\d\d+", linkhref)!=[] and re.findall("classes", linkhref)!=[] and re.findall("\d\d\d+", linkhref)[0] not in alreadydone:
			#os.mkdir(link.getText().replace(" ", "-"))
			id = re.findall("\d\d\d+", linkhref)[0]
			print(id)
			api = requests.get("https://skillshare-flask.herokuapp.com/get_videos_list/"+id)
			y = json.loads(api.text)
			list = y["video_list"]
			if loop > 34:
				os.mkdir("video"+str(loop))
				for i in list:
					vid = i["video_url"]
					print(vid)
					os.system(f"ffmpeg -i {vid} -c copy -bsf:a aac_adtstoasc -f mp4 {i['file_name'].replace(' ', '')}.mp4")
					#os.system(f"move {i['file_name'].replace(' ', '')}.mp4 {link.getText().replace(' ', '-')}")
					os.system(f"move {i['file_name'].replace(' ', '')}.mp4 video{str(loop)}")
			loop += 1
			alreadydone.append(id)
	except KeyboardInterrupt:
		raise
	except:
		print(f"the id {id} failed")
