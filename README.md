9gag image downloader scripts
====

1. 9gag_downloader.py

This script downloads images from the specified 9gag section(default is 'Girl' section)

The user specifies the number of pages to read and the script downloads the images present on the page

Typically a page has about 8-10 images on it

The script will also rename the images to match the title of the image post

2. 9gag_specific_celeb_downloader.py

This script will search for the desired celeb (default is Emma Watson.. obviously :)

The user specifies the number of pages to search 

The script Downloads only those images that match the searched celebrity



The script uses [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#) module

If it is not installed, you can install it by via terminal
$ pip install beautifulsoup4

Any improvements, suggestions are most welcome

P.S Script is working as of January 2015



