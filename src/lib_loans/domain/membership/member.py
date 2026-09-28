"""A person registered to borrow from the library.

A member is someone the library has issued a card to — the human on the
borrowing side of the desk, known to the public as a *patron*. Membership
begins when front-desk staff register the person and hand over a card, and
the card travels with them across every loan and reservation they ever
make. The card number, not the person's name, is what the desk keys on:
names repeat and change, the card number does not.
"""

from dataclasses import dataclass
from typing import NewType

#: A member's library-card number — the identifier printed on the card and
#: scanned at the desk. Stable for the life of the membership.
MemberId = NewType("MemberId", str)


@dataclass(frozen=True)
class Member:
    """One registered borrower, identified by library-card number.

    Identity is the ``id`` (the card number); ``name`` is descriptive and
    may change (marriage, correction) without re-identifying the member. A
    member may hold several loans at once and any number of reservations,
    so the borrowing side of a loan or hold always points back here by
    card number rather than embedding the person's details. The
    business-facing synonym for a member is *patron* (the glossary term
    ``term.patron``), used interchangeably at the desk.

    Created when front-desk staff register a new borrower; the row is not
    deleted when a membership lapses, so historical loans remain navigable.
    """

    id: MemberId
    name: str
