# CSE464 — Data Structures and Algorithms | Instructor Manual

**Academic year:** 2026–2027  
**Prepared by:** Dr. Pronaya Bhattacharya  
**License:** MIT

## How to use

Each module folder contains standalone Python `.py` programs, a `PROGRAM_INDEX.md`, and an instructor Google Colab notebook with algorithm, implementation logic, executable code, sample execution, expected output, and a dry-run trace. Programs are reference solutions, not starter templates. Students should develop their own code rather than submit copied solutions.

```bash
python Module_1/linear_search.py
python -m unittest discover -s tests -v
```

Open a `Module_X_...ipynb` file in [Google Colab](https://colab.research.google.com/) using **File → Upload notebook**, or upload this repository to GitHub and select **Open in Colab**.

## Curriculum boundary

Module I: foundations, complexity and searching. Module II: array addressing, stacks, expressions and queues. Module III: linked lists. Module IV: trees. Module V: sorting, graphs and hashing. Enrichment challenges reflect the supplied detailed notes, including MSTs and shortest paths in Module V. `program_manifest.json` documents mapping. Not every descriptive/MCQ question translates into a programming task; quantitative derivations are represented as demonstrations where appropriate.

## Scope and limitations

Core educational implementations favor clarity and explicit invariants. Some advanced operations (e.g. complete AVL deletion, full B-tree deletion and B+ deletion/redistribution) are **not included** as complete implementations; they remain assignment extensions. B+ tree implements insert, lookup and range scan. Quadratic hashing file demonstrates probe sequences, not full tables with deletion. Asymptotic complexity should be derived by students; observed timings are machine-dependent.

## Testing and reproducibility

Standalone examples are checked for successful execution; `tests/` contains behavioral regression cases. Python 3.10+; no non-standard packages required.

## Licensing

MIT licensing applies to the original code and documentation in this repository. The provided classroom PDF notes are not redistributed in the repository. Attribution and third-party licensing obligations for material independently added later remain with contributors.
