def simplify(poly):
    multi = {}
    signs = []
    if poly == "":
        return ""
    if poly[0]=='-' or poly[0]=='+':
        signs.append(poly[0])
        poly=poly[1:]
    else:
        signs.append('+')
    for char in poly:
        if char=='-' or char=='+':
            signs.append(char)
    monomials = poly.replace('-',' ').replace('+',' ').split(' ')
    #so now we have for example ["3xy","12ab","2x"] and ['-','-','+']
    for mono in monomials:
        #so lets split for example "12ab",'-' and put in in multi as "ab":-12
        numberString=""
        letterString=""
        for char in mono:
            if char in "0123456789":
                numberString+=char
            else:
                letterString+=char
        key = ''.join(sorted(letterString))
        if numberString=="":
            numberString="1"
        sign=1
        if signs.pop(0)=='-':
            sign=-1
        value = sign*int(numberString)
        #so adding to multi
        if not key in multi:
            multi[key] = value
        else:
            multi[key] += value
    #now prepare end string to return it
    keys_order = {} #yolo
    ki=0
    for key in multi:
        keys_order[ki]=key
        ki+=1
    for i in range(ki):#1st el index
        for j in range(i+1,ki):#2nd el index
            #check number of chars
            if len(keys_order[i])>len(keys_order[j]):
                tmp = keys_order[i]
                keys_order[i] = keys_order[j]
                keys_order[j] = tmp
            #lexicosomething
            elif len(keys_order[i])==len(keys_order[j]):
                for c in range(len(keys_order[i])):
                    if keys_order[i][c] > keys_order[j][c]:
                        tmp = keys_order[i]
                        keys_order[i] = keys_order[j]
                        keys_order[j] = tmp
                        break
    #FINISH IT!
    result=""
    for key in range(ki):
        n = keys_order[key]
        if multi[n]==0:
            continue
        elif multi[n]<0:
            if multi[n]==-1:
                result+="-"+n
            else:
                result+=str(multi[n])+n
        else:
            if multi[n]==1 and result=="":
                result+=n
            elif result=="":
                result+=str(multi[n])+n
            elif multi[n]==1:
                result+="+"+n
            else:
                result+="+"+str(multi[n])+n
    return result
"""
Description:

When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function:

simplify(poly)

that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

    All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:

    "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

    All monomials appears in order of increasing number of variables, e.g.:

    "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

    If two monomials have the same number of variables, they appears in lexicographic order, e.g.:

    "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

    There is no leading + sign if the first coefficient is positive, e.g.:

    "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

Good Work :)
"""
