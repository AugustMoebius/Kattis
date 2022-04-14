#https://open.kattis.com/problems/speeding

n = int(input())
input() # Burn off useless 0 0 input
top_speed = 0
total_distance = 0
time = 0
for i in range(0, n-1):
    x = input()
    split = x.split(" ")
    distance = int(split[1])    
    cur_time = int(split[0])
    current_speed = int((distance - total_distance)/(cur_time - time))
    time = cur_time
    total_distance = distance
    if (current_speed > top_speed):
        top_speed = current_speed

print(top_speed)
