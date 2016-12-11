#!/usr/bin/env python

import logging
import os.path
import sys
import os
import fileinput
import argparse
import re

from collections import OrderedDict

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("Up and running %s" % ' '.join(sys.argv))

verbose = False

START = 'XMLDOCUMENT'

terminals = OrderedDict([
    ('(\<\?xml\ version=)', 'xml start'),
    ('(\?\>)', 'xml end'),
    ('(\>)', 'tag end'),
    ('(\/\>)', 'empty tag end'),
    ('(\<\/)', 'end tag begin'),
    ('(\<)', 'start tag begin'),
    ('(\_)', 'underscore'),
    ('(\-)', 'dash'),
    ('(\+)', 'plus'),
    ('(\:)', 'colon'),
    ('(\,)', 'comma'),
    ('(\.)', 'dot'),
    ('(\ )', 'space'),
    ('[0-9]', 'digit'),
    ('[A-Za-z]', 'letter')
])

rules = [
    ['ELEMENT'], # 0
    ['XMLDECL', 'ELEMENT'], # 1
    ['xml start', 'VERNUMB', 'xml end'], # 2
    ['NUMBER', 'dot', 'NUMBER'], # 3
    ['start tag begin', 'NAME', 'X'], # 4
    ['empty tag end'], # 5
    ['tag end', 'Y', 'ENDTAG'], # 6
    ['WORDS'], # 7
    ['ELEMENTS'], # 8
    ['end tag begin', 'NAME', 'tag end'], # 9
    ['CHAR', 'WORDS'], # 10
    [], # 11
    ['ELEMENT', 'ELEMENTS'], # 12
    [], # 13
    ['letter', 'NAMECHARS'], # 14
    ['underscore', 'NAMECHARS'], # 15
    ['colon', 'NAMECHARS'], # 16
    ['NAMECHAR', 'NAMECHARS'], # 17
    [], # 18
    ['letter'], # 19
    ['digit'], # 20
    ['dot'], # 21
    ['dash'], # 22
    ['underscore'], # 23
    ['colon'], # 24
    ['digit', 'O'], # 25
    ['NUMBER'], # 26
    [], # 27
    ['letter'], # 28
    ['digit'], # 29
    ['plus'], # 30
    ['dash'], # 31
    ['underscore'], # 32
    ['colon'], # 33
    ['dot'], # 34
    ['space'] # 35
]

translations = dict([
    (('start tag begin', 'XMLDOCUMENT'), 0),
    (('xml start', 'XMLDOCUMENT'), 1),
    (('xml start', 'XMLDECL'), 2),
    (('digit', 'VERNUMB'), 3),
    (('start tag begin', 'ELEMENT'), 4),
    (('empty tag end', 'X'), 5),
    (('tag end', 'X'), 6),
    (('letter', 'Y'), 7),
    (('digit', 'Y'), 7),
    (('plus', 'Y'), 7),
    (('dash', 'Y'), 7),
    (('underscore', 'Y'), 7),
    (('colon', 'Y'), 7),
    (('dot', 'Y'), 7),
    (('space', 'Y'), 7),
    (('start tag begin', 'Y'), 8),
    (('end tag begin', 'Y'), 8),
    (('end tag begin', 'ENDTAG'), 9),
    (('letter', 'WORDS'), 10),
    (('digit', 'WORDS'), 10),
    (('plus', 'WORDS'), 10),
    (('dash', 'WORDS'), 10),
    (('undesrcore', 'WORDS'), 10),
    (('colon', 'WORDS'), 10),
    (('dot', 'WORDS'), 10),
    (('space', 'WORDS'), 10),
    (('end tag begin', 'WORDS'), 11),
    (('start tag begin', 'ELEMENTS'), 12),
    (('end tag begin', 'ELEMENTS'), 13),
    (('letter', 'NAME'), 14),
    (('underscore', 'NAME'), 15),
    (('colon', 'NAME'), 16),
    (('letter', 'NAMECHARS'), 17),
    (('digit', 'NAMECHARS'), 17),
    (('dash', 'NAMECHARS'), 17),
    (('underscore', 'NAMECHARS'), 17),
    (('colon', 'NAMECHARS'), 17),
    (('dot', 'NAMECHARS'), 17),
    (('empty tag end', 'NAMECHARS'), 18),
    (('tag end', 'NAMECHARS'), 18),
    (('letter', 'NAMECHAR'), 19),
    (('digit', 'NAMECHAR'), 20),
    (('dot', 'NAMECHAR'), 21),
    (('dash', 'NAMECHAR'), 22),
    (('underscore', 'NAMECHAR'), 23),
    (('colon', 'NAMECHAR'), 24),
    (('digit', 'NUMBER'), 25),
    (('digit', 'O'), 26),
    (('xml end', 'O'), 27),
    (('dot', 'O'), 27),
    (('letter', 'CHAR'), 28),
    (('digit', 'CHAR'), 29),
    (('plus', 'CHAR'), 30),
    (('dash', 'CHAR'), 31),
    (('underscore', 'CHAR'), 32),
    (('colon', 'CHAR'), 33),
    (('dot', 'CHAR'), 34),
    (('space', 'CHAR'), 35),
])

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items) - 1]

