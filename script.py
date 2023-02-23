import json
import os
import sys
responseData=None
with open("output.json",'r') as f:
	responseData=json.load(f)
for i in responseData.keys():
	path=os.path.join(os.path.dirname(__file__),i)
	if i not in os.listdir():
		os.mkdir(path)
	for k in responseData.get(i):
		with open(path+f"/{k}.py","a") as f:
			f.write(responseData.get(i).get(k));

