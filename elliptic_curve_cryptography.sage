# Good prime char and elliptic curve to try: see page 77 in 
# Recommendation for Random Number Generation Using Deterministic Random Bit Generators, by Elaine Barker and John Kelsey
# http://csrc.nist.gov/publications/nistpubs/800-90A/SP800-90A.pdf 
# 
# 


F = FiniteField(31)
C = EllipticCurve(F, [-3,3])   # [a,b] for y^2 = x^3 + ax + b 
print(C)               # print the equation of the elliptic curve in finite characteristic
print(C.cardinality()) # number of integral solutions mod 31
print(C.points()[:25]) # if the last coordinate equals 0, this is the point at infinity.
G = C.point((2,25))    # pick one of the points on C
G                      # print this point 
G.order()              # the order of the generator = the number of points on the curve

[p for p in C.points() if (p.order() < 20)]

[(p.order(), p) for p in C.points() if (p.order() < 10)] # prints the order of the points and the point

sorted([(p.order(), p) for p in C.points() if (p.order() < 20)])  #sort the points in ascending order

H = C.point((29,30))
H.order()
pts = [ H*x for x in range(H.order())]  # multiply H by a scalar from 0 to H.order()-1 to get all the iterated points
pts


points = [G*x for x in range(G.order())] # multiply G by a scalar from 0 to G.order()-1 to get all the iterated points
points 



plot(pts[0])+plot(pts[1])+plot(pts[2])+plot(pts[3])+plot(pts[4]) # plot all 5 points

sum([plot(i) for i in pts])  # plot all 5 points



plot_orange = sum([plot(i, hue = 0.1) for i in pts])   # plot the points in the subgroup of C in orange
plot(plot_orange, aspect_ratio = 1 ) # x and y-axes are proportional


plot((plot(C)+ plot(plot_orange)), aspect_ratio = 1)



#
# Output: 
#
# Elliptic Curve defined by y^2 = x^3 + 28*x + 3 over Finite Field of size 31
# 25
# [(0 : 1 : 0), (1 : 1 : 1), (1 : 30 : 1), (2 : 6 : 1), (2 : 25 : 1), (5 : 12 : 1), (5 : 19 : 1), (14 : 15 : 1), (14 : 16 : 1), (15 : 4 : 1), (15 : 27 : 1), (19 : 4 : 1), (19 : 27 : 1), (20 : 10 : 1), (20 : 21 : 1), (21 : 5 : 1), (21 : 26 : 1), (22 : 13 : 1), (22 : 18 : 1), (28 : 4 : 1), (28 : 27 : 1), (29 : 1 : 1), (29 : 30 : 1), (30 : 6 : 1), (30 : 25 : 1)]
# (2 : 25 : 1)
# 25
# [(0 : 1 : 0), (1 : 1 : 1), (1 : 30 : 1), (29 : 1 : 1), (29 : 30 : 1)]
# [(1, (0 : 1 : 0)), (5, (1 : 1 : 1)), (5, (1 : 30 : 1)), (5, (29 : 1 : 1)), (5, (29 : 30 : 1))]
# [(1, (0 : 1 : 0)), (5, (1 : 1 : 1)), (5, (1 : 30 : 1)), (5, (29 : 1 : 1)), (5, (29 : 30 : 1))]
# 5
# [(0 : 1 : 0), (29 : 30 : 1), (1 : 30 : 1), (1 : 1 : 1), (29 : 1 : 1)]
# [(0 : 1 : 0), (2 : 25 : 1), (14 : 15 : 1), (20 : 21 : 1), (19 : 27 : 1), (29 : 1 : 1), (5 : 19 : 1), (28 : 27 : 1), (21 : 26 : 1), (22 : 18 : 1), (1 : 1 : 1), (15 : 4 : 1), (30 : 25 : 1), (30 : 6 : 1), (15 : 27 : 1), (1 : 30 : 1), (22 : 13 : 1), (21 : 5 : 1), (28 : 4 : 1), (5 : 12 : 1), (29 : 30 : 1), (19 : 4 : 1), (20 : 10 : 1), (14 : 16 : 1), (2 : 6 : 1)]
#
 
