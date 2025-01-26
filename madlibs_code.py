with open("madlibs_story.txt","r") as f:
    story=f.read()
sets=set()
start_index=-1
targetstart= '<'
targetend='>'
for i,char in enumerate(story):
    if char==targetstart:
        start_index= i
    if char==targetend and start_index!=-1:
        words=story[start_index:i+1]
        sets.add(words)
        start_index=-1
dicts={}
for words in sets:
     ans=input(f"enter a answers for {words}: ")
     dicts[words]=ans
for words in sets:
    story=story.replace(words,dicts[words])
print(story)