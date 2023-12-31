# What the hell is this?

Simplify is a simple conlang made to replace interpreted languages code with just one line, 
althought i must admit it's far from functional since it was purely adapted from python codes.

# Syntax

The syntax is pretty much based on Python since it was written in python but there's important chars replacements you should check.

Simplify Char | Actual Char
------------- | ------------
\	            | Newline char(\n). <br> Mandatory for every line of code since the one line <br> converter actually removes all actual newline. characters.
&nbsp;        | Tab char(\t). <br> To make the code cleaner, indents are mandatory on this language.
&#124;	      | Space char( ). <br> Alternative to space char because of the replacement done above.
&#42;	        | Comment char(in Python: #). <br> All comments should start and end with asterisks.

# Commands

Variable and function names can have more than one char, so the replacement wont affect them.

Simplify keyword | Actual Keyword
---------------- | --------------
^	               | &#42;&#42;(exponentiation)
&	               | and(&&)
@	               | or(&#124;&#124;)
~	               | not
?	               | range
&#35;	           | reversed(range doesn't support decreasing orders)
b	               | break
d	               | function
e	               | else
f	               | for
F	               | false
i	               | if
p	               | print
r	               | return
s	               | input
t	               | f(format used before strings)
T	               | true
w	               | while

# Why you should use it?

Uh... I don't know? Will you use it tho? It's an esolang, it's not an useful language lol.
