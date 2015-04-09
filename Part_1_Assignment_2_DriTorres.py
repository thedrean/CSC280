#/**********************************************************************/
#/* CSC 280 Programming Project 2 Part 1                                          */
#/*                                                                                                      */
#/* modifier:       Dri Torres                                                                */
#/*                                                                                                       */
#/* filename: Part_1_Assignment_2_DriTorres.py                                */
# /* modified from: CSC 280 HW #2 lab                                               */
#/* date last modified: 09/29/2013                                                    */
#/*                                                                                                       */
#/* action: computes expressions between variables                          */
#/*                                                                                                       */
#/* input: defining variables a, b, c, t, x, y, and z                                */
#/* 							                         */
#/*                                                                                                       */
#/* output: computed expressions                                                      */
#/*                                                                                                       */
#/**********************************************************************/

# Prompt user for variable definitions
a = 10
b = 7
c = -3
t = .0725
x = 41.5
y = 5.25
z = 2.35

# Compute expressions including defined variables

A = (a - b) / (c * b)
B = (x - y) * (x - y) * (x - y)
C = (4 * z * z * z) + (3 * z * z) - 6
D = (40 * y) + (1.5 * y) * (x - 40)
E = (1 + t) * x
F = x + (x * t) - y

# Report computations

print A
print B
print C
print D
print E
print F

#-1
# 47634.765625
# 62.479
# 221.8125
# 44.50875
# 39.25875
