"""A catalogued title the library holds — a work, not a physical object.

A book is the bibliographic record a member searches for and asks about:
the title, by this author, with this catalogue number. It is distinct from
the physical volumes on the shelf — the library may own several identical
copies of one title, and members borrow a copy, never the title itself. A
book exists from the moment it is catalogued, whether or not any copy of it
is currently on the shelf.
"""

from dataclasses import dataclass
from typing import NewType

#: A book's catalogue accession number — the identifier the cataloguer
#: assigns to a title when it enters the collection.
BookId = NewType("BookId", str)


@dataclass(frozen=True)
class Book:
    """One catalogued title, identified by catalogue accession number.

    Identity is the ``id`` (the accession number); ``title`` is the
    human-facing label staff and members search on. A book is the
    *title-level* record — one book maps to many
    :class:`~lib_loans.domain.catalogue.copy.Copy` rows, one per physical
    volume the library owns. Loans never reference a book directly (a
    member borrows a specific volume); reservations do, because a
    :class:`~lib_loans.domain.circulation.hold.Hold` is placed against the
    title before any particular copy is assigned.

    Created when a cataloguer accessions a new title; persists even after
    the last copy is withdrawn, so the catalogue and past loans stay
    intact.
    """

    id: BookId
    title: str
