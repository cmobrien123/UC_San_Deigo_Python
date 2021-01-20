f= open('colinobrien_a6.py','r')
##creating empty variables
line_num=0
characters=0
blank_line_count=0
comment_count=0
#reading each line of code and running 'calcs'
for line in f:
    #creating number lines
    line_num=line_num+1
    #finding number of characters
    for i in line:
            characters=characters+1
    #printing the lines
    str_line=line.strip()
    print(str(line_num)+' '+str_line)
    #counting the number of times I added a blank line
    if '#blank line' in line:
        blank_line_count=blank_line_count+1
    #counting the number of comments I made
    if '#' in line:
        comment_count=comment_count+1
### ending stats
print('#'*20)
print('END STATS')
print('Characer Count: '+str(characters))
print('Line Count: '+str(line_num))
print('Total line spacings added: '+str(blank_line_count))
print('Total number of comments: '+str(comment_count))
print('#'*20)
f.close()
