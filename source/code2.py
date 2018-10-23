print("Type in as many integers as you want. When your list is complete, type 'done' or anything else that isn't an integer.")
n = 0
total = 0

while True:
    number = input("Integer:")
    try:
        number = int(number)
        while True:
            total = total + number
            n = n + 1
            def average(n, total):
                avg = (total/n)
                avg = str(avg)
                return avg 
            print("Average = " + average(n, total))
            break
    except: 
        if n == 0:
            print("If there are no numbers, there is no average.")
            break
        else:
            break

    def average(n, total):
        avg = total/n
        avg = str(avg)
        return avg   
