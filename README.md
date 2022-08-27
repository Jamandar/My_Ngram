# My_Ngram

Task
Write a program my_ngram; It will count the number of occurrences per character. $>./my_ngram "abcdef" a:1 b:1 c:1 d:1 e:1 f:1 $>

Description
In computational linguistics and probability, an n-gram is a contiguous sequence of n items from a given sample of text or speech. The items can be phonemes, syllables, letters, words or base pairs according to the application. The n-grams typically are collected from a text or speech corpus. When the items are words, n-grams may also be called shingles.

Google Inc. has used this technique to improve the completion of its Search Engine. The program was developed by Jon Orwant and Will Brockman and released in mid-December 2010.

My Ngram will take 1 or multiple strings as arguments.

It will display, one per line, each character and the numbers of times it appears.

Order will be alphanumerical.

Installation
gcc -Wall -Wextra my_ngram.c -o my_ngram

Usage
./my_ngram "abcdef"

b:1 c:1 d:1 e:1 f:1

The Core Team
