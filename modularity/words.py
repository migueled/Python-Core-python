#python words.py http://sixty-north.com/c/t.txt
#python
#import words
#help(words)
"""retrieve and print words from a URL.
Usage:
    python3 words.py <url>
"""
import sys
from urllib.request import urlopen

def fetchWords(url):
    """Fecth a list of words from a URL
    Args:
        url: the url of a UTF-8 text document.
    
    Returns:
        a list of strings containing the words from
        the document.
    """
    story = urlopen(url)
    storyWords = []
    for line in story:
        lineWords = line.decode('utf-8').split()
        for word in lineWords:
            storyWords.append(word)
    story.close
    return storyWords

def printItems(items):
    """Print items one per line
    Args:
        an iterable series of printable items.
    """
    for item in items:
        print(item)

def main(url):
    """Print each word from a text documents from at a url
    Args:
        url: the url of a UTF-8 text document.
    """
    words = fetchWords(url)
    printItems(words)

if __name__ == '__main__':
    main(sys.argv[1])