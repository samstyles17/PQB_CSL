fav1 = ['pizza', 'nuggets','hotdog','noodles','pasta','burger']
fav2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']

index1 = index2 = 10

for i in range(len(fav1)):
    ind = fav2.index(fav1[i])

    if i + ind < index1 + index2:
        index1 = i
        index2  = ind


print(fav1[index1])
