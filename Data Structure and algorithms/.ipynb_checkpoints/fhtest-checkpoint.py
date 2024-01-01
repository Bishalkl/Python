print("FILES HANDILING")
f = open("test.txt", 'r') #we can read files with mode "r".
f.seek(0)
print(f.readlines())
    


