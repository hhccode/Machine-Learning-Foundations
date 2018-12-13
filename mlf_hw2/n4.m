syms x3 x4

N = 10000
d = 50
delta = 0.05

ans1 = sqrt((8/N) * log(4*(2*N).^d/delta))
ans2 = sqrt((2*log(2*N*N.^d))/N) + sqrt((2/N) * log(1/delta)) + 1/N

ans3 = solve(sqrt(1/N*(2*x3+log(6*(2*N)^d/delta))) == x3, x3)

ans4 = solve(sqrt(1/(2*N)*(4*x4*(1+x4)+log(4)+d*log((N.^2))-log(delta))) == x4, x4)

ans5 = sqrt(16/N*log(2*N.^d/sqrt(delta)))

