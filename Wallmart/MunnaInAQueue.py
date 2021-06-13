

def main():
    n=int(input())
    queue=list(map(str,input().split()))
    query=int(input())
    while query:
        choice=list(map(str,input().split()))
        if choice[0]=="A":
            queue.pop(0)
        if choice[0]=="B":
            x,y=choice[1],choice[2]
            try:
                index=queue.index(y)
                queue.insert(index+1,x)
            except ValueError:
                pass
        if choice[0]=="C":
            vip=choice[1]
            queue.insert(0,vip)
        query-=1
    print(queue)
main()
            
