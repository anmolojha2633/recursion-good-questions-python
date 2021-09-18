def toh(n,start,end,help):
    if n==1:
        print("move disk",n, "from" ,start,"to",end )
        return
    toh(n-1,start,help,end)
    print("move disk ",n, "from ",start, "to ",end)
    toh(n-1,help,end,start)
    



            #  so beilive the hypothesis that this function will give you 
    
             #number of ways in which n disks will get  placed to their desired destinations

start=1;
end=3;
help=2;
n=3;
toh(n,start,end,help)
