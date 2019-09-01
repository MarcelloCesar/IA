gosta(joao, X):- comida(X).
comida(arroz).
comida(maca).
comida(Y) :- come(X, Y), continuaVivo(X).
come(pedro, carne).
come(maria, X):- come(pedro, X).
continuaVivo(pedro).

