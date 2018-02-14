g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print("| ", g[0], "  | ", g[1], "  | ", g[2], "  | ", g[3], "  |")
print("____________________________")
print("| ", g[4], "  | ", g[5], "  | ", g[6], "  | ", g[7], "  |")
print("____________________________")
print("| ", g[8], "  | ", g[9], " | ", g[10], "| ", g[11], "  |")
print("____________________________")
print("| ", g[12], " | ", g[13], " | ", g[14], " | ", g[15], " |")
print("____________________________")
i = 0
x = 0
y = 0
z = 0
while (i < 8):
    while (x < 4):
        print("player 1:")
        p1 = int(input("Enter the first square:"))
        p2 = int(input("Enter the second square:"))

        if ((p1 == p2 + 1 or p1 == p2 - 1 or p1 == p2 + 4 or p1 == p2 - 4) and (
                            (p1 != 4 or p2 != 5) and (p1 != 8 or p2 != 9) and (p1 != 12 or p2 != 13) and (
                        p1 != 5 or p2 != 4) and (
                            p1 != 9 or p2 != 8) and (p1 != 13 or p2 != 12)) and (
                g[p1 - 1] != "X" and g[p2 - 1] != "X")):

            g[p1 - 1] = "X"
            g[p2 - 1] = "X"
            print("| ", g[0], "  | ", g[1], "  | ", g[2], "  | ", g[3], "  |")
            print("____________________________")
            print("| ", g[4], "  | ", g[5], "  | ", g[6], "  | ", g[7], "  |")
            print("____________________________")
            print("| ", g[8], "  | ", g[9], " | ", g[10], "| ", g[11], "  |")
            print("____________________________")
            print("| ", g[12], " | ", g[13], " | ", g[14], " | ", g[15], " |")
            print("____________________________")



        else:
            for l in range(4, 12):
                if (g[l] != g[l + 1] or g[l] != g[l - 1] or g[l] != g[l + 4] or g[l] != g[l - 4]):
                    z = z + 1

            if (z >= 8):
                print("Try again")

                z = 0
                continue



            else:
                if (x > y):
                    print("Player 1 wins")
                    exit(0)
                else:
                    print("Player 2 wins")
                    exit(0)

        x = x + 1
        i = i + 1
        break

    while (y < 4):
        print("player 2:")
        p1 = int(input("Enter the first square:"))
        p2 = int(input("Enter the second square:"))

        if ((p1 == p2 + 1 or p1 == p2 - 1 or p1 == p2 + 4 or p1 == p2 - 4) and (
                            (p1 != 4 or p2 != 5) and (p1 != 8 or p2 != 9) and (p1 != 12 or p2 != 13) and (
                        p1 != 5 or p2 != 4) and (
                            p1 != 9 or p2 != 8) and (p1 != 13 or p2 != 12)) and (
                g[p1 - 1] != "X" and g[p2 - 1] != "X")):

            g[p1 - 1] = "X"
            g[p2 - 1] = "X"
            print("| ", g[0], "  | ", g[1], "  | ", g[2], "  | ", g[3], "  |")
            print("____________________________")
            print("| ", g[4], "  | ", g[5], "  | ", g[6], "  | ", g[7], "  |")
            print("____________________________")
            print("| ", g[8], "  | ", g[9], " | ", g[10], "| ", g[11], "  |")
            print("____________________________")
            print("| ", g[12], " | ", g[13], " | ", g[14], " | ", g[15], " |")
            print("____________________________")




        else:
            for m in range(4, 12):
                if (g[m] != g[m + 1] or g[m] != g[m - 1] or g[m] != g[m + 4] or g[m] != g[m - 4]):
                    z = z + 1

            if (z >= 8):
                print("Try again")

                z = 0
                continue
