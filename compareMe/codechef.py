import urllib
import threading
from bs4 import BeautifulSoup

def ScrapeUserData(username):
	url = 'http://www.codechef.com/users/' + username
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)
	table = soup.find('table' , {'class':'rating-table'})
	td = table.find_all('td')
	string = """
			Rank				Rating
	Long		%s			%s
	Short		%s 			%s
	LTime(All)	%s			%s	

	""" % (td[4].text , td[5].contents[0] , td[7].text , td[8].contents[0] , td[10].text , td[11].contents[0])

	name = soup.find('div' , {'class':'user-name-box'})
	print
	print ' '*7 ,  name.text
	print string

def main(user1 , user2):
	t1 = threading.Thread(target=ScrapeUserData , args=(user1,))
	t2 = threading.Thread(target=ScrapeUserData , args=(user2,))
	t1.start()
	t2.start()

