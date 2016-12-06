# FIIT SJ 2016

Assignment 1

It runs demo after start and then accepts input (on each new line).

```
$ python sj.py
2016-12-06 16:23:45,079 : INFO : Up and running /Users/laykou/Dropbox/sj.py

=== DEMO START ===
<a><b></b></a>
ACCEPT

<?xml version=1.2?><a><b></b></a>
ACCEPT

<?xml version=1.2?><a><b></b></a>
ACCEPT

<?xml version=1.2?><html><head><title>Toto je telo</title></head><body><br/></body></html>
ACCEPT

blabla
REJECT

<?xml version=1.2?><html><head></html><br/></head>
ACCEPT

<?xml version=1.2?><html>aaa<b></b></html>
REJECT

<empty/>
ACCEPT

<two></two><three></three>
REJECT

<one><two></two><three></three></one>
ACCEPT

<one><two></two><three>example</three></one>
ACCEPT

<one><two></two><three><empty/></three></one>
ACCEPT

<>
REJECT

=== DEMO END ===
```

## Attributes

**--verbose** to run in verbose mode:

```
$python sj.py --verbose
2016-12-06 16:17:16,074 : INFO : Up and running /Users/laykou/Dropbox/sj.py --verbose

=== DEMO START ===
<a><b></b></a>
    Matched '<' therefore adding 'start tag begin' to tokens
    Matched 'a' therefore adding 'letter' to tokens
    Matched '>' therefore adding 'tag end' to tokens
    Matched '<' therefore adding 'start tag begin' to tokens
    Matched 'b' therefore adding 'letter' to tokens
    Matched '>' therefore adding 'tag end' to tokens
    Matched '</' therefore adding 'end tag begin' to tokens
    Matched 'b' therefore adding 'letter' to tokens
    Matched '>' therefore adding 'tag end' to tokens
    Matched '</' therefore adding 'end tag begin' to tokens
    Matched 'a' therefore adding 'letter' to tokens
    Matched '>' therefore adding 'tag end' to tokens

    Tokens are [start tag begin, letter, tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]

    Current index: 0 [start tag begin], stack: [XMLDOCUMENT]
    Remaining tokens [start tag begin, letter, tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'XMLDOCUMENT' in stack by [ELEMENT]
    Current index: 0 [start tag begin], stack: [ELEMENT]
    Remaining tokens [start tag begin, letter, tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'ELEMENT' in stack by [start tag begin, NAME, X]
    Current index: 0 [start tag begin], stack: [X, NAME, start tag begin]
    Remaining tokens [start tag begin, letter, tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Removed element 'start tag begin' from stack and moving on input to 1
    Current index: 1 [letter], stack: [X, NAME]
    Remaining tokens [letter, tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'NAME' in stack by [letter, NAMECHARS]
    Current index: 1 [letter], stack: [X, NAMECHARS, letter]
    Remaining tokens [letter, tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Removed element 'letter' from stack and moving on input to 2
    Current index: 2 [tag end], stack: [X, NAMECHARS]
    Remaining tokens [tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'NAMECHARS' in stack by []
    Current index: 2 [tag end], stack: [X]
    Remaining tokens [tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'X' in stack by [tag end, Y, ENDTAG]
    Current index: 2 [tag end], stack: [ENDTAG, Y, tag end]
    Remaining tokens [tag end, start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Removed element 'tag end' from stack and moving on input to 3
    Current index: 3 [start tag begin], stack: [ENDTAG, Y]
    Remaining tokens [start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'Y' in stack by [ELEMENTS]
    Current index: 3 [start tag begin], stack: [ENDTAG, ELEMENTS]
    Remaining tokens [start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'ELEMENTS' in stack by [ELEMENT, ELEMENTS]
    Current index: 3 [start tag begin], stack: [ENDTAG, ELEMENTS, ELEMENT]
    Remaining tokens [start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'ELEMENT' in stack by [start tag begin, NAME, X]
    Current index: 3 [start tag begin], stack: [ENDTAG, ELEMENTS, X, NAME, start tag begin]
    Remaining tokens [start tag begin, letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Removed element 'start tag begin' from stack and moving on input to 4
    Current index: 4 [letter], stack: [ENDTAG, ELEMENTS, X, NAME]
    Remaining tokens [letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'NAME' in stack by [letter, NAMECHARS]
    Current index: 4 [letter], stack: [ENDTAG, ELEMENTS, X, NAMECHARS, letter]
    Remaining tokens [letter, tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Removed element 'letter' from stack and moving on input to 5
    Current index: 5 [tag end], stack: [ENDTAG, ELEMENTS, X, NAMECHARS]
    Remaining tokens [tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'NAMECHARS' in stack by []
    Current index: 5 [tag end], stack: [ENDTAG, ELEMENTS, X]
    Remaining tokens [tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'X' in stack by [tag end, Y, ENDTAG]
    Current index: 5 [tag end], stack: [ENDTAG, ELEMENTS, ENDTAG, Y, tag end]
    Remaining tokens [tag end, end tag begin, letter, tag end, end tag begin, letter, tag end]
        Removed element 'tag end' from stack and moving on input to 6
    Current index: 6 [end tag begin], stack: [ENDTAG, ELEMENTS, ENDTAG, Y]
    Remaining tokens [end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'Y' in stack by [ELEMENTS]
    Current index: 6 [end tag begin], stack: [ENDTAG, ELEMENTS, ENDTAG, ELEMENTS]
    Remaining tokens [end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'ELEMENTS' in stack by []
    Current index: 6 [end tag begin], stack: [ENDTAG, ELEMENTS, ENDTAG]
    Remaining tokens [end tag begin, letter, tag end, end tag begin, letter, tag end]
        Replace 'ENDTAG' in stack by [end tag begin, NAME, tag end]
    Current index: 6 [end tag begin], stack: [ENDTAG, ELEMENTS, tag end, NAME, end tag begin]
    Remaining tokens [end tag begin, letter, tag end, end tag begin, letter, tag end]
        Removed element 'end tag begin' from stack and moving on input to 7
    Current index: 7 [letter], stack: [ENDTAG, ELEMENTS, tag end, NAME]
    Remaining tokens [letter, tag end, end tag begin, letter, tag end]
        Replace 'NAME' in stack by [letter, NAMECHARS]
    Current index: 7 [letter], stack: [ENDTAG, ELEMENTS, tag end, NAMECHARS, letter]
    Remaining tokens [letter, tag end, end tag begin, letter, tag end]
        Removed element 'letter' from stack and moving on input to 8
    Current index: 8 [tag end], stack: [ENDTAG, ELEMENTS, tag end, NAMECHARS]
    Remaining tokens [tag end, end tag begin, letter, tag end]
        Replace 'NAMECHARS' in stack by []
    Current index: 8 [tag end], stack: [ENDTAG, ELEMENTS, tag end]
    Remaining tokens [tag end, end tag begin, letter, tag end]
        Removed element 'tag end' from stack and moving on input to 9
    Current index: 9 [end tag begin], stack: [ENDTAG, ELEMENTS]
    Remaining tokens [end tag begin, letter, tag end]
        Replace 'ELEMENTS' in stack by []
    Current index: 9 [end tag begin], stack: [ENDTAG]
    Remaining tokens [end tag begin, letter, tag end]
        Replace 'ENDTAG' in stack by [end tag begin, NAME, tag end]
    Current index: 9 [end tag begin], stack: [tag end, NAME, end tag begin]
    Remaining tokens [end tag begin, letter, tag end]
        Removed element 'end tag begin' from stack and moving on input to 10
    Current index: 10 [letter], stack: [tag end, NAME]
    Remaining tokens [letter, tag end]
        Replace 'NAME' in stack by [letter, NAMECHARS]
    Current index: 10 [letter], stack: [tag end, NAMECHARS, letter]
    Remaining tokens [letter, tag end]
        Removed element 'letter' from stack and moving on input to 11
    Current index: 11 [tag end], stack: [tag end, NAMECHARS]
    Remaining tokens [tag end]
        Replace 'NAMECHARS' in stack by []
    Current index: 11 [tag end], stack: [tag end]
    Remaining tokens [tag end]
        Removed element 'tag end' from stack and moving on input to 12
ACCEPT

=== DEMO END ===
```
