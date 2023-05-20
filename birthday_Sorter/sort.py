def is_lesser(t1,t2):
    if(int(t1[2])<int(t2[2])):
        return True
    elif(int(t1[2])==int(t2[2])):
        if(int(t1[1])<=int(t2[1])):
            return True
    return False

f=open('/Users/arnavbalpande/Desktop/12_projects/birthday_Sorter/birthdays.txt','r')
b_tuples=[]
for line in f:
    if(line=="end"):
        break
    else:
        line=line.replace(' ','')
        line=line.replace(':','/')
        line_list=list(line.split('/'))
        line_list[3]=line_list[3][0:-1]
        b_tuples.append(tuple(line_list))
#sort Logic
for i in range(len(b_tuples)):
    for j in range(len(b_tuples)-i-1):
        if( not is_lesser(b_tuples[j],b_tuples[j+1])):
             temp=b_tuples[j]
             b_tuples[j]=b_tuples[j+1]
             b_tuples[j+1]=temp
           
print(b_tuples)
f.close()
f=open("sorted_birthdays.txt",'w')
for t in b_tuples:
    t='/'.join(t)
    t=t.replace('/',':',1)
    print(t)
    f.write(t+'\n')