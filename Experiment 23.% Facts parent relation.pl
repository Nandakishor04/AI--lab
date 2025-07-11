% Facts
male(john).
male(paul).
male(mike).
male(tom).

female(mary).
female(lisa).
female(anna).
female(susan).

parent(john, paul).
parent(mary, paul).
parent(john, lisa).
parent(mary, lisa).

parent(paul, mike).
parent(anna, mike).
parent(paul, susan).
parent(anna, susan).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

grandfather(X, Y) :- parent(X, Z), parent(Z, Y), male(X).
grandmother(X, Y) :- parent(X, Z), parent(Z, Y), female(X).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).
