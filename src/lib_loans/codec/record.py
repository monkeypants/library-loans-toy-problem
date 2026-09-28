"""A whole MARC 21 record: a leader, a directory, and variable fields.

The record is the unit the catalogue exchanges. Its on-the-wire form is
prescribed by MARC 21 / Z39.2: a 24-octet leader, then a directory of
fixed-width entries, then the variable fields the directory points into,
each closed by a field terminator and the record by a record terminator.
This module models that structure so the codec can read a record other
institutions sent and emit one they can read back.
"""

from dataclasses import dataclass, field

from lib_loans.codec.leader import Leader


@dataclass(frozen=True)
class Marc21Record:
    """One bibliographic record in MARC 21 transmission format.

    Composes a :class:`~lib_loans.codec.leader.Leader` with the record's
    variable fields, keyed by their three-digit tag (``245`` title
    statement, ``100`` main entry, …). ``fields`` preserves tag order: the
    standard transmits fields in ascending tag order and the directory's
    entries must agree, so the codec keeps insertion order and does not
    re-sort on the reader's behalf.

    The record is *self-describing through its directory*, not through any
    schema the library holds: the byte offsets in the directory are the
    only index into the variable fields, so the codec rebuilds the
    directory from ``fields`` on encode and trusts it on decode. Conformance
    is the whole contract — a record this codec emits must be one any other
    Z39.2 reader accepts, and vice versa.
    """

    leader: Leader
    fields: dict[str, str] = field(default_factory=dict)
