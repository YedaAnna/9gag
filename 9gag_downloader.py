# @filename:9gag_downloader.py
# @usage: python 9gag_downloader.py
# @author: YedaAnna
# @description: Downloads images from the 9gag.com Girl section
# @version: 2.0
# @date: Monday Jan 05 2015
import os
import urllib2
from bs4 import BeautifulSoup
import urllib
import time
global base_link, page_input
start = time.time()
# to download from other sections, change the section name ex '/cosplay'
section = '/girl'
base_link = "http://9gag.com"


def list_images():
    global name, url, img, nextpage_link
    base_contents = urllib2.urlopen(final_next_link).read()
    parsed_html = BeautifulSoup(base_contents)
    img = parsed_html.find_all("img", "badge-item-img")
    nextpage_link = parsed_html.find_all("a", "btn badge-load-more-post")
    name = []
    url = []
    for link in img:
        name.append(link.get('alt'))
        url.append(link.get('src'))
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
    for i in range(len(name)):
        urllib.urlretrieve(url[i], (name[i] + '.jpg'))

print "Please enter number of pages to download"
page_input = int(input())

if not os.path.exists(os.getcwd() + '/9gag_images/'):
    os.makedirs(os.getcwd() + '/9gag_images/')
os.chdir(os.getcwd() + '/9gag_images/')
find_links()
print "End of Program :)"
print "Time taken: " + str(time.time() - start)
