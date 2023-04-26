"""
String Methods
.strip()

When working with strings that come from real data, you will often find that the strings aren’t super clean. You’ll find
lots of extra whitespace, unnecessary linebreaks, and rogue tabs.

Python provides a great method for cleaning strings: .strip(). Stripping a string removes all whitespace characters from
the beginning and end. Consider the following example:
"""

featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'
"""

All the whitespace on either side of the string has been stripped, but the whitespace in the middle has been preserved.

You can also use .strip() with a character argument, which will strip that character from either end of the string.
"""

featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       '
"""

By including the argument '!' we are able to strip all of the ! characters from either side of the string. Notice that
now that we’ve included an argument we are no longer stripping whitespace, we are ONLY stripping the argument.
Instructions
1.

They sent over another list containing all the lines to the Audre Lorde poem, Love, Maybe. They want you to join
together all of the lines into a single string that can be used to display the poem again, but this time, you’ve noticed
that the list contains a ton of unnecessary whitespace that doesn’t appear in the actual poem.

First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list
love_maybe_lines_stripped.

Use a for loop to iterate through each line in the list and strip them. Be sure to use .append() to add the stripped
lines to a new list.
2.

.join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be
printed to display the poem.

Each line of the poem should show up on its own line.
3.

Print love_maybe_full.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    How to add strings to a list?

List has no attribute: strip? (try a for loop)
My list has every letter separated instead of each line?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
