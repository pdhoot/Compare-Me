#!/usr/bin/python
import argparse
import urllib
import threading
from bs4 import BeautifulSoup



parser = argparse.ArgumentParser(description='compare some users')
parser.add_argument('user1')
parser.add_argument('user2')
parser.add_argument('--spoj' , action='store_true')
args = parser.parse_args()

def scrapUserDataSpoj(username):
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

def main_spoj(user1 , user2):
	t1 = threading.Thread(target=scrapUserDataSpoj , args=(user1,))
	t2 = threading.Thread(target=scrapUserDataSpoj , args=(user2,))
	t1.start()
	t2.start()

if args.spoj is True:
	main_spoj(args.user1 , args.user2)

