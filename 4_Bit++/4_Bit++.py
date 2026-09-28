statements = int(input(" "))
final_result = 0

if 1 <= statements <= 150:
    for i in range(statements):
        operation = input("")
        answer = []
        answer.append(operation)
        for j in answer:
            operation = j.split()
            for x in operation:
                if x.count("+") == 2:
                    final_result = final_result + 1
                elif x.count("-") == 2:
                    final_result = final_result - 1
else:
    print("Error")

print(final_result)
    