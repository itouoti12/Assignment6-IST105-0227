import sys
import random

num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]
num4 = sys.argv[4]
num5 = sys.argv[5]

if num1.isnumeric() and num2.isnumeric() and num3.isnumeric() and num4.isnumeric() and num5.isnumeric():

    if int(num1) < 0 or int(num2) < 0 or int(num3) < 0 or int(num4) < 0 or int(num5) < 0:
        print("<h1>must all args type are positive values</h1>")

    else:
        summary = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
        average = summary / 5
        print(f"<h2>summary is {summary}</h2>")
        print(f"<h2>average is {average}</h2>")

        print(f"<p>logical operation of average:{average}</p>")
        if average > 50:
            print("<div>average is greater than 50.</div>")
        else:
            print("<div>average is lower than 50.</div>")
        
        # uses bitwise operation to determine if the count of positive numbers is even or odd
        print(f"<p>bitwise operation of summary:{summary}</p>")
        if summary & 1 :
            print("<div>the count of args is Odd.</div>")
        else:
            print("<div>the count of args is Even.</div>")
        
        print("<p>sorted list</p>")
        data_list = [10, 43, 18, 22, 55, 90, 100, 32, 68, 13]
        print(f"<div>Original Values:{data_list}</div>")
        data_list.sort()
        print(f"<div>Sorted Values:{data_list}</div>")

else:
    print("<h1>must all args type are numeric values</h1>")
