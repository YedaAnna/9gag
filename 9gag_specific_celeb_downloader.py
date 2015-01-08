# @filename:9gag_specific_celeb_downloader.py
# @usage: python 9gag_specific_celeb_downloader.py
# @author: YedaAnna
# @description: Downloads specifed celebrity images from the 9gag.com Girl section
# @version: 1.0
# @date: Thursday Jan 08 2015
import os
import urllib2
from bs4 import BeautifulSoup
import urllib
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
global base_link, page_input, newlist, ind, j
start = time.time()
# to download from other sections, change the section name ex '/cosplay'
section = '/girl'
base_link = "http://9gag.com"
# change celeb to name of desired celebrity Ex Olivia Wilde or simply Emma
# watch out for typos & Letter cases,
# Generally the first letter of bothwords is in Upper case
celeb = 'Emma Watson'
j = 0


def list_images():
    global name, url, img, nextpage_link, newlist, newurl
    base_contents = urllib2.urlopen(final_next_link).read()
    parsed_html = BeautifulSoup(base_contents)
    img = parsed_html.find_all("img", "badge-item-img")
    nextpage_link = parsed_html.find_all("a", "btn badge-load-more-post")
    name = []
    url = []
    ind = []
    newlist = []
    newurl = []
    for link in img:
        name.append(link.get('alt'))
        url.append(link.get('src'))
    for names in name:
        if celeb in str(names):
            ind.append(name.index(names))
    for index in ind:
        newlist.append(name[index])
        newurl.append(url[index])
    download_images()


def find_links():
    for n in range(1, page_input + 1):
        global final_next_link
        if n == 1:
            final_next_link = base_link + section
            list_images()
        else:
            for link in nextpage_link:
                nextpage = link.get('href')
            final_next_link = base_link + nextpage
            list_images()


def download_images():
    for i in range(len(newlist)):
        global j
        urllib.urlretrieve(newurl[i], (newlist[i] + '_' + str(j) + '.jpg'))
        j += 1

print "Please enter number of pages to search for " + str(celeb)
page_input = int(input())

if not os.path.exists(os.getcwd() + '/9gag_images/'):
    os.makedirs(os.getcwd() + '/9gag_images/')
os.chdir(os.getcwd() + '/9gag_images/')
if not os.path.exists(os.getcwd()+'/'+celeb):
    os.makedirs(os.getcwd()+'/'+celeb)
os.chdir(os.getcwd()+'/'+celeb)
find_links()
print "End of Program :)"
print "Time taken: " + str(time.time() - start)
