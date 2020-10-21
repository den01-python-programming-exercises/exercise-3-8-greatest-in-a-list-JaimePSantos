def main():
    #write your code below this line
    intList = []
    max = 0
    while(True):
      number = int(input())
      if(number==-1):
        break
      intList.append(number)
      if(number>max):
        max = number
    print("The greatest number: " + str(max))

if __name__ == '__main__':
    main()
