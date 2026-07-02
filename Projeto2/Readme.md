# Project 2 — The Meadow (O Prado)

A **predator–prey ecosystem simulator** written in Python. A rectangular meadow, walled in by mountains, is populated by animals that move, eat, breed, and die over discrete time steps (*generations*). The population evolves according to fixed rules, and the state of the meadow can be rendered as ASCII art after each generation.

This is the project where the course introduces **abstract data types (ADTs)** and the **barrier abstraction**: the simulation logic is written entirely against ADT operations and never touches the underlying representation directly. The whole thing is essentially a cellular automaton in the spirit of *Wa-Tor* / Conway's Game of Life.

## Design: three abstract data types

Each ADT is built with the canonical set of operations — **constructors**, **selectors**, **modifiers**, **recognisers**, **tests**, and **transformers** — so that the rest of the program depends only on the interface, not the representation.

### `posicao` — a position on the grid
An `(x, y)` coordinate. Includes `cria_posicao`, selectors `obter_pos_x`/`obter_pos_y`, `eh_posicao`, `posicoes_iguais`, and higher-level helpers `obter_posicoes_adjacentes` (returns the neighbours in the fixed order up/right/down/left) and `ordenar_posicoes` (reading order).

### `animal` — a predator or a prey
Holds species, age, reproduction frequency, hunger, and feeding frequency. Predators have a feeding frequency > 0; prey have 0. Includes constructors, selectors, modifiers (`aumenta_idade`, `aumenta_fome`, `reset_idade`, `reset_fome`), recognisers (`eh_predador`, `eh_presa`, `eh_animal_fertil`, `eh_animal_faminto`), transformers to a single character (`animal_para_char`) or a readable string (`animal_para_str`), and `reproduz_animal`.

### `prado` — the meadow itself
Stores dimensions, obstacles (rocks), and the animals with their positions. Includes constructors with full validation, selectors (`obter_numero_predadores`, `obter_numero_presas`, `obter_animal`, …), modifiers (`inserir_animal`, `eliminar_animal`, `mover_animal`), position recognisers (`eh_posicao_livre`, `eh_posicao_obstaculo`, `eh_posicao_animal`), and `prado_para_str`, which renders the meadow as ASCII.

## Simulation rules

Each generation, every animal (visited in reading order) takes a turn:

- **Movement** — an animal moves to an adjacent free cell chosen deterministically from its position's numeric value. Predators prefer an adjacent prey.
- **Feeding** — a predator that lands on a prey eats it and resets its hunger. A predator that goes too long without eating starves and dies.
- **Reproduction** — an animal that reaches its reproduction age and moves leaves a newborn of the same species behind, resetting its own age.

The deterministic move selection (based on a cell's numeric index) makes runs fully reproducible.

## Requirements

Python 3 — standard library only, no external dependencies.

## Usage

The main entry point is `simula_ecossistema(file, generations, verbose)`:

- `file` — path to a configuration file describing the meadow.
- `generations` — maximum number of generations to simulate.
- `verbose` — if `True`, prints the meadow every time the predator/prey counts change; if `False`, prints only the final state.

It returns a `(predators, prey)` tuple and prints snapshots along the way.

### Input file format

Three-plus lines, each a Python literal:

```
(dim_x, dim_y)
((rock_x1, rock_y1), (rock_x2, rock_y2), ...)
('species', reproduction_freq, feeding_freq, (pos_x, pos_y))
('species', reproduction_freq, feeding_freq, (pos_x, pos_y))
...
```

Line 1 is the meadow size, line 2 the obstacles, and each remaining line one animal (feeding frequency `0` = prey, `> 0` = predator).

### Example

```python
from Projeto2_Rodrigo_Friaes import simula_ecossistema

# simulate up to 10 generations, printing on every population change
predators, prey = simula_ecossistema('ecossistema.txt', 10, True)
```

A rendered meadow looks like this — `@` is a rock, uppercase letters are predators, lowercase are prey:

```
+--------+
|........|
|..r.....|
|.....@..|
|...L....|
+--------+
```

Run the bundled public tests:

```bash
python3 -c "from Projeto2_Rodrigo_Friaes import *; exec(open('FP2122P2_public_tests.py').read())"
```

## Files

- `Projeto2_Rodrigo_Friaes.py` — the solution (all three ADTs plus the simulator).
- `FP2122P2_public_tests.py` — provided public tests with expected outputs in comments.
- `FP2122P2.pdf` — the original assignment brief (Portuguese).
