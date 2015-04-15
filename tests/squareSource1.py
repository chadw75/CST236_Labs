"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 4 sides of a square is square, or rectangle, or trapazoid
"""

def get_square_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given square is square or rectangle

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param d: line d
    :type d: float

    :return: "square", "rectangle", or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 8:
        
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]
       aA = a[4]
       aB = a[5]
       aC = a[6]
       aD = a[7]

    if isinstance(a, dict) and len(a.keys()) == 8:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]
       aA = values[4]
       aB = values[5]
       aC = values[6]
       aD = values[7]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))  and isinstance(c, (int, float)) and isinstance(d, (int, float))
       and (isinstance(aA, (int, float)) and isinstance(aB, (int, float)) and isinstance(aC, (int, float)) and isinstance(aD, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0 or aA <= 0 or aA >= 180 or aB <= 0 or aB >= 180 or aC <= 0 or aC >= 180 or aD <= 0 or aD >= 180:
        return "invalid"

    if a == b and b == c and c == d and aA == 90 and aB == 90 and aC == 90 and aD == 90:
        return "square"

    if a == c and b == d and a != d and aA == 90 and aB == 90 and aC == 90 and aD == 90:
        return "rectangle"
    elif (a == b and b == c and c == d) or (a == c and b == d and a != d) and ((aA == aC and aB == aD) and (aA <= aB or aB <= aA)) and ((aA + aB and aC + aD) == 180):
        return "rhombus"
    else:
        return "not rectangle or square"


"""Rhombous has 4 sides with 2 matching <= angles and 2 matching obtuse angles

example

**********************************
********** aB                 aC *
*********                       **
********                       ***
*******                       ****
******                       *****
*****                       ******
****                       *******
***                       ********
**                       *********
* aA                 aD **********
**********************************




















"""






