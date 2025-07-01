# teleporty

Simulácia stolovej hry Teleporty pre 2 hráčov v jazyku Python. Projekt vznikol ako zadanie na predmet PROG1.

## Popis hry

Hra sa hrá na hracej ploche veľkosti `n x n` (kde `5 <= n <= 10`). Každý hráč má jednu figúrku, ktorú sa snaží dostať z počiatočného políčka `+` na cieľové políčko `*`. Pohyb sa riadi hodením 6-strannej kocky.

Na hracej ploche sú náhodne rozmiestnené teleporty:
- Veľké písmená (A, B, …) označujú pozitívne teleporty (posun vpred),
- Malé písmená (a, b, …) označujú negatívne teleporty (posun späť).

Figúrky sa pohybujú hadovitým spôsobom – v nepárnych riadkoch zľava doprava, v párnych sprava doľava.

Vyhráva hráč, ktorý ako prvý dorazí presne na cieľové políčko.
