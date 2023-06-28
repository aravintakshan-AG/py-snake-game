from fil import *
def instr():
      c={1:"green",2:"yellow",3:"orange",4:"purple",5:"white",6:"pink"}
      print("-----------------------------------------------------------------------------------------------------------------------")
      print("||                                      INSTRUCTION OF GAME                                                          ||")
      print("-----------------------------------------------------------------------------------------------------------------------")
      print("keys to move the snake:")
      print(" 1.for forward press 'upparrow' or 'w'\n 2.for backward press 'backarrow' or 's'\n"
            " 3.for left press 'leftarrow' or 'a'\n 4.for right press 'rightarrow' or 'd'")
      print("rules:-")
      print(" 1.eat the apple 'red block'\n 2.dont touch ur own snake body\n 3.dont hit by the blue block")
      print("for score:-")
      f=input("if you want to see score enter 'yes':")
      if f=="yes" or f=="YES":
            sco=pri()
            print("the score is:")
            print(sco)
      print("for start:-")
      na=input("enter your name:")
      print("choose the colour from the list")
      print("colour list are",c)
      col=eval(input("enter the colour number from the list:"))
      le=eval(input("select level speed 1 to 3 :"))
      sp=eval(input("select level 1 to 2 : "))
      st=input("ENTER START TO START THE GAME:")
      return c[col],st,na,le,sp