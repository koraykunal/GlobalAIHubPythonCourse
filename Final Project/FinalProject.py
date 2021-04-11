
questions = ["What color is banana ? : ", "What is the combination of all colors ? : ", "What is the satellite of world ? : ",  # soruları ve cevapları listede tanımladım
            "What would be your brother's father's mother-in-law ? : ", "What is the largest planet in the solar system ? : ",    
            "What is the land surrounded by seas on all four sides ? : ", "Which is the largest country in terms of area ? : ",
            "What is the fastest growing plant ? : ", "Who is the first to prove that the earth is round ? : ", "It is a field of study covering artificial neural networks and similar machine learning algorithms : "]

answers = ["Yellow","White","Moon","Grandmother","Jupiter","Island","Russia","Bamboo","Macellan","Deep Learning"]   
k=0            # doğur cevap sayısını ölçmek için bir değişken tanımladım
joker=1        # joker hakkı tanımladım

print("---------Welcome to the 'WHO WANTS TO BE A MILLIONAIRE'---------")
print("Rules" + "\n" + "* There are 10 questions and they all have one correct answer." +
      "\n" + "* Write the answer but pay attention to capitalization." +
      "\n" + "* You have one JOKER card. You can use the joker by typing the 'joker'. Use it carefully!" +
      "\n" + "Good luck")


for i in range(len(questions)):                                            # soru sayısı kadar döngüye girmesini istiyorum for loop açtım.
    print("")
    print("Question {}: ".format(i+1))
    print("\n" + "*"*40)
    comAnswer = input(questions[i])
    
    if (comAnswer ==answers[i] ):                                          # cevaplarımın doğru mu yanlış mı olduğunu kontrol eden bi if mekanizması yazdım.
        print("Congratulations, Right")        
        k +=1
    elif (comAnswer.lower() == "joker"):                                   # farklı olarak birşey eklemek istedim ve kullanıldığında bilemese dahi soruyu doğru kabul edecek bir joker kartı ekledim
        if joker == 1:
            print("You answered the question correctly using the joker.")
            print("Answer: {}".format(answers[i]))
            joker -= 1
            k += 1
        elif joker < 1:
            print("Sorry, you have no any joker!")
    elif (comAnswer != answers[i] ):
        print("Ups. Wrong answer, it was: {}".format(answers[i]))
if (k>=5):
    print("")
    print("Wow, You have successfully completed the competition. You got {} questions right".format(k))
else:
    print("")
    print("Sorry, you failed. You got {} questions right".format(k))