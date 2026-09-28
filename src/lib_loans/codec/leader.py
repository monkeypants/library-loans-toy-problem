"""The 24-octet leader that opens every MARC 21 record.

The leader is the fixed-length head of a record: a run of exactly 24
characters whose positions are assigned, octet by octet, by the standard.
It is not the library's invention — its shape is dictated wholly by MARC
21 / Z39.2, which is why this module lives in the codec, not the domain.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Leader:
    """The fixed 24-octet leader of a MARC record.

    Always exactly 24 characters. The standard fixes the meaning of each
    position: ``record_length`` is the five-digit count at positions 00-04,
    ``record_status`` a single character at position 05 (``n`` new, ``c``
    corrected, ``d`` deleted), and ``record_type`` a single character at
    position 06. The remaining positions carry the indicator/subfield
    counts and the base address of data; this codec models the few its
    encoder writes and round-trips the rest verbatim.

    The leader is parsed first and parsed by position, never by delimiter —
    a malformed length here invalidates the whole record, so the codec
    rejects a leader that is not exactly 24 octets before reading further.
    """

    record_length: int
    record_status: str
    record_type: str
    base_address: int
