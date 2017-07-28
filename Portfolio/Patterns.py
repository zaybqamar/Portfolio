#def AskInput():
FirstString = input("First string?")
SecondString = input("Second string?")
Width = int(input("Width?"))
#return(Width)

#AskInput()

LetterList = [FirstString]


def EvenWidth():
    if Width%2==0:
        print("even")
        for x in range(0, Width-1):
            LetterList.append(FirstString)
        print(LetterList)
        LetterList.pop(len(LetterList)-1)
        print(LetterList)

def OddWidth():
    if Width%2==1:
        print("odd")
        for x in range(0, Width-1):
            LetterList.append(FirstString)
        print(LetterList)
        for i in range(0,2):
            LetterList.pop(len(LetterList)-1)

        print(LetterList)




EvenWidth()
OddWidth()


#def CreateOutput(FirstString, SecondString, Width):
#    AskInput()
#    for x in range(0, Width):
#        print(FirstString)
