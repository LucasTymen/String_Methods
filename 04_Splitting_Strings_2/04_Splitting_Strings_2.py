"""
String Methods
Splitting Strings II

If we provide an argument for .split() we can dictate the character we want our string to be split on. This argument
should be provided as a string itself.

Consider the following example:
"""
greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
# => ['sa', 'ta', 'a']
"""
We provided 'n' as the argument for .split() so our string “santana” got split at each 'n' character into a list of
three strings.

What do you think happens if we split the same string at 'a'?
"""
print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', '']
"""
Notice that there is an unexpected extra '' string in this list. When you split a string on a character that it also
ends with, you’ll end up with an empty string at the end of the list.

You can use any string as the argument for .split(), making it a versatile and powerful tool.
Instructions
1.

Your boss at the Poetry organization sent over a bunch of author names that he wants you to prepare for importing into
the database. Annoyingly, he sent them over as a long string with the names separated by commas.

Using .split() and the provided string, create a list called author_names containing each individual author name as it’s
own string.
2.

Great work, but now it turns out they didn’t want poet’s first names (why didn’t they just say that the first time!?)

Create another list called author_last_names that only contains the last names of the poets in the provided string.

There are several ways to do this, but one way is to iterate through the list you created in part one and use .split(),
negative indexing, and .append() to construct the new list.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    How does split() work for arguments longer than a single character?

How to select only last names? (Solution Explanation)
How should I use .split() to remove commas between names?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
