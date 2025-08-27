import re
from urllib.request import urlopen

url = input('Type URL: ')
page = urlopen(url)
#https://en.wikipedia.org/wiki/Hurricane_Irene_(2005)?scrlybrkr=e3b74d72
#https://en.wikipedia.org/wiki/Short_(crater)

#this link will not work for the body. It reads the first <p> </p> tag, and ends there. keep trying to find a way around this.
#https://en.wikipedia.org/wiki/Hydrogen
#https://www.scottmorris.com/services.html

html_bytes = page.read()
html = html_bytes.decode("utf-8")

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)

body_index = html.find("<div>")
start_index = body_index + len("<div>")
end_index = html.find("</div>")
body = html[start_index:end_index]
body = re.sub("<.*?>", "", body)
print(body)
