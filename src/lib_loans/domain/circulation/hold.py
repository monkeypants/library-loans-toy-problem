"""A member's request to borrow a title that has no copy free right now.

A hold is the waiting-list entry the desk records when a member wants a
title but every copy is out: the member asks, and the library promises the
next returned copy. It is a request against a title, which is what
distinguishes it from a loan — a loan is a copy already in hand, a hold is
a claim on a copy not yet available. A hold comes into existence only when
demand outruns the copies on the shelf.
"""

from dataclasses import dataclass
from datetime import date

from lib_loans.domain.catalogue.book import BookId
from lib_loans.domain.membership.member import MemberId


@dataclass(frozen=True)
class Hold:
    """One reservation, identified by member, title, and when placed.

    A single hold is uniquely ``(book, member, placed_at)``. The hold
    references the :class:`~lib_loans.domain.catalogue.book.Book` *title*,
    **not** a :class:`~lib_loans.domain.catalogue.copy.Copy` —
    deliberately, because at the moment a hold is placed no copy is free to
    assign. A specific copy is bound only later, when one is returned and
    the hold is fulfilled by issuing a loan; until then the title-level
    reference is the placeholder standing in for "whichever copy comes back
    first".

    ``status`` is a free-form ``str`` today, drawn from a fixed vocabulary
    — ``waiting`` (queued, no copy yet) / ``ready`` (a copy is held at the
    desk for collection) / ``collected`` (turned into a loan) / ``expired``
    (the ready copy went uncollected) / ``cancelled`` (the member withdrew
    the request). It should become a ``StrEnum`` (mirroring
    :class:`~lib_loans.domain.circulation.loan_status.LoanStatus`) once the
    states stop churning; until then callers must treat any value outside
    that set as a data error.

    Created when a member asks for a title whose every copy is on loan;
    discharged when the next copy is returned and handed to the member at
    the front of the queue.
    """

    book: BookId
    member: MemberId
    placed_at: date
    status: str
