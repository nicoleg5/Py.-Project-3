def make_choice(): #User inputs a letter to make a choice.

  print("Please select one of the following:")

  print("(a)  Find all Isis rectangles of the type n for a given n;")
  print("(b)  Find I_n for a given n;")
  print("(c)  Find I_n for n in a given range;")

  user_choice = input("Enter your choice here: ").lower()
  print()

  return (user_choice)


def choice_input(user_choice): #Asks for positive integers.

  if user_choice == 'a':
    print("Please enter a positive n value: ")
    one = int(input("n = "))
    print()
    print("List of Isis rectangles")
    print("--------------------------------")
    print([f"{rec[0]} X {rec[1]}" for rec in choice_a(one)])
  elif user_choice == 'b':
    print("Please enter a positive n value: ")
    two = int(input("n = "))
    choice_b(two)
  else:
    print("Please enter two positive integers for n1 and n2:")
    n1 = int(input("n1 = "))
    n2 = int(input("n2 = "))
    choice_c(n1, n2)


def choice_a(one):  #Returns a list of all Isis rectangles of type n.

  low = 2 * one + 1
  high = 4 * one
  list_rectangles = []

  for x in range(low, high+1):
    numerator = 2 * x * one
    denominator = x - 2 * one
    if numerator % denominator == 0:
      b = numerator // denominator
      list_rectangles.append((x, b))
  return(list_rectangles)


def choice_b(two):  #Returns the number of Isis rectangles of type n.
  
  lst = choice_a(two)
  print()
  print("There are %d Isis rectangles of type %d." %(len(lst), two))
  
  
def choice_c(n1, n2):   #Returns a chart of the number of Isis rectangles of type n, for n1 and n2.

  print()
  print("n\tNumber of Isis rectangles")
  print("----------------------------------")

  for z in range(n1, n2+1):
    lst = choice_a(z)
    print(f"{z}\t{len(lst)}")


x = make_choice()
choice_input(x)

