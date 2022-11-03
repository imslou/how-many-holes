#magic toeplitz
#   1 2 3 4 5
#   4 5 1 2 3
#   2 3 4 5 1
#   5 1 2 3 4 
#   3 4 5 1 2 = 15
#
# solve for n x n = n

example = [1,2,3,4,5
          ,4,5,1,2,3
          ,2,3,4,5,1
          ,5,1,2,3,4
          ,3,4,5,1,2]
          
def concat(*args):
    return "".join([str(x) for x in [*args]])

def answer(n):
    return sum([i for i in range(1,n+1)])

def generate(n): 
    sqr = []
    tile = [i for i in range(1,n+1)]
    for y in range(0,n):
        i = y+1
        e=[]
        for x in range(0,n):
            #THIS IS THE FUCKING MAGIC SAUCE MAKE IT WORK AUUUUUUUU.mp3 https://www.youtube.com/watch?v=CelgqNnv0wU
            i = i + 1 if i < n-1 else 0
            e.append(tile[i])
            sqr.append(tile[i]) #example[(n*y)+x]
        print(">>>>",concat(e))
    return sqr
  
def test(n):
    print("============ Testing =================")
    print("Expected answer for square of", n, "is", answer(n))
    sqr = generate(n)
    
    rd = 0
    row=[]
    col=[]
    left_diagonal=[]
    right_diagonal=[]
    
    for y in range(0,n):
        
        r=[]
        c=[]
        for x in range(0,n):
            r.append(sqr[(n*y)+x])
            c.append(sqr[(n*x)+y])
        
        row.append(r)
        col.append(c)
        left_diagonal.append(sqr[(n*y)+y])
        right_diagonal.append(sqr[rd+(n-1)])
        rd = rd+(n-1)
        
    print("check diagonals:")
    print(left_diagonal, sum(left_diagonal))
    print(right_diagonal, sum(right_diagonal))
    print("check rows:")
    for check in range(0,n):
        print(row[check], sum(row[check]))
    print("check cols:")
    for check in range(0,n):
        print(col[check], sum(col[check]))

n=5              
test(n)
