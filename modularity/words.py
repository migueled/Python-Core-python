#python words.py http://sixty-north.com/c/t.txt
import sys
from urllib.request import urlopen

def fetchWords(url):
    story = urlopen(url)
    storyWords = []
    for line in story:
        lineWords = line.decode('utf-8').split()
        for word in lineWords:
            storyWords.append(word)
    story.close
    return storyWords

def printItems(items):
    for item in items:
        print(item)

def main(url):
    words = fetchWords(url)
    printItems(words)

if __name__ == '__main__':
    main(sys.argv[1])