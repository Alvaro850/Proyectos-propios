clc;
I = eye(2);
syms x1  
syms x2
syms x_1
syms x_2
syms k
syms u
syms b
syms m
syms y_1
syms s
A = [0 1;-k/m -b/m];
B = [0;1/m];
C = [0 1];
D = [0];
xt = [x1;x2];
x_t = (A*xt)+B*u;
G(s) = C * inv(s*I-A)*B+D; 
