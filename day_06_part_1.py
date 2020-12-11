with open('day_06_input.txt') as f:
    answers = [line.rstrip() for line in f]

i = 0
no_of_answers = 0
while i < len(answers):
    
    checklist = []
    answer = answers[i]

    while i < len(answers) and answers[i] != '':
        answer += answers[i]
        i += 1

    answer_index = 0
    while answer_index < len(answer):
        
        if(answer[answer_index] not in checklist):
            no_of_answers += +1
            checklist.append(answer[answer_index])
            
        answer_index += 1

    i += 1

print(no_of_answers)