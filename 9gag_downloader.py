# @filename:9gag_downloader.py
# @usage: python 9gag_downloaded.py
# @author: YedaAnna
# @description: Downloads images from the 9gag.com Girl section 
# @version: 1.0 
# @date: Monday Jan 05 2015
import os
import sys
import urllib2
from bs4 import BeautifulSoup	
import urllib
import time
global base_link
global m
start=time.time()
base_link="http://9gag.com/girl/"

def images():
	base_contents=urllib2.urlopen(final_next_link).read()
	a=[]
	b=[]
	temp_file=open('temp_html.txt', 'w' )
	nextpage=open('nextpage.txt', 'w')
	html=base_contents
	parsed_html = BeautifulSoup(html)
	img=parsed_html.find_all('img')
	b=parsed_html.find_all("a", "btn badge-load-more-post")
	for index in b:
		nextpage.write(str(index)+"\n")
	for index in img:
		temp_file.write(str(index)+"\n")
	temp_file.close()
	nextpage.close() 
	process()

def links():
	for n in range(1,m+1):
		global final_next_link
		if n ==1:
			final_next_link= base_link
			images()
		else:
			new_link=open('nextpage.txt','r')
			for lines in new_link:
				coloumn=lines.split()
				nextlink=coloumn[7]
				nextlink=nextlink.replace('href="/girl/','')
				nextlink=nextlink.replace('">Load', '')
			final_next_link=base_link+nextlink
			images()

def process():	
	read_file=open('temp_html.txt', 'r')
	name=[]
	url=[]
	for lines in read_file:
		coloumn=lines.split()
		if len(coloumn) != 5:
			pass
		else:
			name_joined=''.join(coloumn[1]+coloumn[2])
			name.append(name_joined)
			url.append(coloumn[4])
	new_name=[]
	new_url=[]
	for j in range(len(name)):
		temp=name[j].replace('alt="', '')
		temp=temp.replace('"', '' )
		new_name.append(temp)
	for i in range(len(url)):
		temp2=url[i].replace('src=', '')
		temp2=temp2.replace('"', '')
		temp3=temp2.replace('>', '')
		new_url.append(temp3)
	for k in range(len(new_url)):
		urllib.urlretrieve(new_url[k], (new_name[k] +'.jpg'))
	read_file.close() 

print "Please enter no of pages to download"
m=int(input())

if os.path.exists(os.getcwd()+'/9gag_images/'):
	os.chdir(os.getcwd()+ '/9gag_images/')
else:	
	os.makedirs(os.getcwd()+'/9gag_images/')
	os.chdir(os.getcwd()+'/9gag_images/')	
links()
os.remove('temp_html.txt')
os.remove('nextpage.txt')
print "End of Program :)"
print "Time taken: " +str(time.time()-start)
