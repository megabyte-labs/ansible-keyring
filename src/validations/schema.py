"""
schema is a library for validating python data structures

TODO: study this one a bit more. lots of useful stuff here!
"""
from schema import Schema, Use, And, Optional


schema = Schema([{
    "name": And(str, len),
    "age":  And(Use(int), lambda n: 18 <= n <= 99),
    Optional("gender"): And(
        str, Use(str.lower), lambda s: s in ("squid', 'kid")
    )
}])

data = [
    {"name": "Sue", "age": "28", "gender": "Squid"},
    {"name": "Sam", "age": "42"},
    {"name": "Sacha", "age": "20", "gender": "KID"}
]

# Check if valid...
schema.is_valid(data)

# Return validated data...
validated = schema.validate(data)
