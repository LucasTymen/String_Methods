"""
String Methods
.find()

Another interesting string method is .find(). .find() takes a string as an argument and searching the string it was run
on for that string. It then returns the first index value where that string is located.

Here’s an example:
"""
print('smooth'.find('t'))
# => '4'
"""
We searched the string 'smooth' for the string 't' and found that it was at the fourth index spot, so .find() returned 4.

You can also search for larger strings, and .find() will return the index value of the first character of that string.
"""
print("smooth".find('oo'))
# => '2'
"""
Notice here that 2 is the index of the first o.
Instructions
1.

In the code editor is the first line of Gabriela Mistral’s poem God Wills It.

At what index place does the word “disown” appear? Save that index place to the variable disown_placement.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    How can I find all indices where a substring appears in a string?

What causes .find() to return -1?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
