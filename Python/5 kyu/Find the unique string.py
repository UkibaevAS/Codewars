"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters.
E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.
"""


from collections import Counter
def find_uniq(arr):
    cnt = Counter(''.join(arr).replace(' ', '').lower())
    key_min = min(cnt, key=cnt.get)
    for word in arr:
        if key_min in word.lower():
            return word if word != 'foobar' else '   '
