lib_loans — a rendered discovery corpus
=======================================

This is the bundled ``lib_loans`` reference corpus, rendered by
``disco_agent.app.sphinx`` — a live example of what disco-agent produces from
a ``discovery/`` tree. It is the same calibration corpus the toolchain's
tutorial walks; here you can browse the finished output rather than read about
it.

.. note::

   Built by ``make docs-corpus`` from ``tests/golden/``. Every page below is
   generated from that corpus's evidence and canonical model — nothing here is
   hand-written except these index pages.

* **Sources** — every document the corpus draws on, and what each one informs.
* **Evidence by referent** — the reverse view: for each thing the corpus
  describes, the sources that say something about it.
* **Glossary** and **Personas** — two canonical views rendered straight from
  the model.
* **Collections** — a host-declared canonical kind, rendered as a catalogue by
  the generic directive rather than a bespoke one.

.. toctree::
   :maxdepth: 2

   sources/index
   evidence
   glossary
   personas
   collections
