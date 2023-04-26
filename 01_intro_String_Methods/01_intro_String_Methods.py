"""
String Methods
Introduction

Do you have a gigantic string that you need to parse for information? Do you need to sanitize a user’s input to work in
a function? Do you need to be able to generate outputs with variable values? All of these things can be accomplished
with string methods!

Python comes with built-in string methods that give you the power to perform complicated tasks on strings very quickly
and efficiently. These string methods allow you to change the case of a string, split a string into many smaller
strings, join many small strings together into a larger string, and allow you to neatly combine changing variables with
string outputs.

In the previous lesson, you worked with len(), which was a function that determined the number of characters in a string.
This, while similar, was NOT a string method. String methods all have the same syntax:

string_name.string_method(arguments)

Unlike len(), which is called with a string as its argument, a string method is called at the end of a string and each
one has its own method specific arguments.
Instructions

The diagram shows all of the string methods you can expect to learn in this lesson. Take a quick look at them and then
let’s get started!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Can we call more than one string method in a single statement?

Still have questions? View this exercise's thread in the Codecademy Forums.


######################### String Methods : 'Hello World' #########################

"""

'Hello world'.upper() # outputs 'HELLO WORLD'
'Hello world'.lower() # outputs 'hello world'
'Hello world'.title() # outputs 'Hello World'
'Hello world'.split() # outputs ['Hello', 'world']
' '.join(['Hello', 'world']) # outputs 'Hello world'
'Hello world'.replace('H', 'J') # outputs 'Jello world'
'   Hello world     '.strip() # outputs 'Hello world'
"{} {}".format("Hello", "world") # outputs 'Hello world'
