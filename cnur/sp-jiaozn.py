from urllib.request import urlopen
import re


url = "https://www.jiaozn.com/tupian/"

html = urlopen(url).read().decode('utf-8')


pattern = re.compile(r'<a href=".*" title="(.*)"><img class="thumbs r"')

title_str = re.findall(pattern, html)


date_str = re.compile(r'<i class="fa fa-clock-o" .* ((.*))&nbsp;&nbsp;&nbsp;<i class="fa fa-user"></i>')

title_str = re.findall(date_str, html)

print(date_str)