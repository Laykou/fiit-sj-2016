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
