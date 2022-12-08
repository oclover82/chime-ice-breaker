"""Provides ice-breaker questions."""

import random

DEFAULT_ICE_BREAKERS = [
"Felicitations for the Season"
"Sterling Carillon"
"Circuitous Gambol of Festive Conifer"
"Awesome Hibernal Acreage"
"Altitudinous Celestials Acclaim"
"Senior Flattened by a Cloven Aviator"
"Covert Observation of Matriarch's Scandalous Osculation"
"Petite Birthplace"
"Sprightly Venerable Benefactor"
"Allegiants Proceed"
"Enquiry of Mutual Auditory Perception"
"Hushed Darkness"
"Noel - Envisage Blanched"
"Inaugural Yule"
"Royal Eastern Trio"
"Planetary Jubilance"
"Theurgical Cool Guy"
"Matchless season"
"Full-Grown Enumeration of Holiday Hopes"
"Commencement of Yuletide Complexion"
]


def get_random():
    """Provide random ice breaker question."""
    return random.choice(DEFAULT_ICE_BREAKERS)
