from fractions import Fraction as frac

def mixed_fraction(s):
    sNum = int(s.split('/')[0])
    sDen = int(s.split('/')[1])
    sRes = sNum / sDen
    divRes = abs(sNum) % abs(sDen)

    try:
        if int(sRes) == 0:
            return (f'{frac(sNum, sDen)}')
        elif divRes == 0:
            return (f'{int(sRes)}')
        else:
            return (f'{int(sRes)} {abs(frac(divRes, sDen))}')
    except TypeError:
            return (f'{int(sRes)} {abs(frac(int(divRes), sDen))}')
