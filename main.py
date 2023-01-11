count = 1

while count <= 5:
  mark = int(input("Enter mark : "))
  print(mark)

  if mark > 75:
    print("A")
  elif mark >= 65:
    print("B")
  elif mark >= 55:
    print("C")
  elif mark >= 45:
    print("S")
  else:
    print("F")

  count += 1