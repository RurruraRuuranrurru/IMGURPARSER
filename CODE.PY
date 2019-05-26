import string, random, urllib, os, thread, array, sys

if len(sys.argv) < 2:
    sys.exit("Usage: python " + sys.argv[0] + " (Number of threads)")
threadAmount = int(sys.argv[1])

noneWorking = ['0', '503', '4939', '4940', '4941', '12003', '5556', '5082']

def scrapePictures():
	amount =7
	while True:
		p1 = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(amount-amount/2)))
		p2 = str(''.join(random.choice(string.digits + string.lowercase) for _ in range(amount/2)))
		name = p1+p2
		link = "http://i.imgur.com/" + "" + str(name) + ".jpg"
		site = urllib.urlopen(link)
		meta = site.info()
		file_size=meta.getheaders("Content-Length")[0]
		if file_size in noneWorking:
			pass
		else:
			urllib.urlretrieve(""+ link, str(name) + ".jpg")
			print "[+] Valid: " + name +".jpg"

			
for i in range(threadAmount): 
	thread.start_new_thread(scrapePictures, ())
	print ("THREAD " +str(i+1) + " STARTED!")

while (True):
	pass
