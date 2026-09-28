# MARC 21 Format for Bibliographic Data — conformance excerpt

*Reproduced clauses from the record-structure standard (ANSI/NISO Z39.2)
the catalogue exchange must conform with. Normative, externally
versioned, and outside this project's control — cited here by clause so
the codec's conformance is traceable.*

## §4 Record structure

### §4.2 Leader

The leader is the first field of the record. It consists of 24 octets
(character positions 00-23) and is the only field of fixed length.

Character position 05 contains the record status: a single character,
where `n` denotes a new record, `c` a corrected or revised record, and
`d` a deleted record.

### §4.3 Directory

The directory follows the leader. Each entry is a fixed 12 octets and
gives the tag, length, and starting character position of one variable
field. Entries appear in ascending order of the tags they point to.

## §5 Variable fields

Variable fields are transmitted in ascending tag order, and each variable
field is closed by a field terminator. The record as a whole is closed by
a record terminator.
