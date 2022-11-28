# this will open the file and store in
# "file" variable
import re
file = open("demoFile.txt", "r")
x = file.read()
test_str = x
print (re.sub(r"([0-9]+(\.[0-9]+)?)",r" \1 ", test_str).strip())


# Python3 code to demonstrate working of
# Add space between Numbers and Alphabets in String

# initializing string
# test_str = 'ge3eks4geeks'
#
# # printing original String
# print("The original string is : " + str(test_str))
# num="0123456789"
# for i in test_str:
# 	if i in num:
# 		test_str=test_str.replace(i," "+i+" ")
# res=test_str
# # printing result
# print("The space added string : " + str(res))
