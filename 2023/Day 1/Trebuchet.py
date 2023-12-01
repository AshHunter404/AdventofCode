# open input file
fn = "day1input.txt" 
f = open(fn,'r')
txt = f.read().split("\n")

#extracts digits from string containing digits and letters - no special characters
di = [v.translate(str.maketrans('', '', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')) for v in txt[:-1]]
#print(len(di))

# print first and last digit and those added together to form a new value
#for i in range(len(di)):
#    print("first digit: {}, last digit: {}, value: {}".format(di[i][0], di[i][-1], di[i][0] + di[i][-1]))

dil = sum( [int(p[0] + p[-1]) for p in di] )
print(dil)
