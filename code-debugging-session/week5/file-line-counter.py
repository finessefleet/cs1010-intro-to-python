#Bug Focus: File handling, logic with string stripping
#This is a part of CS1010 Code Debugging Sessions started from Week 5. 

def count_lines(file_path):
    f = open(file_path)
    count = 0
    for line in f:
        if line != "\n":
            count += 1
    f.close()
    return count

print(count_lines("sample.txt"))