#!/usr/bin/env python3

import sys
from pypdf import PdfReader
from gtts import gTTS


def main():
    infile = sys.argv[1]
    outfile = infile.split('.')[0] + '.mp3'

    reader = PdfReader(infile)
    text = ''
    for i in range(0, len(reader.pages)):
        text += reader.pages[i].extract_text()
    
    tts = gTTS(text)
    tts.save(outfile)


if __name__ == '__main__':
    main()
