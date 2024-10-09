    Objectif
Will has a low IQ. In order to show everyone what he is made of, he decided to write his own programming language. However, his low IQ got the better of him and he implemented the order of operations incorrectly!

From highest to lowest priority, here are the operators and what they mean:
* \- (Unary): Negation
* \+ : Addition
* / : Division
* \- : Subtraction
* \* : Multiplication

For example, the statement 6+-3*5 would be interpreted as (6 + (-3)) * 5 because - (Unary) has a higher priority than +, which has a higher priority than *.

Your goal is to evaluate the given expression and output the correct answer with these jumbled order of operations.

    Entrée

A string expression containing the expression you need to evaluate. The expressions contains only decimal digits and operators. No whitespace or parentheses.

    Sortie
A number representing the result of the expression.

    Contraintes
1 <= length of expression <= 200
Operations are left-associative.

    Exemple
Entrée

>1+2

Sortie

>3

--

>1+2

>3
---
>3*2+5

>21
---

>3*-4/2

>-6
---

>42

>42
---

>-42

>-42
---

>540-6+5-40*6+87+9*3*62+1+10-3620/-44+54+-9*8-4

>-2123007192
---

>2*3-18/1+5/3-1*2

>4
---

>5*2+3+4+5+6-7-8-9-10+11+12+13+14+15-16-20-28+35+555-487

>-6100