def tokenize(input):
    remaining = input
    tokens = []

    while remaining:
        matched = False

        for terminal, name in terminals.iteritems():
            match = re.match(terminal, remaining)

            if match:
                matched = True
                token = match.group(0)

                tokens.append(name)
                remaining = remaining[len(token):]

                if verbose:
                    print "\tMatched '%s' therefore adding '%s' to tokens" % (token, name)
                break

        if not matched:
            if recovery:
                # try to recover - skip all undefined symbols

                nearest_terminal = None
                nearest_name = None
                nearest_dist = None
                nearest_token = None

                # find nearest matching terminal
                for terminal, name in terminals.iteritems():
                    match = re.search(terminal, remaining)

                    if match:
                        matched = True
                        token = match.group(0)

                        terminal_dist = match.start()
                        if terminal_dist < nearest_dist or not nearest_dist:
                            nearest_dist = terminal_dist
                            nearest_terminal = terminal
                            nearest_name = name
                            nearest_token = token

                if nearest_terminal:
                    if verbose:
                        print "\tSkipped '%s' - undefined symbol." % (remaining[:nearest_dist])
                        print "\tMatched '%s' as nearest matching terminal, therefore adding '%s' to tokens" % (token, name)

                    match = re.search(nearest_terminal, remaining)

                    tokens.append(nearest_name)
                    remaining = remaining[len(nearest_token)+nearest_dist:]

            else:
                if verbose:
                    logger.error("Phrase is not valid - no terminal matching remaining part '%s'", remaining)

                return False



    return tokens

def process(input):
    stack = Stack()
    tokens = tokenize(input)

    if not tokens:
        return False

    if verbose:
        print ""
        print "\tTokens are [%s]" % ', '.join(tokens)
        print ""

    index = 0
    stack.push(START)

    while not stack.isEmpty():
        if verbose:
            print "\tCurrent index: %d [%s], stack: [%s]" % (index, tokens[index], ', '.join(stack.items))
            print "\tRemaining tokens [%s]" % ', '.join(tokens[index::])

        top = stack.pop()

        if tokens[index] == top:
            if verbose:
                print "\t\tRemoved element '%s' from stack and moving on input to %d" % (top, index + 1)

            index += 1
        else:
            key = (tokens[index], top)

            if key in translations:
                rule = rules[translations[key]]

                if verbose:
                    print "\t\tReplace '%s' in stack by [%s]" % (top, ', '.join(rule))

                for item in rule[::-1]:
                    stack.push(item)
            else:
                if verbose:
                    logger.error("No translation for input '%s' and non-terminal '%s'", tokens[index], top)

                return False

    return stack.isEmpty() and (index == len(tokens))

def test(input):
    print 'ACCEPT' if process(input) else 'REJECT'

def demo_test(input):
    print input
    test(input)
    print ''

def demo():
    print ''
    print '=== DEMO START ==='

    #demo_test('<?xml version=1.2?><a><b></b></a>')
    #demo_test('<?xml version=1.2?><html><head><title>Toto je telo</title></head><body><br/></body></html>')
    #demo_test('blabla')
    #demo_test('<?xml version=1.2?><html><head></html><br/></head>')
    #demo_test('<?xml version=1.2?><html>aaa<b></b></html>')
    #demo_test('<empty/>')
    #demo_test('<two></two><three></three>')
    #demo_test('<one><two></two><three></three></one>')
    #demo_test('<one><two></two><three>example</three></one>')
    #demo_test('<one><two></two><three><empty/></three></one>')
    #demo_test('<>')
    #demo_test('<?xmlversion=1.2?><html>aaa<b></b></html>')
    #demo_test('<?xml version=1.2?><html>aaa<b></b></html>')
    #demo_test('<?xml version=1.2?><html><head></html><br/></head>')
    
    demo_test('<a>*#<b></b></a>')

    print '=== DEMO END ==='
    print ''

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    p.add_argument("-r", "--recovery", help="Enable lexical error recovery", action="store_true")
    args = p.parse_args()

    verbose = args.verbose
    recovery = args.recovery

    demo()
    #for line in fileinput.input():
    #    test(line)
