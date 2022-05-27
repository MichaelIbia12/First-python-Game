actions =  ["run", "block","attack","jump"]
closeRange = 400
x =30
enemyAction = ""

counter = 0

while True:
    if x == 400:
        enemyAction = actions[2]
        print("\n"+enemyAction+"\n")
    else:
        x += 10
    counter += 1
       
    if counter % 3  == 0:
        print("\nblock\n")

    
    print(counter)