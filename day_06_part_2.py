with open('day_06_input.txt') as f:
    answers = f.readlines()

i = 0
no_of_answers = 0
while i < len(answers):
    
    answer = ''
    people = 0

    while i < len(answers) and answers[i] != '\n':
        answer += answers[i]
        i += 1
        people += 1
    
#    i += 1
    
    answer_index = 0
    checklist = []
    while answer_index < len(answer) and answer[answer_index] != '\n':
        checklist.append(answer[answer_index])
        answer_index += 1

    checklist_index = 0

#    print(checklist)
#    print(answer)
    while checklist_index < len(checklist):

        if( answer.count(checklist[checklist_index])  == people ):
            no_of_answers += +1
            
        checklist_index += 1

    i += 1

print(no_of_answers)