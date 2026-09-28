# library-loans-toy-problem

A toy problem, for testing/documentation.

A small discovery corpus about a lending library (`lib_loans`): its
canon, the sources and meetings it was learned from, the evidence read
from them, and a small Python package whose classes are canon too.
bugflow serves it as its first corpus, and its tests read it.

## What is here

- `pyproject.toml`: the `[tool.disco]` table that marks this directory
  as a corpus and says where each part lives.
- `discovery/canonical/`: the canon, one file per kind (codec,
  collections, glossary, personas, qualities).
- `discovery/sources/`, `discovery/meetings/`, `discovery/standards/`:
  what the canon was learned from.
- `discovery/evidence/`: what was read from each source through each
  lens.
- `src/lib_loans/`: the library's domain model and a MARC 21 codec,
  whose modules and classes are canon.
- `docs/`: the Sphinx site the canon renders into.
- `expected/`: the health report (`health.txt`) and the rendered pages
  (`rst.txt`) this corpus produced under disco-agent, kept as the
  expectation to test against.

## Where it came from

Copied from `tests/golden` in GoSource's disco-agent repository at
commit `64c57268`, where it was disco-agent's test and demo corpus.
GoSource released it under the GPL-3 on 2026-09-28. The files are
unchanged; disco-agent's lock file is left out, since the corpus
declares no dependencies.

## Licence

GPL-3.0. See `LICENSE`.
