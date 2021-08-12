def AnswerReveal(CurrentAnswer, Answers, AttemptAnswer):
    for i in range(len(Answers)):
        if(AttemptAnswer == Answers[i]):
            CurrentAnswer = CurrentAnswer[:i] + Answers[i] + CurrentAnswer[i + 1:]

    return CurrentAnswer

def AnswerStarOut(Answer):
    CurrentAnswer = ""
    for i in range(len(Answer)):
        Answer = list(Answer)
        Answer[i] = "*"
        CurrentAnswer = "".join(Answer)    

    return CurrentAnswer

def AnswerCheck(Answers, AttemptAnswer):
    if(AttemptAnswer == Answers):
        return True

    for i in range(len(Answers)):
        if(AttemptAnswer == Answers[i]):
            return True
    return False

def main():
    GameOver = False
    Answer = "spoon"
    Answer = Answer.upper()
    NumberOfAttempts = 6

    CurrentAnswer = AnswerStarOut(Answer)

    while(NumberOfAttempts != 0 or GameOver == True): 
        print(f"current Answer is: {CurrentAnswer}")
        print(f"Number of Trys: {NumberOfAttempts}")


        AttemptAnswer = input("Enter Answer here: ")
        AttemptAnswer = AttemptAnswer.upper()
        RightOrWrong = AnswerCheck(Answer, AttemptAnswer)
        
        CurrentAnswer = AnswerReveal(CurrentAnswer, Answer, AttemptAnswer)

        if(RightOrWrong == True):
            if(AttemptAnswer == Answer):
                GameOver = True
                print("\n")
                print(f"The Answer is - {Answer}")
                break
            elif(CurrentAnswer == Answer):
                GameOver = True
                print("\n")
                print(f"The Answer is - {Answer}")
                break
            else: 
                continue
        elif(RightOrWrong == False): 
            NumberOfAttempts = NumberOfAttempts - 1 
            continue
        
        if(NumberOfAttempts == 0):
            GameOver = True
            print("\n")
            print(f"The Answer is - {Answer}")
            break
    
    print("\n")
    if(GameOver == True):
        print("You have won the Game")
    else:
        print("you have used all your trys please try again")

        

main()