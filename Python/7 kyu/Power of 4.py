"""
DESCRIPTION:
Write a method that returns true if a given parameter is a power of 4, and false if it's not. If parameter is not an Integer (eg String, Array) method should return false as well.

(In C# Integer means all integer Types like Int16,Int32,.....)

Examples
isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True
"""


def powerof4(n):
    exp = 0
    if isinstance(n, bool):
        return False
    elif isinstance(n, int):
        while 4 ** exp <= n:
            if 4 ** exp == n:
                return True
            exp += 1
        return False
    else:
        return False