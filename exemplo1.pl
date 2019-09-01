ultimo([X|[]]):-  !.
ultimo([_|Y]):- ultimo(Y).
ultimo(X, Y):- X is ultimo(Y)