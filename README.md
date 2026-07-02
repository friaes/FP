# Foundations of Programming — Course Projects

Two Python projects built for the **Fundamentos da Programação** (Foundations of Programming) course at **Instituto Superior Técnico (IST)**, University of Lisbon, during the 2021–22 academic year.

The course is a first-year introduction to procedural and functional programming in Python, with a strong emphasis on **data abstraction**, **abstract data types (ADTs)**, defensive programming, and algorithmic thinking — building up from primitive types and control flow to recursion, higher-order functions, and file I/O.

Both projects were graded against an automated public/private test suite. The public tests used for grading are included in each project folder.

## Projects

| # | Project | Theme | Core concepts |
|---|---------|-------|---------------|
| 1 | [**Buggy Data Base**](./Projeto1) | Repairing a corrupted authentication database through five independent tasks | String manipulation, tuples, dictionaries, checksums, ciphers, exception handling |
| 2 | [**The Meadow**](./Projeto2) | A predator–prey ecosystem simulator | Abstract data types, the barrier abstraction, recursion, file I/O, ASCII rendering |

## Running the projects

Both projects are single-file, dependency-free Python 3 programs (standard library only).

```bash
# Project 1 — run the bundled public tests
cd Projeto1
python3 -c "from Projeto1_Rodrigo_Friaes import *; exec(open('FP2122P1_publictests.py').read())"

# Project 2 — run a simulation from an input file (see the Projeto2 README)
cd Projeto2
python3 Projeto2_Rodrigo_Friaes.py
```

See each project's own README for a full description, the task breakdown, and detailed usage.

## Repository layout

```
.
├── Projeto1/                      # Buggy Data Base
│   ├── Projeto1_Rodrigo_Friaes.py # solution
│   ├── FP2122P1_publictests.py    # provided public tests
│   └── FP2122P1.pdf               # original assignment (Portuguese)
├── Projeto2/                      # The Meadow
│   ├── Projeto2_Rodrigo_Friaes.py # solution
│   ├── FP2122P2_public_tests.py   # provided public tests
│   └── FP2122P2.pdf               # original assignment (Portuguese)
└── README.md
```
