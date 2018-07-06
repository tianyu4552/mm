#coding:utf-8
import urllib
from bs4 import BeautifulSoup

page = urllib.urlopen('https://www.vmei.com/nca-12-1.html');
htmlcode = page.read();
soup = BeautifulSoup(htmlcode, "html.parser")
# pageFile = open('pageCode.html','w')#以写的方式打开pageCode.txt
# pageFile.write(htmlcode)#写入
# pageFile.close()