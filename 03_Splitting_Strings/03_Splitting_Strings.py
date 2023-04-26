"""

String Methods
Splitting Strings

.upper(), .lower(), and .title() all are performed on an existing string and produce a string in return. Let’s take a look at a string method that returns a different object entirely!

.split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument (which in the case of .split() is known as the delimiter). The following syntax should be used:

string_name.split(delimiter)

If you do not provide an argument for .split() it will default to splitting at spaces.

For example, consider the following strings:

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

.split returned a list with each word in the string. Important to note: if we run .split() on a string with no spaces, we will get the same string in return.
Instructions
1.

In the code editor is a string of the first line of the poem Spring Storm by William Carlos Williams.

Use .split() to create a list called line_one_words that contains each word in this line of poetry.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    If we run .split() without an argument, what happens to consecutive whitespaces?

What does the delimiter do?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
