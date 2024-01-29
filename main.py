#Hi!
print("Maded by tiny_mauss")
print("-------------------")
print(" ")

def main():
  mark=input("Введіть вашу оцінку: ")

  try:
    m=int(mark)
    
    if m<=3:
      print("Початковий рівень")
      
    elif m<=6 and m>3:
      print("Середній рівень")

    elif m<=9 and m>6:
      print("Достатній рівень")

    elif m>=10 and m<13:
      print("Високий рівень")

    else:
      print("У вас надвисокий рівень, вітаю")

  except ValueError:
    main()
    return

main()
print("")
print("thx for using")
