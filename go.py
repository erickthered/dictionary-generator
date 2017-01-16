#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import string
import sys
import getopt

alphabet = list(string.printable)
alphabet = alphabet[0:-5] + [u"á", u"é", u"í", u"ó", u"ú", u"Á", u"É", u"Í", u"Ó", u"Ú", u"ñ", u"Ñ", u"ü", u"Ü"]

def md5(string):
    m = hashlib.md5()
    m.update(string.encode('utf8'))
    return m.hexdigest()


def isLastPossibleWord(currentWord):
    return currentWord == alphabet[-1] * len(currentWord)


def getIncrementPosition(currentWord):
    i = len(currentWord) - 1
    while currentWord[i] == alphabet[-1]:
        i -= 1
    return i


def nextWord(currentWord):
    newWord = currentWord
    length = len(currentWord)
    addChar = False
    if length == 0:
        newWord = alphabet[0]
    else:
        addChar = isLastPossibleWord(currentWord)
        if addChar:
            newWord = alphabet[0] * (length+1)
        else:
            newIndex = alphabet.index(currentWord[length-1]) + 1
            if newIndex >= len(alphabet):
                incrementIndex = getIncrementPosition(currentWord)
                newIndex = alphabet.index(currentWord[incrementIndex]) + 1
                prefix = currentWord[0:incrementIndex]
                suffix = alphabet[0] * (length - incrementIndex - 1)
                newWord = prefix + alphabet[newIndex] + suffix
            else:
                newWord = currentWord[0:length-1] + alphabet[newIndex]

    return newWord

def main(argv):
    i = 1
    n = None
    opts, args = getopt.getopt(argv, "n:")
    for opt, arg in opts:
        if opt == '-n':
            if int(arg) > 0:
                n = int(arg)
    if n:    
        startWord = alphabet[0] * n
        endWord = alphabet[len(alphabet) - 1] * n
        word = startWord
        print word,"\t",md5(word)

        while word != endWord:
            word = nextWord(word)
            print word,"\t",md5(word)
            i += 1

        print str(i) + " Words"
    else:
        print "Usage: "
        print "\t", sys.argv[0], " -n <number>"
        print "  where: "
        print "\t-n\tLength of words to be generated"
        print "  example: "
        print "\t",sys.argv[0], " -n 1"

if __name__ == "__main__":
    main(sys.argv[1:])