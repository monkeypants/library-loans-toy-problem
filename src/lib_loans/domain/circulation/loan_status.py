"""The lifecycle states a loan moves through, from checkout to closure.

This is the controlled vocabulary for where a loan stands: it leaves the
desk *out*, and ends either *returned* (the volume came back) or *lost*
(it never did). *Overdue* is not a fourth destination — it is *out* past
its due date, a flag that triggers reminders rather than a separate fate.
The vocabulary exists so that "what state is this loan in?" has one agreed
set of answers across the desk, the reminders process, and the catalogue.
"""

from enum import StrEnum


class LoanStatus(StrEnum):
    """A loan's lifecycle state.

    Opens *out* and is terminal at *returned* or *lost*. Legal
    transitions: ``out -> returned``, ``out -> overdue`` (the due date
    passed while still out), ``overdue -> returned``, ``overdue -> lost``.
    ``returned`` and ``lost`` are terminal — a closed loan never reopens.

    ``overdue`` is a *derived* state: a loan is overdue precisely when it
    is still out and its due date is in the past, so it is computed from
    the loan's dates rather than set independently. Callers must not treat
    ``overdue`` as mutually exclusive with the open/closed split — an
    overdue loan is still an open loan.
    """

    OUT = "out"
    OVERDUE = "overdue"
    RETURNED = "returned"
    LOST = "lost"
