"""
String Methods
Joining Strings II

In the last exercise, we joined together a list of words using a space as the delimiter to create a sentence. In fact,
you can use any string as a delimiter to join together a list of strings. For example, if we have the list
"""
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
"""
We could join this list together with ANY string. One often used string is a comma , because then we can create a string
of comma separated variables, or CSV.
"""
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'
"""
You’ll often find data stored in CSVs because it is an efficient, simple file type used by popular programs like Excel
or Google Spreadsheets.

You can also join using escape sequences as the delimiter. Consider the following example:


smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of
the world so soft and slow', 'Turning you \'round and \'round']

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

print(smooth_fifth_verse)


This code is taking the list of strings and joining them using a newline \n as the delimiter. Then it prints the result
and produces the output:

Well I'm from the barrio
You hear my rhythm on your radio
You feel the turning of the world so soft and slow
Turning you 'round and 'round

Instructions
1.

You’ve been given a list, winter_trees_lines, that contains all the lines to William Carlos Williams poem, Winter Trees.
You’ve been asked to join together the strings in the list together into a single string that can be used to display the
full poem. Name this string winter_trees_full.

Print your result to the terminal. Make sure that each line of the poem appears on a new line in your string.

Use \n, the escape character for a line break.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    What if the strings in the list contain the delimiter?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
