import pyqrcode
import os
import binascii

# Generate QR-code
number_of_codes = 20

for i in range(number_of_codes):

    url_tmp = "https://chasquiwan.github.io/QR_Schatzsuche/stationen/{:>02}_station.html".format(i+1)
    url = pyqrcode.create(url_tmp)
    url.png('{:>02}_Station_QR.png'.format(i+1), scale=6)

# Merge QR-codes
command = 'montage'

for i in range(number_of_codes):
    command += ' -label {} {:>02}_Station_QR.png'.format(i+1, i+1)

command += ' -tile x4 -geometry +50+50 -pointsize 50  QR.png'
os.system(command)

# Generate markdown pages
textstring = """# Station {}

audio/{:>02}_station.mp3

[Hier gehts zum ersten Hinweis](#erster-hinweis)

[Hier gehts zum zweiten Hinweis](#zweiter-hinweis)\n

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

## Erster Hinweis

[Zurück](#station-{})

![](img/{:>02}_station_A.png)

[Zurück](#station-{})

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

## Zweiter Hinweis

[Zurück](#station-{})

![](img/{:>02}_station_B.jpg)

[Zurück](#station-{})

{{% include open_embed.html %}}"""

for i in range(number_of_codes):

    f = open('{:>02}_station.md'.format(i+1), 'w+')
    f.write(textstring.format(i+1, i+1, i+1, i+2, i+1, i+1, i+2, i+1))
    f.close()
