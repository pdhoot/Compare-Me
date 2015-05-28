import urllib
import threading
from bs4 import BeautifulSoup
from sys import argv , stderr , exit

def scrapUserData(username):
	url = 'http://www.spoj.com/users/' + username
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)
	div1 = soup.find('div' , {'class':'col-md-3'})
	paragraphs = div1.find_all('p')
	user = div1.find('h4')
	data = user.text + '\n'
	dl = soup.find('dl' , {'class':'dl-horizontal profile-info-data profile-info-data-stats'})
	dd = dl.find_all('dd')
	data=data + paragraphs[2].text + '\n'
	data = data + 'Prbolems Solved : ' + dd[0].text + '\n'
	data = data + 'Solutions Submitted : ' + dd[1].text + '\n'
	print data

if len(argv)!=3:
	try:
		raise TypeError()
	except:
		print >>stderr , 'usage: python spoj.py user1 , user2'
		exit(1)
t1 = threading.Thread(target=scrapUserData , args=(argv[1],))
t2 = threading.Thread(target=scrapUserData , args=(argv[2],))
t1.start()
t2.start()
