"""
String Methods
Splitting Strings III

We can also split strings using escape sequences. Escape sequences are used to indicate that we want to split by
something in a string that is not necessarily a character. The two escape sequences we will cover here are

    \n Newline
    \t Horizontal Tab

Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by
tabs. \t is particularly useful when dealing with certain datasets because it is not uncommon for data points to be
separated by tabs.

Let’s take a look at an example of splitting by an escape sequence:
"""


smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)


"""
This code is splitting the multi-line string at the newlines (\n) which exist at the end of each line and saving it to a
new list called chorus_lines. Then it prints chorus_lines which will produce the output

['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to
better suit your mood', "Because you're so smooth"]

The new list contains each line of the original string as its own smaller string. Also, notice that Python automatically
escaped the ' character in the first line and adjusted to double quotation marks to allow the apostrophe on last line
when it created the new list.
Instructions
1.

The organization has sent you over the full text for William Carlos Williams poem Spring Storm. They want you to break
the poem up into its individual lines.

Create a list called spring_storm_lines that contains a string for each line of Spring Storm.

You will have to use .split() and the escape character for a newline, \n.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    What other escape sequences are there?

What does the backslash in the variable declaration mean? (= \)

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
