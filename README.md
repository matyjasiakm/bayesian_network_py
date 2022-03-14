# Losowy generator oparty na sieci Bayesa
Implementacja losowego generatora danych, który działa zgodnie z rozkładem prawdopodobieństwa dla podanej sieci bayesowskiej. Podana sieć powinna opisywać zależności miedzy zmiennymi losowymi
(zero-jedynkowymi)
</br>

Do rozwiązania zadania został zaimplementowany algorytm MCMC z próbkowaniem Gibbsa w następującej postaci opisanej za pomocą listy kroków:
1. Podaj sieć Bayesa z zależnościami i tabelami prawdopodobieństw warunkowych oraz liczbę próbek.
2. Zainicjuj losowo stany początkowe każdego z węzłów, a liczbę dokonanych
   próbek na 0.
3. Wybierz losowo węzeł X z podanej sieci.
4. Wybierz losowo wartość X z prawdopodobieństwem P(X | otoczka markowa X) i przypisz wylosowaną wartość do węzła X.
5. Zwiększ liczbę próbek o jeden.
6. Jeżeli liczba dokonanych próbek jest mniejsza niż podana liczba próbek
   idź do punktu 3.
7. Zwróć wartości wszystkich węzłów.
   Po wielokrotnym wywołaniu algorytmu i każdorazowym pobieraniu informacji
   z węzłów, otrzymujemy dane których rozkład jest zgodny z podaną siecią bayesowską.