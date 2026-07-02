# Project 1 — Buggy Data Base (BDB)

A set of Python functions that repair a corrupted user-authentication database. The database (the *Buggy Data Base*) stores login information and has started wrongly rejecting legitimate users because of unknown corruption. The project is split into **five independent tasks**, each recovering a different part of the data.

This project focuses on **procedural programming without abstract data types**: raw strings, tuples, and dictionaries, plus rigorous argument validation with exceptions.

## The five tasks

### 1. Documentation repair — string manipulation
The documentation was corrupted by "bursts" of adjacent same-letter uppercase/lowercase pairs (e.g. `aA`, `Bb`) inserted into words. These pairs cancel out, much like matter and antimatter.

- `corrigir_palavra(s)` — repeatedly removes adjacent case-pairs of the same letter until the word stabilises (`'cCdatabasacCADde'` → `'database'`).
- `eh_anagrama(s1, s2)` — tests whether two words are anagrams (case-insensitive).
- `corrigir_doc(s)` — cleans a full document and removes later words that are anagrams of an already-seen word, keeping the first occurrence.

### 2. PIN discovery — grid navigation
The database PIN is entered on a 3×3 keypad (`1`–`9`) by moving between adjacent buttons. Each instruction line is a string of moves `C`/`B`/`E`/`D` (up/down/left/right); moves that would leave the pad are ignored. Each line yields one PIN digit.

- `obter_posicao(caracter, num)` — applies a single move to a button, respecting the pad edges.
- `obter_digito(cadeia, num)` — applies a full line of moves and returns the resulting button.
- `obter_pin(t)` — turns a tuple of instruction strings into the full PIN tuple, starting from button `5`.

### 3. Data-coherence check — validation & checksums
Each database entry is a triple `(cipher, control_sequence, security_sequence)`. An entry is valid only if its **control sequence** matches a checksum computed from the cipher: the five most frequent letters, ordered by decreasing frequency and then alphabetically, wrapped in `[...]`.

- `eh_entrada(entrada)` — structural validator for a single entry.
- `validar_cifra(s1, s2)` — recomputes the checksum from the cipher and compares it to the stored control sequence.
- `filtrar_bdb(lista)` — returns the entries that fail the coherence check.

### 4. Content decryption — a Caesar-style cipher
Valid ciphers are decrypted using a **security number** (the smallest positive difference between any pair of numbers in the security sequence). Letters shift by the security number, with an extra offset that depends on whether the character sits at an even or odd index; hyphens become spaces.

- `obter_num_seguranca(t)` — smallest positive pairwise difference in a tuple.
- `decifrar_texto(s, num)` — decrypts one cipher string.
- `decifrar_bdb(lista)` — decrypts every valid entry in the database.

### 5. Password debugging — rule validation
Each user has a password and a validation rule. A password is valid if it contains at least three lowercase vowels, has at least one letter repeated in two consecutive positions, and contains a specified character a permitted number of times.

- `eh_utilizador(dic)` — validates the structure of a user record.
- `eh_senha_valida(senha, regra)` — checks a password against its rule (with helper `letras_consecutivas`).
- `filtrar_senhas(lista)` — returns the sorted names of users whose passwords are invalid.

## Requirements

Python 3 — standard library only, no external dependencies.

## Usage

The functions are meant to be imported and composed. A quick example:

```python
from Projeto1_Rodrigo_Friaes import corrigir_doc, obter_pin

corrigir_doc('BuAaXOox...')          # -> 'Buggy data base has wrong data'
obter_pin(('DD', 'B', 'CCE', 'LD'))  # -> a tuple of PIN digits
```

Run the bundled public tests:

```bash
python3 -c "from Projeto1_Rodrigo_Friaes import *; exec(open('FP2122P1_publictests.py').read())"
```

Every function that is documented as validating its input raises
`ValueError('<function_name>: argumento invalido')` on malformed arguments, matching the assignment specification.

## Files

- `Projeto1_Rodrigo_Friaes.py` — the solution (all five tasks).
- `FP2122P1_publictests.py` — provided public tests with expected outputs in comments.
- `FP2122P1.pdf` — the original assignment brief (Portuguese).
