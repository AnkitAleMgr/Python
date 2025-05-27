import traceback

def amount_multiplier(amount):
    
    if amount == 0:
        amount += 1000
    else:
        amount *= 2
    
    return amount


questions = ("What language are you using " , "Where is great wall of china located ", "What color is the sky ")
correct_answers = ("Python" , "China", "Blue")
options =("(Python, Java, JavaScript, HTML)","(Nepal, India, China, Pakistan)", "(Red, Blue, Green, Yellow)") 

try:
    amount = 0
    
    for i in range(len(questions)):
        question = questions[i]
        correct_ans = correct_answers[i]
        option = options[i]
        
        choice = input(question + option + ": \n> ").title()
        
        if choice == correct_ans:
            print("Correct ans")
            amount = amount_multiplier(amount)
            print("your current amount is " + str(amount) + "\n" )
        else:
            print("Incorrect ans")
            print("your current amount is " + str(amount) + "\n" )
            
    print("Your final amount is :", amount)
    
except:
    traceback.print_exc()