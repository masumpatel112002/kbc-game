# KBC game made by masum patel

qutions=[
        ["who is prime minister of india?","pm modi","bhupa bhai","emran khan","masum patel",1],
        ["which programing languages is use to web devloping?","html","java","c#","c",1],
        ["who is CEO of twitter?","ratan tata","elon musk","adani","muka kaka",2],
        ["which fildas is best for AI","mechenical","IC","civil","computer",4]
        ]

rs=[1000,2000,3000,5000]

print("Welcome to Masum's KBC")
print("select any option through number like for A select 1,B select 2,C select 3,D select 4\n")

for i in range(0,len(qutions)):
    qution=qutions[i]
    print(qution[0])
    print(f"{qution[1]}     {qution[2]}")
    print(f"{qution[3]}     {qution[4]}\n")
    ans=int(input("Enter answer between 1 to 4:-"))
    conform=input("Really your answer lock? y/n\n")

    if conform=="y":  
        if ans==qution[-1]:
            print(f"your answer is right you won rupees {rs[i]}\n")    
        else:
            print(f"your answer is wrong you win {rs[i-1]}\n") 
            break       
    else:
        print(qution[0])
        print(f"{qution[1]}     {qution[2]}")
        print(f"{qution[3]}     {qution[4]}\n")
        ans=int(input("Enter answer between 1 to 4:-"))
        conform=input("Really your answer lock? y/n\n")