"""MARC 21 codec — encode/decode catalogue records to the transmission format.

The library's catalogue is exchanged with other institutions as MARC 21
records (ANSI/NISO Z39.2). This package is the *codec*: its sole job is
conformance with that external standard, so unlike the domain model it
owns no business rules — every structure here exists because a clause of
the standard requires it, and the provenance the toolchain records points
*out* to those normative clauses rather than to internal sources.
"""
