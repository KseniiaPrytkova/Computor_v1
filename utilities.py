#!/usr/bin/env python

import sys

# def ntsqrt(n):
#     sgn = 0
#     if n < 0:
#         sgn = -1
#         n = -n
#     val = n
#     while True:
#         last = val
#         val = (val + n / val) * 0.5
#         if comp_abs(val - last) < 1e-9:
#             break
#     if sgn < 0:
#         return complex(0, val)
#     return val

def comp_abs(nb):
	if (nb < 0):
		nb *= -1
	return (nb)

def comp_sqrt(nb):
	if nb == 0 or nb == 1:
		return nb
	calc = nb
	diff = calc
	calc = 0.5 * (calc + nb / calc)
	while calc != diff:
		diff = calc
		calc = 0.5 * (calc + nb / calc)
	return calc