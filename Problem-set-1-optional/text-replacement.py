###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker_1 = "AFK"
replacement_1 = "away from keyboard"
line_1 = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
marker_2 = "EY"
replacement_2 = "Eyjafjallajokull"
line_2 = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

# Answer example 1
find_afk = line_1.find("AFK")
first_part = line_1[0:find_afk]
second_part = line_1[find_afk+3:]
replaced_line_1 = first_part + replacement_1 + second_part

print replaced_line_1

#Answer example 2
find_ey = line_2.find("EY")
first_part = line_2[0:find_ey]
second_part = line_2[find_ey+2:]
replaced_line_2 = first_part + replacement_2 + second_part

print replaced_line_2

# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.
