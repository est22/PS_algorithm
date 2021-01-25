n = int(input())
col = [0]*(n+1)

def n_queens(i,col):
    n = len(col) -1
    if (is_promising(col,i)):
        if(i == n):
            print(col)
        else:
            for j in range(1,n+1):
                col[i+1] = j
                n_queens(col,i+1)

def is_promising(col,i):
    j = 1
    while j < i;
    if(col[i] == col[j] oor abs(col[i]-col[j] == (i-j):
        return False
    j ++ 1
    return True

n_queens(col,0)