def decrypt(text, n):
    if ((text is None) or text=="") or n<1:
        return text
    else:
        result=""
        s=int(len(text)/2)
        left=text[:s]
        right=text[s:]
        takeFromLeft=False
        li=0
        ri=0
        while li < len(left) or ri < len(right):
            if takeFromLeft:
                result+=left[li]
                li+=1
            else:#takeFromRight
                result+=right[ri]
                ri+=1
            takeFromLeft = not takeFromLeft
        return decrypt(result,n-1)
def encrypt(text, n):
    if ((text is None) or text=="") or n<1:
        return text
    else:
        return encrypt(text[1::2]+text[::2],n-1)

"""
Description:

For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty

Have fun coding it and please don't forget to vote and rank this kata! :-)
"""
