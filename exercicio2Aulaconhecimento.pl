passaro(tweety).
peixe(goldie).
minhoca(molie).

gosta(X,Y) :- passaro(X), minhoca(Y).
gosta(X,Y) :- gato(X), (passaro(Y) ; peixe(Y)).

amigos(X,Y) :- gosta(X,Y), gosta(Y,X).
amigos(silvester,eu).

come(silvester,Y) :- gosta(silvester,Y).

gato(silvester).
