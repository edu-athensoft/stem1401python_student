"""
string literal - escape characters
\

\' single quote
\" double quote
\\ backslash
\n new line
\r carriage return
\t tab
\b backspace
\f form feed
\v vertical tab (Internet Explorer 9 and older treats '\v as 'v instead of a vertical tab ('\x0B). If cross-browser compatibility is a concern, use \x0B instead of \v.)
\0 null character (U+0000 NULL) (only if the next character is not a decimal digit; else it is an octal escape sequence)
\xFF character represented by the hexadecimal byte "FF"

strings
chars
multiline string
unicode string      u'...'
raw string          r'...'
"""

str1 = 'I\'m a student.'
print(str1)

str1 = "I\'m a \"student\"."
print(str1)

# filepath = "C:\program files\abc\bcd"
# print(filepath)

filepath = "C:\\program files\\abc\\bcd"
print(filepath)

str1 = "abcdefg\nabcdefg\nabcdefgabcdefg"
print(str1)

str1 = "abcd\tabcd\tabcdef\tgabcdefg"
print(str1)

str1 = "abc1\tab  \tabcdef\tgabcdefg"
print(str1)


# r - raw
str1 = r"abc1\tab  \tabcdef\ngabcdefg"
print(str1)
str1 = "abc1\tab  \tabcdef\ngabcdefg"
print(str1)





