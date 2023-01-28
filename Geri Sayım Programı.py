program = True
while program == True:

  x = int(input("Geri sayımını yapmak istediğiniz bir tam sayı giriniz."))

  print("Sayımız", x)

  while x > -1 :
    print(x)
    x = x - 1
  print("Geri Sayım Sona Erdi.")
