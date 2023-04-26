"""
String Methods
.format()

Python also provides a handy string method for including variables in strings. This method is .format(). .format() takes
variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for
where those variables will be imported.

Consider the following function:
"""
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
"""
The function favorite_song_statement takes two arguments, song and artist, then returns a string that includes both of
the arguments and prints a sentence. Note: .format() can take as many arguments as there are {} in the string it is run
on, which in this case is two.

Here’s an example of the function being run:
"""
print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."
"""
Now you may be asking yourself, I could have written this function using string concatenation instead of .format(), why
is this method better? The answer is legibility and reusability. It is much easier to picture the end result .format()
than it is to picture the end result of string concatenation and legibility is everything. You can also reuse the same
base string with different variables, allowing you to cut down on unnecessary, hard to interpret code.
Instructions
1.

Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The
function should use .format() to return the following string:

 The poem "[TITLE]" is written by [POET].

For example, if the function is given the inputs
"""
poem_title_card("I Hear America Singing", "Walt Whitman")
"""
It should return the string

The poem "I Hear America Singing" is written by Walt Whitman.

Remember to escape the " characters!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Can we provide any input type to the format() method?

What are the backslashes in the string?
What are good reasons to use string formatting?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
