"""
String Methods
Review

Excellent work! This lesson has shown you the vast variety of string methods and their power. Whatever the problem you
are trying to solve, if you are working with strings then string methods are likely going to be part of the solution.

Over this lesson you’ve learned:

    .upper(), .title(), and .lower() adjust the casing of your string.
    .split() takes a string and creates a list of substrings.
    .join() takes a list of strings and creates a string.
    .strip() cleans off whitespace, or other noise from the beginning and end of a string.
    .replace() replaces all instances of a character/string in a string with another character/string.
    .find() searches a string for a character/string and returns the index value that character/string is found at.
    .format() allows you to interpolate a string with variables.

Well I’ve been stringing you along for long enough, let’s get some more practice in!
Instructions
1.

Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems, titled
highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that
can display the name, title, and publication date of the highlighted poems on the site.

First, start by printing highlighted_poems to the terminal and see how it displays.
2.

The information for each poem is separated by commas, and within this information is the title of the poem, the author,
and the date of publication.

Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

Recall that the syntax for splitting a string into a list is:

py my_string.split(delimiter)
3.

Print highlighted_poems_list, how does the structure of the data look now?
4.

Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.

Start by creating a new empty list, highlighted_poems_stripped.

Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it
to your new list, highlighted_poems_stripped.

Your for loop should look have the form:

for poem in highlighted_poem_list:
  # code that strips the poem and appends it to the list

5.

Print highlighted_poems_stripped.

Looks good! All the whitespace is cleaned up.
6.

Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists.

Create a new empty list called highlighted_poems_details.
7.

Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into
highlighted_poems_details.
8.

Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.

Create three new empty lists, titles, poets, and dates.
9.

Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists
titles, poets, and dates.

For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles,
"William Carlos Williams" to poets, and "1915" to dates.
10.

Finally, write a for loop that uses .format() to print out the following string for each poem:

The poem TITLE was published by POET in DATE.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    What other string methods are there?

How can we reference the right index if all our lists are separate? (step 10)
What if I use += instead of append?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
