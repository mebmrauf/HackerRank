# https://www.hackerrank.com/challenges/designer-pdf-viewer

def designerPdfViewer(h, word):
    maxHeight = max([h[ord(alpha)-ord('a')] for alpha in word])
    return maxHeight*len(word)