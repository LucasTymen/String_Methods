"""

String Methods
Formatting Methods

There are three string methods that can change the casing of a string. These are .lower(), .upper(), and .title().

    .lower() returns the string with all lowercase characters.
    .upper() returns the string with all uppercase characters.
    .title() returns the string in title case, which means the first letter of each word is capitalized.

Here’s an example of .lower() in action:
"""
favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)
# => 'smooth'
"""
Every character was changed to lowercase! It’s important to remember that string methods can only create new strings,
they do not change the original string.
"""
print(favorite_song)
# => 'SmOoTH'
"""
See, it’s still the same! These string methods are great for sanitizing user input and standardizing the formatting of
your strings.
Instructions
1.

You’re a programmer working for an organization that is trying to digitize and store poetry called Preserve the Verse.

You’ve been given two strings, the title of a poem and its author, and have been asked to reformat them slightly to fit
the conventions of the organization’s database.

Make poem_title have title case and save it to poem_title_fixed.
2.

Print poem_title and poem_title_fixed.

How did the string change?
3.

The organization’s database also needs the author’s name to be uppercase only.

Make poem_author uppercase and save it to poem_author_fixed.
4.

Print poem_author and poem_author_fixed.

Again, how did the string change?
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Do these methods affect special characters?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
