"""
String Methods
Joining Strings

Now that you’ve learned to break strings apart using .split(), let’s learn to put them back together
using .join(). .join() is essentially the opposite of .split(), it joins a list of strings together with a given
delimiter. The syntax of .join() is:
"""
'delimiter'.join(list_you_want_to_join)
"""
Now this may seem a little weird, because with .split() the argument was the delimiter, but now the argument is the list.
This is because join is still a string method, which means it has to act on a string. The string .join() acts on is the
delimiter you want to join with, therefore the list you want to join has to be the argument.

This can be a bit confusing, so let’s take a look at an example.
"""
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
"""
We take the list of strings, my_munequita, and we joined it together with our delimiter, ' ', which is a space. The
space is important if you are trying to build a sentence from words, otherwise, we would have ended up with:
"""
print(''.join(my_munequita))
# => 'MySpanishHarlemMonaLisa'
"""
Instructions
1.

You’ve been provided with a list of words from the first line of Jean Toomer’s poem Reapers.

Use .join() to combine these words into a sentence and save that sentence as the string reapers_line_one.

Make sure that you are running join on a space, ' ', otherwise you’ll mash the words together.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    If you do a join() after a split() using the same delimiter, does this result in the original string?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
