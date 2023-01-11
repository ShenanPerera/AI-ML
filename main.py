count = 1 
max_mark = 0
min_mark = 100
average = 0
total = 0

while count <= 10:
  marks  = int(input("Enter marks : "))
  if max_mark < marks:
    max_mark = marks

  if min_mark > marks :
    min_mark = marks
    
  total = total + marks
  count = count + 1
  
average = total / 10

print ("maximum mark : " , max_mark)
print ("minimum mark : " , min_mark)
print ("average mark : " , average)