g=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print ("| ",g[0],"  | ",g[1],"  | ",g[2],"  | ",g[3],"  |")
print ("____________________________")
print ("| ",g[4],"  | ",g[5],"  | ",g[6],"  | ",g[7],"  |")
print ("____________________________")
print ("| ",g[8],"  | ",g[9]," | ",g[10],"| ",g[11],"  |")
print ("____________________________")
print ("| ",g[12]," | ",g[13]," | ",g[14]," | ",g[15]," |")
print ("____________________________")
i=0
x=0
y=0
z=0
while (i<8) :
  while (x<4):
    print ("player 1:")
    p1 = int(input("Enter the first square:"))
    p2 = int(input("Enter the second square:"))

    if ((p1==p2+1 or p1==p2-1 or p1==p2+4 or p1==p2-4) and((p1!= 4 or p2 != 5)and(p1 != 8 or p2 != 9)and(p1 != 12 or p2 != 13) and (p1 != 5 or p2 != 4) and (
        p1 != 9 or p2 != 8) and (p1 != 13 or p2 != 12))and( g[p1-1]!="X" and g[p2-1]!="X")):


        g[p1 - 1] = "X"
        g[p2 - 1] = "X"
        print ("| ",g[0],"  | ",g[1],"  | ",g[2],"  | ",g[3],"  |")
        print ("____________________________")
        print ("| ",g[4],"  | ",g[5],"  | ",g[6],"  | ",g[7],"  |")
        print ("____________________________")
        print ("| ",g[8],"  | ",g[9]," | ",g[10],"| ",g[11],"  |")
        print ("____________________________")
        print ("| ",g[12]," | ",g[13]," | ",g[14]," | ",g[15]," |")
        print ("____________________________")



    else :
      for l in range (4,12):
        if (g[l] != g[l+1]  or g[l] != g[l-1] or g[l] != g[l+4]  or g[l] != g[l- 4] ):
           z=z+1





      if (z>=8):
          print ("Try again")

          z=0
          continue



      else:
        if (x>y ):
          print ("Player 1 wins")
          exit(0)
        else :
          print ("Player 2 wins")
          exit (0)


    x = x + 1
    i = i + 1
    break


  while(y<4):
    print("player 2:")
    p1 = int(input("Enter the first square:"))
    p2 = int(input("Enter the second square:"))

    if ((p1==p2+1 or p1==p2-1 or p1==p2+4 or p1==p2-4) and ((p1!= 4 or p2 != 5)and(p1 != 8 or p2 != 9)and(p1 != 12 or p2 != 13) and (p1 != 5 or p2 != 4) and (
        p1 != 9 or p2 != 8) and (p1 != 13 or p2 != 12))and (g[p1-1]!="X" and g[p2-1]!="X")):

        g[p1 - 1] = "X"
        g[p2 - 1] = "X"
        print ("| ",g[0],"  | ",g[1],"  | ",g[2],"  | ",g[3],"  |")
        print ("____________________________")
        print ("| ",g[4],"  | ",g[5],"  | ",g[6],"  | ",g[7],"  |")
        print ("____________________________")
        print ("| ",g[8],"  | ",g[9]," | ",g[10],"| ",g[11],"  |")
        print ("____________________________")
        print ("| ",g[12]," | ",g[13]," | ",g[14]," | ",g[15]," |")
        print ("____________________________")




    else:
      for m in range(4,12):
        if (g[m] != g[m + 1] or g[m] != g[m - 1] or g[m] != g[m + 4] or g[m] != g[m - 4]):
          z=z+1


      if (z >=8):
        print ("Try again")

        z=0
        continue


      else :
        if (x > y ):
          print ("Player 1 wins")
          exit(0)
        else:
          print ("Player 2 wins")
          exit(0)


    y=y+1
    i = i + 1
    break
print ("Player 2 wins")






            else:
                if (x > y):
                    print("Player 1 wins")
                    exit(0)
                else:
                    print("Player 2 wins")
                    exit(0)

        y = y + 1
        i = i + 1
        break
print("Player 2 wins")



