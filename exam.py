'''
#while ...else
counter = 5

while counter != 0 :
  print(counter)
  counter -= 1
  if counter == 1:
    break;
else:
  print("while ended without a break")

print("while was ended")
'''
'''
# global vs local
# assign
# parameter
# global


a = 1

def increase():
  a += 1
  print(a)

increase()

#print(a)
'''

#input returns a str, no need for casting


# not a == b is not efficient!!
# always use a != b

'''
# return boolean
def is_valid():
  return True

while is_valid():
  user_input = input("give me your password")
'''
