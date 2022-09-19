history = '''A \'succession of Hindu dynasties\' ruled \nover the region from the 7th-14th centuries.
After the seventh century, \tsignificant developments took\\ place in Kashmiri Hinduism.'''

#String Functions


print(len(history))     #to know the length or the number of the letters in a string
print(history.endswith("Kashmiri Hinduism."))    #to know the last word in the string
print(history.count("the"))    #to count the number of occurance of a particular word
print(history.capitalize())    #to capitalize ythe initial word of the string
print(history.find("seventh"))    #to find the index number of a word in a string
print(history.replace("Hindu","Islam"))   #to replace a  word with another in a string



# Using Escape Sequences

# \n - puts the sentence in  next line
# \t - inserts a tab space in a string
# \\ - inserts a \ single slash 
# \' - inserts single quotes in a string