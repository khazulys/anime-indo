from requests import Session
from bs4 import BeautifulSoup as bs
import urllib.request
from threading import Thread as td
from time import sleep

class animeindo:
	def __init__(self, episod):
		self.res = Session()
		self.episod = int(episod)
		self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5320 (KHTML, like Gecko) Chrome/40.0.855.0 Mobile Safari/5320'}
		self.url = f"https://anime-indo.link/boruto-naruto-next-generations-episode-{self.episod}/"

	def links(self):
		r = self.res.get(self.url, headers=self.headers, allow_redirects=True)
		soup = bs(r.text, 'html.parser')
		link = 'https://anime-indo.link' + soup.iframe.get("src")
		return link

	def download(self):
		s = self.res.get(self.links(), headers=self.headers)
		sb = bs(s.text, 'html.parser')
		links = sb.source.get("src")
		urllib.request.urlretrieve(links, 'vid.mp4')
		print('\nSuccess')
		exit(0)
		
	def animated(self):
		t = td(target=self.download)
		t.start()
		while t.is_alive():
			for i in "-\|/-\|/":
				print(f'\rDownloading {i}',end="",flush=True)
				sleep(0.1)
				
main = animeindo(237)
main.animated()