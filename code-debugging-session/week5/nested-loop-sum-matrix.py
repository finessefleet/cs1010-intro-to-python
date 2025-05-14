#Bug Focus: Indexing, list structure confusion
#This is a part of CS1010 Code Debugging Sessions started from Week 5. 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
total = 0
for i in range(3):
    for j in range(3):
        total =+ matrix[i][j]
print(total)