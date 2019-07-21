from bs4 import BeautifulSoup
from os import listdir
f = open('outputs.html', 'w')
f.write('''
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
    <style>
      body {
        font-family: 'Segoe UI', 'Calibri', sans-serif;
        width: 50em;
        margin: 4em;
      }
    
      pre {
        font-family: 'consolas', 'monaco', monospace;
      }
    </style>
  </head>
<body>
''')
for filename in listdir('files'):
  html_doc = open('files/' + filename, 'rb')
  soup = BeautifulSoup(html_doc, 'html.parser')
  asm = soup.find(id = 'assignment_show')
  f.write(asm.prettify())
  print(filename, 'is processed')
f.write('''
</body>
</html>
''')
f.close()
print('done!')