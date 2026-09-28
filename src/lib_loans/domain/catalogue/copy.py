"""A physical volume on the shelf — one borrowable instance of a title.

A copy is the object a member actually carries home: a single bound volume
with its own barcode, sitting in one of possibly several identical volumes
of the same catalogued title. The distinction from the catalogued title is
the one the desk cares about — "is a copy free?" is a different question
from "do we hold this title?", and only copies are loaned. A copy is what
the desk scans when issuing a loan.
"""

from dataclasses import dataclass
from typing import NewType

from lib_loans.domain.catalogue.book import BookId

#: A copy's barcode — the sticker scanned at the desk, unique to one
#: physical volume even among identical copies of the same title.
CopyId = NewType("CopyId", str)


@dataclass(frozen=True)
class Copy:
    """One physical volume, identified by barcode.

    Identity is the ``id`` (the barcode); ``book`` is the foreign key to
    the :class:`~lib_loans.domain.catalogue.book.Book` title this volume is
    an instance of. Many copies share one book; each copy is on **at most
    one open loan at a time** — that invariant is what lets the desk answer
    "is a copy of this title available?" by checking whether any copy of
    the book has no open loan.

    Created when a physical volume is accessioned against an existing
    catalogued title; withdrawn (not deleted) when the volume is lost or
    discarded, so historical loans against it remain navigable.
    """

    id: CopyId
    book: BookId
