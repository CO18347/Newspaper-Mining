import re

# for this we need to have file called combined.txt which will have all the links from which we
# need to extract thedata from.

with open("./Combined.txt",'r') as f:
	x = f.read()
	x = x.split()
	for link in x:
		link = link.split("/")[-1]
		# link = link.split("_")
		link  = link.replace("_", " ").upper()
		link = link.replace("JUL ", "JULY ")
		link = link.replace("JUN ", "JUNE ")
		ans = re.findall(r"([0-3]{0,}[0-9].*2020)", link)
		print(ans[0])