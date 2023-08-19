"""
Write a program that prints out the two largest and two smallest elements of a list
called scores.

"""
scores = [100,23,45,6,677]
scores.sort()
print( 'Two smallest: ', scores[0], scores[1])
print( 'Two largest: ', scores[-1], scores[-2])