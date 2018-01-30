# -*- coding: utf-8 -*-

from urllib.request import urlopen

with urlopen('http://photo.vyidea.com') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text
        print(line)
        if 'EST' in line or 'EDT' in line: # look for Eastern Time
            print(line)
