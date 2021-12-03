import time

"""
Thanks for using Replit for Advent of Code!

Here are a few tips:

1. To install packages, just import them and Replit will install them for you, or click on the cube in the sidebar to install manually.
2. If you're stuck, try using the debugger in the sidebar shaped like a play/pause button.
3. When you're done, you can share your project by clicking the project name and then "Publish"
3.a When you share your project, use the #adventofcode hashtag!
4. Have fun, and good luck!
"""


"""
Place your question data into the data.txt file.
You may need to parse the data!
"""
with open('data.txt') as f:
    change = [line.rstrip() for line in f]


if __name__ == "__main__":
  replit_start_time = time.perf_counter()
  """
  Run your functions here.
  This code won't be run if imported.
  """

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




  # Keep this line at the end of your code
  
replit_end_time = time.perf_counter()
print("Elapsed time:", replit_end_time - replit_start_time)