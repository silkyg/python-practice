import functools

l = [1,2,3,4,5]

#return new numbers which are 1+ of each number in the list
def method_map(lst):
    m = map(lambda x:x+1, lst)
    return m

k = method_map(l)

print ("map result ->", end=' ')
for i in k :
    print (i,  end= ' ')

# find the sum of all the numbers from the list
def method_reduce(lst):
    return functools.reduce(lambda a,b:a+b, lst)

r = method_reduce(l)
print ("\nreduce result ->", r)


# filter the numbers from the list which are divisible by 2

def method_filter(lst):
    return filter(lambda x : x%2==0, lst)

f = method_filter(l)

print("filter result ->", end =' ')
for i in f:
    print(i,end= ' ')