"""A copy checked out to a member for a fixed loan period.

A loan is the record the desk creates when a volume leaves the building: a
named member takes a specific copy, due back by a date. It is the unit of
circulation the whole desk turns on. A loan is distinct from a hold — a
hold is a request for a title with no copy free, a loan is a copy already
in someone's hands.
"""

from dataclasses import dataclass
from datetime import date, datetime

from lib_loans.domain.catalogue.copy import CopyId
from lib_loans.domain.circulation.loan_status import LoanStatus
from lib_loans.domain.membership.member import MemberId


@dataclass(frozen=True)
class Loan:
    """One checkout, identified by the copy borrowed and when it left.

    A single loan is uniquely the pair ``(copy, checked_out_at)`` — the
    same copy is loaned again and again over its life, each checkout a
    distinct loan. ``checked_out_at`` is the *timestamp* the copy left the
    desk, not a calendar date: a copy borrowed and returned in the morning
    can be loaned again the same afternoon, and the two loans are distinct
    only because their checkout moments differ. ``member`` records who
    holds it; ``due`` is the calendar date it is expected back (day
    granularity — overdue is reckoned per day); ``returned_at`` is empty
    while the loan is open and carries the return timestamp once closed.

    A copy is on **at most one open loan at a time** (the invariant
    :class:`~lib_loans.domain.catalogue.copy.Copy` relies on). ``status``
    tracks the lifecycle through
    :class:`~lib_loans.domain.circulation.loan_status.LoanStatus`
    (``out / overdue / returned / lost``); ``returned_at`` is set if and
    only if ``status`` is ``returned``. ``overdue`` is derived — a loan is
    overdue when it is still ``out`` and ``due`` has passed — so it is not
    stored independently of the dates.

    Created at the desk when staff issue a copy to a member; never deleted
    on return — the closed row is the borrowing history a member can ask
    to see.
    """

    copy: CopyId
    member: MemberId
    checked_out_at: datetime
    due: date
    status: LoanStatus
    returned_at: datetime | None = None
