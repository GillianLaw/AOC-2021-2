import time


with open('data.txt') as f:
    change = [line.rstrip() for line in f]


if __name__ == "__main__":
  replit_start_time = time.perf_counter()
 

distance = 0
deep = 0
aim = 0

for i in change:
 
  if i[0] == 'f':
      distance += int(i[-1:]) 
     
      if aim >= 0:
          deep += aim * int(i[-1:])
      # else:
      #     deep -= aim * int(i[-1:])
  elif i[0] == 'u':
      deep -= int(i[-1:]) 
      aim -= int(i[-1:]) 
  elif i[0] == 'd':
      deep += int(i[-1:]) 
      aim += int(i[-1:])

 


print('distance', distance)
print('deep', deep)
print(aim)
print((deep - aim) * distance)




 
  
replit_end_time = time.perf_counter()
print("Elapsed time:", replit_end_time - replit_start_time)