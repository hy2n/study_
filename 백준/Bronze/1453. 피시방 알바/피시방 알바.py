answer = 0
user_size = int(input())
people_input = str(input())

seat = {}

for x in people_input.split(" "):
    val = int(x)
    if val in seat and (seat[val] == True):
        answer+=1
        continue
    seat[val] = True
print(answer)