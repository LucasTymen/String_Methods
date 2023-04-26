"""
String Methods
.format() II

.format() can be made even more legible for other people reading your code by including keywords. Previously,
with .format(), you had to make sure that your variables appeared as arguments in the same order that you wanted them to
appear in the string, which added unnecessary complications when writing code.

By including keywords in the string, and in the arguments, you can remove that ambiguity. Let’s look at an example.
"""
def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
"""
Now it is clear to anyone reading the string what it is supposed to return, they don’t even need to look at the arguments
of .format() in order to get a clear understanding of what is supposed to happen. You can even reverse the order of
artist and song in the code above and it will work the same way.

For example, if the arguments of .format() are in a different order, the code will still work since the keywords are
present:
"""
def favorite_song_statement(song, artist):
  # this will have the same output as the above example
  return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)
"""
This makes writing AND reading the code much easier.
Instructions
1.

The function poem_description is supposed to use .format() to print out some quick information about a poem, but it
seems to be causing some errors currently.

Fix the function by using keywords in the .format() method.
2.

Run poem_description with the following arguments and save the results to the variable my_beard_description:
"""
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Can we utilize both keyword and positional arguments in the format() method?

Do we need to define the variables seperately?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
