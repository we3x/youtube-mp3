import sys, getopt, os
from optparse import OptionParser

def download(link):
    os.system('youtube-dl --extract-audio --audio-format mp3 --output "%(title)s.%(ext)s" "' + link + '"')

def download_from_file(file):
    f = open(file)
    for line in f:
        download(line)


def main():
    parser = OptionParser()
    parser.add_option("-l", "--link", dest="link", help="download from link")
    parser.add_option("-f", "--file", dest="filename", help="download all links from file")
    (options, args) = parser.parse_args()
    if options.filename != None:
        download_from_file(options.filename)
    elif options.link != None:
        download(options.link)



if __name__ == "__main__":
    main()
