class Solution:
    
    class line:
        
        def getSpaces(self,size):
            s = ''
            for i in range(size):
                s += ' '
            return s
        
        def __init__(self,words,maxWidth):
            self.words = words
            self.maxWidth = maxWidth
            
        def leftJustified(self):
            s = ''
            for word in self.words:
                s += word
                s += ' '
            s = s[:-1]
            s += self.getSpaces(self.maxWidth-len(s))
            return s    
            
            
        def __str__(self):
            #3) lets list all the requirements:
            #1-If there's just a single word we return it leftJustified
            #2-If there's an even number of spaces to be distributed we do that.
            #3-Otherwise we have to split the number of spaces evenly
            #initially I coded 2 and 3 seperately just to make my life easier, but it meant 
            #more if/else statements, now as you can see it is all condensed in one for loop
            if len(self.words) == 1:
                return self.leftJustified()
            totalWordsLength = 0
            for word in self.words:
                totalWordsLength += len(word)
            spaceCount = len(self.words) - 1
            widthToSplit = self.maxWidth - totalWordsLength
            s = ''
            for i in range(len(self.words)):
                word = self.words[i]
                s += word
                if i != len(self.words)-1:
                    s += self.getSpaces(widthToSplit//spaceCount)
                    # here's where the magic happens, the first check is to see if there's an uneven distribution of spaces
                    # the 2nd check helps us achieve the "even distribution", this was the hardest thing to come up with in this problem.
                    if widthToSplit % spaceCount and i < (widthToSplit % spaceCount): 
                        s += ' '
            return s
                    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        lines = []
        currLineWords = []
        currLineWidth = 0
        #1) I started with this part of the code which breaks down the string into "lines"
        # following the rules proposed by the question.
        # using a class to store the lines helps alot with the code quality.
        for word in words:
            if currLineWidth + len(word) <= maxWidth:
                currLineWords.append(word)
                currLineWidth += len(word) + 1
            else:
                lines.append(self.line(currLineWords,maxWidth))
                currLineWords = []
                currLineWidth = 0
                currLineWords.append(word)
                currLineWidth += len(word) + 1
        if currLineWords:
            lines.append(self.line(currLineWords,maxWidth))
        
        #2) Then we just have to "print" each line with the requirements provided, I created a custom
        # __str__ method for that & a custom .leftJustified function for the last line which is left justified.
        out = []
        for i in range(len(lines)-1):
            out.append(str(lines[i]))
        out.append(lines[len(lines)-1].leftJustified())
            
        return out