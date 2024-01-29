# In computer science classes, we haven't taught try & except yet, but my knowledge is much greater than that of my classmates))
# (We have just started learning if/elif/else)

#Hi!
print("Maded by tiny_mauss")
print("-------------------")
print(" ")

def main():
  mark=input("Input your mark: ")

  try:
    m=int(mark)
    
    if m<=3:
      print("Beginner level")
      
    elif m<=6 and m>3:
      print("Middle level")

    elif m<=9 and m>6:
      print("Sufficient level")

    elif m>=10 and m<13:
      print("High level")

    else:
      print("You have a super high level, congratulations")

  except ValueError:
    main()
    return

main()
print("")
print("thx for using")
