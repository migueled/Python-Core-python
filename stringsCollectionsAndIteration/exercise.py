from urllib.request import urlopen
story = urlopen( 'http://sixty-north.com/c/t.txt' )
storyWords = []
for line in story:
    #lineWords = line.split()
    lineWords = line.decode( 'utf8' ).split()
    for word in lineWords:
        storyWords.append( word )

story.close()
storyWords