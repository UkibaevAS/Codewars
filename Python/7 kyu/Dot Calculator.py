"""
You'll have to return a string that contains dots, as many the equation returns. If the result is 0,
return the empty string. When it comes to subtraction, the first number will always be greater than
or equal to the second number.

Examples (Input => Output)
* "..... + ..............." => "...................."
* "..... - ..."             => ".."
* "..... - ."               => "...."
* "..... * ..."             => "..............."
* "..... * .."              => ".........."
* "..... // .."             => ".."
* "..... // ."              => "....."
* ". // .."                 => ""
* ".. - .."                 => ""
"""


def result_output(sign: str, txt: str) -> list:
    txt = txt.replace(' ', '').split(sign)
    return [len(i) for i in txt]


def calc(txt):
    if txt.count('+') == 1:
        res = result_output('+', txt)
        return (res[0] + res[1]) * "."
    elif txt.count('-') == 1:
        res = result_output('-', txt)
        return (res[0] - res[1]) * "."
    elif txt.count('*') == 1:
        res = result_output('*', txt)
        return (res[0] * res[1]) * "."
    else:
        res = result_output('//', txt)
        return (res[0] // res[1]) * "."

# def calculator(txt):
#     a, op, b = txt.split()
#     a, b = len(a), len(b)
#     return '.' * eval(f'{a} {op} {b}')