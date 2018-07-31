#boggle submission

#Intro
print('Welcome to the lovely game of boggle\nPlease select a grid size')
 
#Grid Size
def Setup():
    BoardRow = input ('Please input a row length: ')
    BoardCol = input ('Please input a column length: ')
    Grid = int(BoardRow) * int(BoardCol)
    MaxLengthOfWord = Grid
    print('Grid size selcted: ', BoardRow,'x',BoardCol)
    return MaxLengthOfWord

MaxLengthOfWord = Setup()

#Randomiser
#TBC

#Grid Search

#All words found
Words = ['cat','what','bat','guidance','bll','a','ab','abc']

#Words found is true
#pip3 install pyenchant
def WordIsTrue():
    import enchant
    WordsChecked =[]
    d = enchant.Dict("en_GB")
    for Word in Words:
        if int(len(Word)) >=3:       
            if d.check(Word) is True:
                WordsChecked.append(Word)
    return WordsChecked

WordsChecked = WordIsTrue()

#All words letter length as list
def TotWordLen():
    TotWordLength = []
    a=0
    for Word in WordsChecked:
        lenofword = int(len(WordsChecked[a]))
        a+=1
        TotWordLength.append(lenofword)
    return TotWordLength

ListLenWords = TotWordLen()

#Scoring Dictionary
def ScoreTable():
    lenword = [i for i in range(1,int(MaxLengthOfWord)+1)]
    score = [i for i in range(int(MaxLengthOfWord)-1)]
    score.insert(0,0)
    ScoreTable = (dict(zip(lenword,score)))
    return ScoreTable

ScoreTable = ScoreTable()

#Wordscore
def WordScore():
    WordScore = []
    for no in ListLenWords:
        x = (ScoreTable.get(no))
        WordScore.append(x)
    return WordScore

#Result
Total = sum(WordScore())
result = {
    "score": Total,
    "words": WordsChecked
}

print(result)

