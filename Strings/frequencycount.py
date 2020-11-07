string = "hemanth"
count = [0 for i in range(26)]
for i in string:
    count[ord(i)-ord('a')]+=1
for i in string:
    if count[ord(i)-ord('a')]>0:
        print(f"{i}: {count[ord(i)-ord('a')]}")
        count[ord(i)-ord('a')]=0
#if we want sorted order we traverse count instead of string
