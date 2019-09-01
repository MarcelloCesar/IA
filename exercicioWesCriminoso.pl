hostil(cuba).
arma(misseis).
americano(west).
vende(west, misseis, cuba).
criminoso(X) :- vende(X, AlgumaCoisa, Alguem), hostil(Alguem), arma(AlgumaCoisa), americano(X).