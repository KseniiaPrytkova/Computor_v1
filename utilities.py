#!/usr/bin/env python

import sys

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
