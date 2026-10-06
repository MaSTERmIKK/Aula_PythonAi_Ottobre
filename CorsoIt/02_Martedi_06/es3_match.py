eta = int(input())
maggiorenne = eta >= 18

if maggiorenne == True:
    eta = "maggiorenne"
else:
    eta = "minorenne"

match eta:
    case "maggiorenne":
        print("puoi vedere il film")
    case "minorenne":
        print("NON puoi vedere il film")
        
        
x = input()
y = input()

scelta = input()

match scelta:
    case "addizione":
        print(x+y)
    case "moltiplicazione":
        print(x*y)
    case "sottrazione":
        print(x-y)
    case "divisione":
        if y == 0:
            print("non si può")
        else:
            print(x/y)
            