#! /usr/bin/env python3

import argparse


# create an ArgumentParser object ('parser') that will hold all the information necessary
# to parse the command line
parser = argparse.ArgumentParser(description = 'this script returns the Fibonacci number at a specific position in the Fibonacci sequence')


# add positional (required) arguments
parser.add_argument("num", hlep="the fibnocci number you want to get")

#add optional argument
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-s", "--simple", action="store_true", help="print simple output(defult)")

#parse the arguments
args = parser.parse_args()

#this script returns the Fibonacci number at a specific position in the Fibonacci sequence



#calculate the Fibonacci number
a,b = 0,1

for i in range(num):
	a,b = a+b

#simple output
#print(num,a)

#verbose output
#print("for position", num, "the Fibonacci number is", a)


if args.verbose:
	#verbose output
	print("for position", num, "the Fibonacci number is", a)

else:
	#simple output
	print(num, a)

