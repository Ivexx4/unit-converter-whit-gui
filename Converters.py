"""
Unit Converters Module

This module implements specific converter instances using the base Converter class.
It provides converters for Temperature, Length, Weight, and Volume units.

Each converter is an instance of the Converter class, initialized with a dictionary
of units and their conversion factors. The conversion factors are specified as
tuples of (scale_factor, offset).

Available Converters:
    - Temperature: Convert between temperature scales (Celsius, Fahrenheit, Kelvin, etc.)
    - Length: Convert between length units (meters, feet, inches, etc.)
    - Weight: Convert between weight/mass units (kilograms, pounds, etc.)
    - Volume: Convert between volume units (liters, gallons, etc.)

Example Usage:
    >>> from Converters import Temperature
    >>> Temperature.convert(25, "ºC", "°F")
    77.0
"""

from base_class import Converter

# Temperature converter - Converts between different temperature scales
# Base unit: Celsius (ºC) with scale factor 1 and offset 0
Temperature = Converter({
    # --- 1. Base Unit & Synonyms ---
    "ºC": (1, 0),  # Base Unit
    "C": (1, 0),  # Synonym
    "Celsius": (1, 0),  # Synonym

    # --- 2. Common Scales ---
    "°F": (1.8, 32),
    "F": (1.8, 32),  # Synonym (32/212 scale)
    "Fahrenheit": (1.8, 32),  # Synonym (32/212 scale)
    "ºR": (1.8, 491.67),  # Rankine
    "Rankine": (1.8, 491.67),  # Synonym

    # --- 3. Kelvin (SI Absolute) & SI Prefixes ---
    "K": (1, 273.15),
    "Kelvin": (1, 273.15),  # Synonym
    # Multiples
    "daK": (1e-1, 273.15e-1),
    "hK": (1e-2, 273.15e-2),
    "kK": (1e-3, 273.15e-3),
    "MK": (1e-6, 273.15e-6),
    "GK": (1e-9, 273.15e-9),
    "TK": (1e-12, 273.15e-12),
    "PK": (1e-15, 273.15e-15),
    "EK": (1e-18, 273.15e-18),
    "ZK": (1e-21, 273.15e-21),
    "YK": (1e-24, 273.15e-24),
    "RK": (1e-27, 273.15e-27),
    "QK": (1e-30, 273.15e-30),
    # Submultiples
    "dK": (1e1, 273.15e1),
    "cK": (1e2, 273.15e2),
    "mK": (1e3, 273.15e3),
    "µK": (1e6, 273.15e6),
    "nK": (1e9, 273.15e9),
    "pK": (1e12, 273.15e12),
    "fK": (1e15, 273.15e15),
    "aK": (1e18, 273.15e18),
    "zK": (1e21, 273.15e21),
    "yK": (1e24, 273.15e24),
    "rK": (1e27, 273.15e27),
    "qK": (1e30, 273.15e30),

    # --- 4. Historical & Obsolete Scales ---
    "ºD": (-1.5, 150),
    "Delisle": (-1.5, 150),  # Synonym
    "ºRe": (0.8, 0),
    "Reaumur": (0.8, 0),  # Synonym
    "ºN": (0.33, 0),
    "Newton": (0.33, 0),  # Synonym
    "ºRø": (21 / 40, 7.5),
    "Rømer": (21 / 40, 7.5),  # Synonym
    "ºDu": (1.104, -10.4),  # Du Crest
    "DuCrest": (1.104, -10.4),  # Synonym
    "ºLi": (-1, 100),  # Linnaeus (Inverted Celsius)
    "Linnaeus": (-1, 100),  # Synonym
    "ºF(96)": (64 / 37, 32),  # Fahrenheit (Original 32/96)
    "Fahrenheit-96": (64 / 37, 32),  # Synonym
    "ºW": (9 / 650, -2091 / 260),  # Wedgwood
    "ºL": (1, 253),  # Leiden

    # --- 5. Specialized & Scientific ---
    "GM": (0.072, -8.72),  # Gas Mark
    "T_P": (7.058e-33, 0),  # Planck Temperature
})
# Length converter - Converts between different units of length/distance
# Base unit: Meter (m) with scale factor 1 and offset 0
Length = Converter({
    # 1. Metric (SI) Units
    "m": (1, 0),  # Base Unit
    "metre": (1, 0),  # Synonym for m
    # Multiples
    "dam": (0.1, 0),
    "hm": (0.01, 0),
    "km": (0.001, 0),
    "Mm": (1e-6, 0),
    "Gm": (1e-9, 0),
    "Tm": (1e-12, 0),
    "Pm": (1e-15, 0),
    "Em": (1e-18, 0),
    "Zm": (1e-21, 0),
    "Ym": (1e-24, 0),
    "Rm": (1e-27, 0),  # Ronna
    "Qm": (1e-30, 0),  # Quetta
    # Submultiples
    "dm": (10, 0),
    "cm": (100, 0),
    "mm": (1000, 0),
    "µm": (1e6, 0),
    "nm": (1e9, 0),
    "pm": (1e12, 0),
    "fm": (1e15, 0),
    "am": (1e18, 0),
    "zm": (1e21, 0),
    "ym": (1e24, 0),
    "rm": (1e27, 0),  # Ronto
    "qm": (1e30, 0),  # Quecto

    # 2. Imperial & US Customary Units
    "in": (39.3700787, 0),
    "inch": (39.3700787, 0),  # Synonym for in
    "ft": (3.2808399, 0),
    "foot": (3.2808399, 0),  # Synonym for ft
    "yd": (1.0936133, 0),
    "yard": (1.0936133, 0),  # Synonym for yd
    "mi": (0.000621371192, 0),
    "mile": (0.000621371192, 0),  # Synonym for mi
    "mil": (39370.0787, 0),
    "barleycorn": (3 / 0.0254, 0),
    "line": (12 / 0.0254, 0),
    "fath": (1 / 1.8288, 0),  # Also Nautical
    "fathom-en": (1 / 1.8288, 0),  # Synonym for fath
    "fur": (1 / 201.168, 0),  # Also Surveying
    "furlong": (1 / 201.168, 0),  # Synonym for fur
    "ch": (1 / 20.1168, 0),  # Gunter's Chain, also Surveying
    "rd": (1 / 5.0292, 0),  # Rod, also Surveying
    "pole": (1 / 5.0292, 0),  # Synonym for rd
    "perch": (1 / 5.0292, 0),  # Synonym for rd
    "lea-en": (1 / 4828.032, 0),  # English League
    "hh": (1 / 0.1016, 0),  # Hand
    "hand": (1 / 0.1016, 0),  # Synonym for hh
    "span": (1 / 0.2286, 0),
    "quarter": (1 / 0.2286, 0),
    "pace-en": (1 / 0.762, 0),  # English Pace
    "rope": (1 / 6.096, 0),
    "bolt-us": (1 / 91.44, 0),  # US Bolt
    "ell-en": (1 / 1.143, 0),  # English Ell
    "finger": (1 / 0.1143, 0),
    "nail": (1 / 0.05715, 0),
    "caliber": (100 / 0.0254, 0),
    "button": (8 / 0.0254, 0),  # Also Typographical (Ligne)

    # 3. Surveying & Nautical Units
    "nmi": (1 / 1852, 0),  # Nautical Mile
    "cbl": (1 / 185.2, 0),  # Cable
    "shackle": (1 / 27.432, 0),
    "ft-us": (3937 / 1200, 0),  # US Survey Foot
    "li-gunter": (1 / 0.201168, 0),  # Gunter's Link
    "li-ramden": (1 / 0.3048, 0),  # Ramden's Link
    "ch-ramden": (1 / 30.48, 0),  # Ramden's Chain
    "ch-rathbone": (1 / 10.0584, 0),  # Rathbone's Chain
    "yd-mega": (1 / 0.829, 0),  # Megaphone-corrected yard?

    # 4. Astronomical & Physics Units
    "au": (1 / 1.495978707e11, 0),  # Astronomical Unit
    "ly": (1 / 9.4607e15, 0),  # Light-year
    "light-ns": (1 / 0.299792458, 0),  # Light-nanosecond
    "pc": (1 / 3.085677581e16, 0),  # Parsec
    "kpc": (1 / 3.085677581e19, 0),  # Kiloparsec
    "Mpc": (1 / 3.085677581e22, 0),  # Megaparsec
    "Gpc": (1 / 3.085677581e25, 0),  # Gigaparsec
    "Tpc": (1 / 3.085677581e28, 0),  # Teraparsec
    "Ppc": (1 / 3.085677581e31, 0),  # Petaparsec
    "Epc": (1 / 3.085677581e34, 0),  # Exaparsec
    "Zpc": (1 / 3.085677581e37, 0),  # Zettaparsec
    "Ypc": (1 / 3.085677581e40, 0),  # Yottaparsec
    "siriometer": (1 / 1.4959787e17, 0),
    "D_H": (1 / 1.303e26, 0),  # Hubble distance
    "Å": (1e10, 0),  # Ångström
    "micron": (1e6, 0),  # Synonym for µm
    "fermi": (1e15, 0),  # Synonym for fm
    "a_0": (1 / 5.29177e-11, 0),  # Bohr radius
    "l_P": (1 / 1.616255e-35, 0),  # Planck length
    "xu": (1 / 1.0021e-13, 0),  # X-unit
    "S": (1e-12, 0),  # Note: Identical to "Tm"

    # 5. Typographical & Digital Units
    "pt": (72 / 0.0254, 0),  # Point
    "pica": (6 / 0.0254, 0),
    "px": (96 / 0.0254, 0),  # Pixel (at 96 DPI)
    "twip": (1440 / 0.0254, 0),  # Twentieth of a point
    "agate": (72 / (5.5 * 0.0254), 0),
    "cicero": (1 / 0.004511658, 0),
    "didot-pt": (1 / 0.00037597, 0),  # Didot point
    "pcl-pt": (300 / 0.0254, 0),
    "ligne": (144 / 0.3248, 0),  # French Ligne (Typographical)

    # 6. Historical & Regional Units
    # Ancient
    "cubit-egy": (1 / 0.524, 0),  # Egyptian Cubit
    "pes-rom": (1 / 0.296, 0),  # Roman Foot
    "passus-rom": (1 / 1.48, 0),  # Roman Pace
    "mi-rom": (1 / 1480, 0),  # Roman Mile
    "stadion-gr": (1 / 185, 0),  # Greek Stadion
    "beru-bab": (1 / 10800, 0),  # Babylonian Beru
    "kus-sumer": (1 / 0.495, 0),  # Sumerian Kus
    "su-si": (1 / 0.0165, 0),  # Sumerian Su-si
    "tefach": (1 / 0.0762, 0),  # Hebrew Tefach
    "zeret": (1 / 0.2286, 0),  # Hebrew Zeret
    "amah": (1 / 0.4572, 0),  # Hebrew Amah

    # French
    "point-fr": (1 / 0.000188, 0),  # Point (Truchet)
    "ligne-fr": (1 / 0.002256, 0),  # Ligne (Paris)
    "pouce-fr": (1 / 0.02707, 0),  # Pouce (Paris inch)
    "pied-fr": (1 / 0.3248394, 0),  # Pied du roi (Paris foot)
    "toise-fr": (1 / 1.949036, 0),  # Toise (Paris fathom)
    "perche-fr-arpent": (1 / 7.146, 0),  # Perche d'arpent
    "perche-fr-roi": (1 / 5.847, 0),  # Perche du roi
    "perche-fr-ord": (1 / 6.497, 0),  # Perche ordinaire
    "arpent-fr-arpent": (1 / 71.46, 0),  # Arpent (10 perches d'arpent)
    "arpent-fr-roi": (1 / 58.47, 0),  # Arpent (10 perches du roi)
    "lieue-fr-ancienne": (1 / 3248, 0),  # Lieue ancienne
    "lieue-fr": (1 / 3898, 0),  # Lieue de Paris (French League)
    "lieue-fr-postes": (1 / 4288, 0),  # Lieue des Postes
    "lieue-fr-degre": (1 / 4448, 0),  # Lieue de 25 au degré
    "lieue-fr-tarif": (1 / 4678, 0),  # Lieue tarifaire

    # Spanish
    "ponto-es": (1 / 0.0001613, 0),  # Punto
    "línea-es": (1 / 0.001935, 0),  # Línea
    "pulgada-es": (1 / 0.023216, 0),  # Pulgada (Spanish inch)
    "pie-es": (1 / 0.2786, 0),  # Pie (Spanish foot)
    "codo-es": (1 / 0.41783, 0),  # Codo geométrico
    "codo-real-es": (1 / 0.55778, 0),  # Codo real
    "vara-es": (1 / 0.8359, 0),  # Vara
    "paso-es": (1 / 1.3932, 0),  # Paso
    "braza-es": (1 / 1.6718, 0),  # Braza (2 varas)
    "estadal-es": (1 / 3.3436, 0),  # Estadal (4 varas)
    "milla-es": (1 / 1393.2, 0),  # Milla
    "legua-es": (1 / 4179.5, 0),  # Legua (League)

    # Portuguese
    "ponto-pt": (1 / 0.00019, 0),  # Ponto
    "linha-pt": (1 / 0.00229, 0),  # Linha
    "polegada-pt": (1 / 0.0275, 0),  # Polegada (Portuguese inch)
    "palmo-pt": (1 / 0.22, 0),  # Palmo de craveira (Span)
    "pé-pt": (1 / 0.33, 0),  # Pé (Portuguese foot)
    "côvado-pt": (1 / 0.66, 0),  # Côvado (Cubit)
    "vara-pt": (1 / 1.1, 0),  # Vara
    "passo-pt": (1 / 1.65, 0),  # Passo geométrico
    "toesa-pt": (1 / 1.98, 0),  # Toesa
    "braça-pt": (1 / 2.2, 0),  # Braça (Fathom)
    "légua-pt-20": (1 / 5555, 0),  # Légua de 20 ao grau
    "légua-pt-18": (1 / 6173, 0),  # Légua de 18 ao grau
    "milha-pt": (1 / 1852, 0),  # Milha geográfica (same as nmi)

    # Italian (Regional)
    "linea-it-genoa": (1 / 0.00172, 0),  # Linea (Genoa)
    "oncia-it-rome": (1 / 0.0186, 0),  # Oncia (Rome)
    "pollice-it-genoa": (1 / 0.02067, 0),  # Pollice (Genoa)
    "palmo-it-rome-arch": (1 / 0.22319, 0),  # Palmo architettonica (Rome)
    "palmo-it-sicily": (1 / 0.24203, 0),  # Palmo (Sicily)
    "palmo-it-rome-merc": (1 / 0.24908, 0),  # Palmo mercantile (Rome)
    "palmo-it-naples": (1 / 0.26455, 0),  # Palmo (Naples)
    "piede-it-rome": (1 / 0.297587, 0),  # Piede (Rome)
    "piede-it": (1 / 0.2977, 0),  # Piede (General Italian Foot)
    "piede-it-venice": (1 / 0.347735, 0),  # Piede (Venice)
    "piede-it-bologna": (1 / 0.38, 0),  # Piede (Bologna)
    "piede-it-milan": (1 / 0.435185, 0),  # Piede (Milan)
    "piede-it-liprando": (1 / 0.51377, 0),  # Piede liprando (Sardinia)
    "braccio-fl": (1 / 0.583, 0),  # Braccio (Florentine)
    "braccio-it-milan": (1 / 0.59494, 0),  # Braccio (Milan)
    "braccio-it-rome-tele": (1 / 0.635, 0),  # Braccia per le tele (Rome)
    "braccio-it-bologna": (1 / 0.64, 0),  # Braccio (Bologna)
    "braccio-it-rome-merc": (1 / 0.67, 0),  # Braccia da mercante (Rome)
    "braccio-it-venice": (1 / 0.683, 0),  # Braccio (Venice)
    "canna-it-rome-merc": (1 / 1.99263, 0),  # Canna mercantile (Rome)
    "canna-it-sicily": (1 / 2.0648, 0),  # Canna (Sicily)
    "canna-it-rome-arch": (1 / 2.2319, 0),  # Canna architettonica (Rome)
    "canna-it-naples": (1 / 2.6455, 0),  # Canna (Naples)
    "miglio-it-sicily": (1 / 1486.66, 0),  # Miglio (Sicily)
    "miglio-it-rome": (1 / 1487.93, 0),  # Miglio (Rome)
    "miglio-it-venice": (1 / 1738.67, 0),  # Miglio (Venice)
    "miglio-it-milan": (1 / 1784.81, 0),  # Miglio (Milan)

    # German/Prussian
    "linie-de": (1 / 0.002179, 0),  # Linie (Prussian)
    "zoll-de-pruss": (1 / 0.026154, 0),  # Zoll (Prussian inch)
    "fuss-pruss": (1 / 0.31385, 0),  # Fuss (Prussian foot)
    "fuss-de-rhine": (1 / 0.31387, 0),  # Rheinfuss (Rhine foot)
    "elle-pruss": (1 / 0.58847, 0),  # Elle (Prussian, 1.875 Fuss)
    "klafter-de": (1 / 1.8831, 0),  # Klafter (Prussian, 6 Fuss)
    "rute-pruss": (1 / 3.7662, 0),  # Rute (Prussian, 12 Fuss)
    "wegstunde-de": (1 / 3710, 0),  # Wegstunde (1/2 Meile)
    "meile-de-bavaria": (1 / 7415, 0),  # Meile (Bavaria)
    "meile-de-geo": (1 / 7420.54, 0),  # Geographische Meile
    "meile-de": (1 / 7500, 0),  # Meile (German mile, 'Reichsmeile')
    "meile-de-pruss": (1 / 7532.5, 0),  # Meile (Prussian)

    # Other European
    "verst": (1 / 1066.8, 0),  # Russian
    "arshin": (1 / 0.7112, 0),  # Russian/Turkish
    "mi-scot": (1 / 1814.2, 0),  # Scottish Mile
    "ell-scot": (1 / 0.9413, 0),  # Scottish Ell
    "mil-scan": (1 / 10000, 0),  # Scandinavian Mile
    "alen-dk": (1 / 0.6277, 0),  # Danish Alen
    "aln-se": (1 / 0.5938, 0),  # Swedish Aln
    "tum-se": (24 / 0.5938, 0),  # Swedish Tum (inch)

    # Asian
    "li-cn": (1 / 500, 0),  # Chinese Li
    "zhang-cn": (0.3, 0),  # Chinese Zhang
    "chi-cn": (3, 0),  # Chinese Chi
    "cun-cn": (30, 0),  # Chinese Cun
    "fen-cn": (300, 0),  # Chinese Fen
    "sun-jp": (1 / 0.030303, 0),  # Japanese Sun
    "shaku-jp": (1 / 0.30303, 0),  # Japanese Shaku
    "ken-jp": (1 / 1.81818, 0),  # Japanese Ken
    "ri-jp": (1 / 3927.27, 0),  # Japanese Ri

    # Indian & Middle Eastern
    "gaz": (1 / 0.9144, 0),  # Indian
    "kos": (1 / 3218.69, 0),  # Indian
    "angula": (1 / 0.01778, 0),  # Indian
    "farsakh": (1 / 5500, 0),  # Persian
    "arash": (1 / 0.95, 0),  # Persian

    # 7. Specialized Industry Units
    # Textile
    "hank-cotton": (1 / 768.096, 0),
    "skein-wool": (1 / 109.728, 0),
    "spyndle": (1 / 13167.36, 0),

    # Manufacturing / Other
    "U": (1 / 0.04445, 0),  # Rack Unit
})

# Weight converter - Converts between different units of weight/mass
# Base unit: Kilogram (kg) with scale factor 1 and offset 0
Weight = Converter({
    # --- 1. Base Unit & Synonyms ---
    "kg": (1, 0),  # Kilogram (Base Unit)
    "kilogram": (1, 0),  # Synonym
    "kilo": (1, 0),  # Synonym

    # --- 2. Metric (SI) Units (Full Range) ---
    "g": (1000, 0),  # Gram
    "gram": (1000, 0),  # Synonym
    "tonne": (0.001, 0),  # Tonne (Metric Ton)
    "ton": (0.001, 0),  # Synonym (same as Mg)
    # Multiples
    "dag": (100, 0),  # Decagram
    "hg": (10, 0),  # Hectogram
    "Mg": (0.001, 0),  # Megagram
    "Gg": (1e-6, 0),  # Gigagram
    "Tg": (1e-9, 0),  # Teragram
    "Pg": (1e-12, 0),  # Petagram
    "Eg": (1e-15, 0),  # Exagram
    "Zg": (1e-18, 0),  # Zettagram
    "Yg": (1e-21, 0),  # Yottagram
    "Rg": (1e-24, 0),  # Ronnagram (New)
    "Qg": (1e-27, 0),  # Quettagram (New)
    # Submultiples
    "dg": (10000, 0),  # Decigram
    "cg": (100000, 0),  # Centigram
    "mg": (1e6, 0),  # Milligram
    "ug": (1e9, 0),  # Microgram
    "mcg": (1e9, 0),  # Synonym for ug
    "ng": (1e12, 0),  # Nanogram
    "pg": (1e15, 0),  # Picogram
    "fg": (1e18, 0),  # Femtogram
    "ag": (1e21, 0),  # Attogram
    "zg": (1e24, 0),  # Zeptogram
    "yg": (1e27, 0),  # Yoctogram
    "rg": (1e30, 0),  # Rontogram (New)
    "qg": (1e33, 0),  # Quectogram (New)

    # --- 3. Imperial & US Customary (Avoirdupois) ---
    "lb": (1 / 0.45359237, 0),  # Pound
    "pound": (1 / 0.45359237, 0),  # Synonym
    "oz": (1 / 0.028349523125, 0),  # Ounce
    "ounce": (1 / 0.028349523125, 0),  # Synonym
    "dr": (1 / 0.0017718451953125, 0),  # Dram (1/16 oz)
    "gr": (1 / 6.479891e-5, 0),  # Grain (1/7000 lb)
    "st": (1 / 6.35029318, 0),  # Stone (14 lb)
    "cwt": (1 / 45.359237, 0),  # US Hundredweight (100 lb)
    "lwt": (1 / 50.80234544, 0),  # Imperial Hundredweight (112 lb)
    "uston": (1 / 907.18474, 0),  # US Ton (Short ton, 2000 lb)
    "ukton": (1 / 1016.0469088, 0),  # UK Ton (Long ton, 2240 lb)
    "slug": (1 / 14.59390294, 0),  # Slug

    # --- 4. Troy & Apothecary ---
    "lbt": (1 / 0.3732417216, 0),  # Troy Pound (12 ozt)
    "ozt": (1 / 0.0311034768, 0),  # Troy Ounce (480 gr)
    "dwt": (1 / 0.00155517384, 0),  # Pennyweight (24 gr)
    "ozap": (1 / 0.0311034768, 0),  # Apothecary Ounce (same as ozt)
    "drap": (1 / 0.0038879346, 0),  # Apothecary Dram (60 gr)
    "sgr": (1 / 0.0012959782, 0),  # Scruple (Apothecary, 20 gr)

    # --- 5. Historical & Regional (European) ---
    # French (Paris)
    "livre-fr": (1 / 0.4895, 0),  # Livre (Pound)
    "marc-fr": (1 / 0.24475, 0),  # Marc (1/2 livre)
    "once-fr": (1 / 0.03059, 0),  # Once (Ounce)
    "gros-fr": (1 / 0.003824, 0),  # Gros
    "grain-fr": (1 / 5.311e-5, 0),  # Grain
    # Spanish (Castilian)
    "libra-es": (1 / 0.460093, 0),  # Libra (Pound)
    "onza-es": (1 / 0.02875, 0),  # Onza (Ounce)
    "grano-es": (1 / 3.55e-5, 0),  # Grano
    "arroba-es": (1 / 11.502, 0),  # Arroba (Mass)
    "quintal-es": (1 / 46.009, 0),  # Quintal
    # Portuguese
    "arratel-pt": (1 / 0.459, 0),  # Arratel (Pound)
    "libra-pt": (1 / 0.459, 0),  # Libra (Synonym)
    "onca-pt": (1 / 0.02868, 0),  # Onca (Ounce)
    "grao-pt": (1 / 4.99e-5, 0),  # Grao
    "arroba-pt": (1 / 14.688, 0),  # Arroba (Mass)
    "quintal-pt": (1 / 58.752, 0),  # Quintal
    # German (Prussian)
    "pfund-de": (1 / 0.4677, 0),  # Pfund (Pound)
    "unze-de": (1 / 0.02923, 0),  # Unze (Ounce)
    "loth-de": (1 / 0.01461, 0),  # Loth
    "zentner-de": (1 / 46.77, 0),  # Zentner
    # Russian
    "funt-ru": (1 / 0.4095, 0),  # Funt (Pound)
    "zolotnik-ru": (1 / 0.00426, 0),  # Zolotnik
    "dolia-ru": (1 / 4.44e-5, 0),  # Dolia
    "pood": (1 / 16.38, 0),  # Pood

    # --- 6. Historical & Regional (Asian) ---
    "tael": (1 / 0.05, 0),  # Tael (Chinese, approx 50g)
    "catti": (1 / 0.6048, 0),  # Catti (or Kati)
    "picul": (1 / 60.48, 0),  # Picul
    "momme-jp": (1 / 0.00375, 0),  # Momme (Japanese)
    "tola-in": (1 / 0.01166, 0),  # Tola (India)
    "seer-in": (1 / 0.933, 0),  # Seer (India)

    # --- 7. Historical (Ancient) ---
    # Roman
    "libra-rom": (1 / 0.3289, 0),  # Roman Pound
    "uncia-rom": (1 / 0.0274, 0),  # Roman Ounce
    "drachma-rom": (1 / 0.00342, 0),  # Roman Drachma
    # Greek (Attic)
    "mina-gr": (1 / 0.431, 0),  # Mina
    "drachma-gr": (1 / 0.00431, 0),  # Drachma
    "obol-gr": (1 / 0.00072, 0),  # Obol
    # Hebrew
    "shekel-heb": (1 / 0.0114, 0),  # Shekel
    "beka-heb": (1 / 0.0057, 0),  # Beka
    "gerah-heb": (1 / 0.00057, 0),  # Gerah
    "talent-heb": (1 / 34.2, 0),  # Talent

    # --- 8. Scientific & Specialized ---
    "ct": (5000, 0),  # Carat
    "Da": (1 / 1.660539e-27, 0),  # Dalton / AMU
    "gamma": (1e9, 0),  # Gamma (1 microgram)
    "m_p": (1 / 2.1764e-8, 0),  # Planck Mass
    "M_earth": (1 / 5.972e24, 0),  # Earth Mass
    "M_jup": (1 / 1.898e27, 0),  # Jupiter Mass
    "M_solar": (1 / 1.989e30, 0),  # Solar Mass
    "M_sun": (1 / 1.989e30, 0),  # Synonym
})

# Volume converter - Converts between different units of volume
# Base unit: Liter (L) with scale factor 1 and offset 0
Volume = Converter({
    # --- 1. Base & Metric (SI) Units (Liters) ---
    "L": (1, 0),  # Liter (Base Unit)
    "liter": (1, 0),  # Synonym
    "cc": (1000, 0),  # Cubic Centimeter (Synonym for mL)
    "lambda": (1e6, 0),  # Lambda (Synonym for µL in chemistry)
    # Multiples
    "daL": (0.1, 0),  # Decaliter
    "hL": (0.01, 0),  # Hectoliter
    "kL": (0.001, 0),  # Kiloliter
    "ML": (1e-6, 0),  # Megaliter
    "GL": (1e-9, 0),  # Gigaliter
    "TL": (1e-12, 0),  # Teraliter
    "PL": (1e-15, 0),  # Petaliter
    "EL": (1e-18, 0),  # Exaliter
    "ZL": (1e-21, 0),  # Zettaliter
    "YL": (1e-24, 0),  # Yottaliter
    "RL": (1e-27, 0),  # Ronnaliter
    "QL": (1e-30, 0),  # Quettaliter
    # Submultiples
    "dL": (10, 0),  # Deciliter
    "cL": (100, 0),  # Centiliter
    "mL": (1000, 0),  # Milliliter
    "µL": (1e6, 0),  # Microliter
    "nL": (1e9, 0),  # Nanoliter
    "pL": (1e12, 0),  # Picoliter
    "fL": (1e15, 0),  # Femtoliter
    "aL": (1e18, 0),  # Attoliter
    "zL": (1e21, 0),  # Zeptoliter
    "yL": (1e24, 0),  # Yoctoliter
    "rL": (1e27, 0),  # Rontoliter
    "qL": (1e30, 0),  # Quectoliter

    # --- 2. Cubic Metric Units (m³) ---
    "m³": (0.001, 0),  # Cubic Meter (Base for this section)
    "stere": (0.001, 0),  # Stere (Synonym for m³)
    # Multiples
    "dam³": (1e-6, 0),  # Cubic Decameter (10³ m³)
    "hm³": (1e-9, 0),  # Cubic Hectometer (10⁶ m³)
    "km³": (1e-12, 0),  # Cubic Kilometer (10⁹ m³)
    "Mm³": (1e-21, 0),  # Cubic Megameter (10¹⁸ m³)
    "Gm³": (1e-30, 0),  # Cubic Gigameter (10²⁷ m³)
    "Tm³": (1e-39, 0),  # Cubic Terameter (10³⁶ m³)
    "Pm³": (1e-48, 0),  # Cubic Petameter (10⁴⁵ m³)
    "Em³": (1e-57, 0),  # Cubic Exameter (10⁵⁴ m³)
    "Zm³": (1e-66, 0),  # Cubic Zettameter (10⁶³ m³)
    "Ym³": (1e-75, 0),  # Cubic Yottameter (10⁷² m³)
    "Rm³": (1e-84, 0),  # Cubic Ronnameter (10⁸¹ m³)
    "Qm³": (1e-93, 0),  # Cubic Quettameter (10⁹⁰ m³)
    # Submultiples
    "dm³": (1, 0),  # Cubic Decimeter (10⁻³ m³)
    "cm³": (1000, 0),  # Cubic Centimeter (10⁻⁶ m³)
    "mm³": (1e6, 0),  # Cubic Millimeter (10⁻⁹ m³)
    "µm³": (1e15, 0),  # Cubic Micrometer (10⁻¹⁸ m³)
    "nm³": (1e24, 0),  # Cubic Nanometer (10⁻²⁷ m³)
    "pm³": (1e33, 0),  # Cubic Picometer (10⁻³⁶ m³)
    "fm³": (1e42, 0),  # Cubic Femtometer (10⁻⁴⁵ m³)
    "am³": (1e51, 0),  # Cubic Attometer (10⁻⁵⁴ m³)
    "zm³": (1e60, 0),  # Cubic Zeptometer (10⁻⁶³ m³)
    "ym³": (1e69, 0),  # Cubic Yoctometer (10⁻⁷² m³)
    "rm³": (1e78, 0),  # Cubic Rontometer (10⁻⁸¹ m³)
    "qm³": (1e87, 0),  # Cubic Quectometer (10⁻⁹⁰ m³)

    # --- 3. US Customary (Liquid) & Apothecary ---
    "gal": (1 / 3.785411784, 0),  # US Gallon
    "qt": (1 / 0.946352946, 0),  # US Quart
    "pt": (1 / 0.473176473, 0),  # US Pint
    "cup": (1 / 0.24, 0),  # US Legal Cup (240mL)
    "cup-us": (1 / 0.2365882365, 0),  # US Customary Cup
    "fl_oz": (1 / 0.0295735295625, 0),  # US Fluid Ounce
    "tbsp": (1 / 0.01478676478125, 0),  # US Tablespoon
    "tsp": (1 / 0.00492892159375, 0),  # US Teaspoon
    "gill-us": (1 / 0.11829411825, 0),  # US Gill
    "fldr": (1 / 0.0036966911953125, 0),  # US Fluid Dram
    "flsc-us": ((1 / 0.0295735295625) * 24, 0),  # US Fluid Scruple (1/24 fl_oz)
    "min": (1 / 6.1611519921875e-5, 0),  # US Minim
    "bbl-fl": (1 / 119.240471196, 0),  # US Barrel (Fluid, 31.5 gal)
    "bbl-oil": (1 / 158.987294928, 0),  # US Barrel (Oil, 42 gal)
    "rundlet": (1 / 69.9721179, 0),  # Rundlet (18.5 US gal)
    "tierce": (1 / 158.987294928, 0),  # Tierce (Synonym for bbl-oil)

    # --- 4. UK Imperial & Apothecary ---
    "gal-uk": (1 / 4.54609, 0),  # UK Gallon
    "qt-uk": (1 / 1.1365225, 0),  # UK Quart
    "pt-uk": (1 / 0.56826125, 0),  # UK Pint
    "cup-uk": (1 / 0.284130625, 0),  # UK Cup (284 mL)
    "fl_oz-uk": (1 / 0.0284130625, 0),  # UK Fluid Ounce
    "tbsp-uk": (1 / 0.0177581640625, 0),  # UK Tablespoon
    "tsp-uk": (1 / 0.0059193880208333, 0),  # UK Teaspoon
    "gill-uk": (1 / 0.1420653125, 0),  # UK Gill
    "noggin-uk": (4 / 0.56826125, 0),  # Noggin (1/4 UK pt)
    "pottle-uk": (1 / 2.273045, 0),  # Pottle (2 UK qt)
    "fldr-uk": (8 / 0.0284130625, 0),  # UK Fluid Drachm (1/8 fl_oz-uk)
    "flsc-uk": (24 / 0.0284130625, 0),  # UK Fluid Scruple (1/3 fldr-uk)
    "firkin": (1 / 40.91481, 0),  # Firkin (UK, 9 UK gal)
    "kilderkin-uk": (1 / 81.82962, 0),  # Kilderkin (18 UK gal)

    # --- 5. US Customary (Dry) ---
    "gal-us-dry": (1 / 4.40488377086, 0),  # US Dry Gallon
    "qt-us-dry": (1 / 1.101220942715, 0),  # US Dry Quart
    "pt-us-dry": (1 / 0.5506104713575, 0),  # US Dry Pint
    "pk-us": (1 / 8.80976754172, 0),  # US Peck
    "bu-us": (1 / 35.23907016688, 0),  # US Bushel

    # --- 6. Cubic Imperial / US Units ---
    "in³": (1 / 0.016387064, 0),  # Cubic Inch
    "ft³": (1 / 28.316846592, 0),  # Cubic Foot
    "yd³": (1 / 764.554857984, 0),  # Cubic Yard
    "mi³": (1 / 4.16818182544058e12, 0),  # Cubic Mile
    "af": (1 / 1233481.8375475, 0),  # Acre-foot

    # --- 7. Cooking (Other Metric) ---
    "tsp-met": (200, 0),  # Teaspoon (Metric, 5 mL)
    "tbsp-met": (1000 / 15, 0),  # Tablespoon (Metric, 15 mL)
    "cup-met": (4, 0),  # Cup (Metric, 250 mL)
    "cup-aus": (4, 0),  # Cup (Australia, 250 mL)
    "tbsp-aus": (50, 0),  # Tablespoon (Australia, 20 mL)
    "cup-jp": (5, 0),  # Cup (Japan, 200 mL)

    # --- 8. Industry & Specialized ---
    "board-foot": (1 / 2.359737216, 0),  # Board Foot (12x12x1 in)
    "cord": (1 / 3624.55635, 0),  # Cord (Firewood, 128 ft³)
    "register-ton": (1 / 2831.68466, 0),  # Register Ton (Shipping, 100 ft³)
    "hogshead": (1 / 238.480942392, 0),  # Hogshead (US, 63 gal)
    "tun": (1 / 953.9238, 0),  # Tun (Wine, 252 gal)
    "butt": (1 / 476.9619, 0),  # Butt (Wine, 126 gal)

    # --- 9. Historical & Regional ---
    # Spanish
    "celemín-es": (1 / 4.625, 0),  # Celemín
    "fanega-es-dry": (1 / 55.5, 0),  # Fanega (dry)
    "cántara-es": (1 / 16.133, 0),  # Cántara
    "arroba-es-liq": (1 / 12.563, 0),  # Arroba (liquid)
    "almud-es": (1 / 4.625, 0),  # Almud

    # Portuguese
    "quartilho-pt": (1 / 0.35, 0),  # Quartilho
    "canada-pt": (1 / 1.4, 0),  # Canada
    "pote-pt": (1 / 8.4, 0),  # Pote
    "almude-pt": (1 / 16.8, 0),  # Almude
    "pipa-pt": (1 / 420, 0),  # Pipa
    "tonel-pt": (1 / 840, 0),  # Tonel

    # French
    "roquille-fr": (1 / 0.02975, 0),  # Roquille
    "poisson-fr": (1 / 0.119, 0),  # Poisson
    "demiard-fr": (1 / 0.238, 0),  # Demiard
    "chopine-fr": (1 / 0.4761, 0),  # Chopine
    "pinte-fr": (1 / 0.9521, 0),  # Pinte (Paris)
    "velte-fr": (1 / 7.617, 0),  # Velte
    "quartaut-fr": (1 / 68.55, 0),  # Quartaut
    "feuillette-fr": (1 / 137.1, 0),  # Feuillette
    "muid-fr-liq": (1 / 274.2, 0),  # Muid (liquid)
    "litron-fr-dry": (1 / 0.7935, 0),  # Litron (dry)
    "boisseau-fr-dry": (1 / 12.7, 0),  # Boisseau (dry)
    "minot-fr-dry": (1 / 38.09, 0),  # Minot (dry)
    "setier-fr-dry": (1 / 152.3, 0),  # Setier (dry)
    "muid-fr-dry": (1 / 1828, 0),  # Muid (dry)

    # German
    "ahm-de": (1 / 137.4, 0),  # Ahm (Prussian)
    "ohm-de": (1 / 137.4, 0),  # Ohm (Synonym for Ahm)
    "anker-de": (1 / 34.35, 0),  # Anker (Prussian)
    "eimer-de": (1 / 68.7, 0),  # Eimer (Prussian)

    # Dutch
    "anker-nl": (1 / 38.8, 0),  # Anker (Dutch)
    "stoop-nl": (1 / 2.4, 0),  # Stoop (Dutch)
    "mutsje-nl": (1 / 0.15, 0),  # Mutsje (Dutch)

    # Scandinavian
    "kanna-se": (1 / 2.617, 0),  # Kanna (Swedish)
    "pot-dk": (1 / 0.966, 0),  # Pot (Danish)

    # Russian
    "garnets-ru": (1 / 3.279, 0),  # Garnets
    "vedro-ru": (1 / 12.299, 0),  # Vedro
    "chetvert-ru-dry": (1 / 209.9, 0),  # Chetvert (dry)
    "bochka-ru": (1 / 491.96, 0),  # Bochka

    # Asian (Historical)
    "go-jp": (1 / 0.18039, 0),  # Go (Japanese)
    "sho-jp": (1 / 1.8039, 0),  # Sho (10 go)
    "to-jp": (1 / 18.039, 0),  # To (10 sho)
    "koku-liq-jp": (1 / 180.39, 0),  # Koku (liquid, 10 to)
    "koku-dry-jp": (1 / 278.3, 0),  # Koku (dry, historical)
    "sheng-cn": (1 / 1.0354688, 0),  # Sheng (Chinese)
    "dou-cn": (1 / 10.354688, 0),  # Dou (10 sheng)
    "pao-in": (1 / 0.233, 0),  # Pao (Indian)

    # --- 10. Ancient ---
    # Roman
    "hemina-rom": (1 / 0.273, 0),  # Hemina
    "sextarius-rom": (1 / 0.546, 0),  # Sextarius
    "congius-rom": (1 / 3.27, 0),  # Congius
    "modius-rom": (1 / 8.7, 0),  # Modius (dry)
    "urna-rom": (1 / 13.1, 0),  # Urna
    "amphora-rom": (1 / 26.2, 0),  # Amphora

    # Biblical/Hebrew
    "log-heb": (1 / 0.31, 0),  # Log
    "kab-heb": (1 / 1.22, 0),  # Kab
    "hin-heb": (1 / 3.67, 0),  # Hin
    "omer-heb": (1 / 2.2, 0),  # Omer (dry)
    "seah-heb": (1 / 7.33, 0),  # Seah (dry)
    "bath-heb": (1 / 22, 0),  # Bath (liquid)
    "ephah-heb": (1 / 22, 0),  # Ephah (dry)
    "homer-heb": (1 / 220, 0),  # Homer
    "kor-heb": (1 / 220, 0),  # Kor (Synonym for Homer)

    # Babylonian/Egyptian
    "qa-bab": (1 / 1.2, 0),  # Qa (Babylonian)
    "hekat-egy": (1 / 4.8, 0),  # Hekat (Egyptian)
    "hin-egy": (1 / 0.48, 0),  # Hin (Egyptian)

    # --- 11. Physics ---
    "V_P": (1 / 4.22419e-102, 0),  # Planck Volume (l_P³)
})

# Area converter - Converts between different units of area
# Base unit: Square Meter with scale factor 1 and offset 0
Area = Converter({
    # --- 1. Base Unit & Metric (SI) Units ---
    "m²": (1, 0),  # Square Meter (Base Unit)
    "sq m": (1, 0),  # Synonym
    # Multiples
    "dam²": (1e-2, 0),  # Square Decameter (Are)
    "hm²": (1e-4, 0),  # Square Hectometer (Hectare)
    "km²": (1e-6, 0),  # Square Kilometer
    "Mm²": (1e-12, 0),  # Square Megameter
    "Gm²": (1e-18, 0),  # Square Gigameter
    "Tm²": (1e-24, 0),  # Square Terameter
    "Pm²": (1e-30, 0),  # Square Petameter
    "Em²": (1e-36, 0),  # Square Exameter
    "Zm²": (1e-42, 0),  # Square Zettameter
    "Ym²": (1e-48, 0),  # Square Yottameter
    "Rm²": (1e-54, 0),  # Square Ronnameter
    "Qm²": (1e-60, 0),  # Square Quettameter
    # Submultiples
    "dm²": (1e2, 0),  # Square Decimeter
    "cm²": (1e4, 0),  # Square Centimeter
    "mm²": (1e6, 0),  # Square Millimeter
    "µm²": (1e12, 0),  # Square Micrometer
    "nm²": (1e18, 0),  # Square Nanometer
    "pm²": (1e24, 0),  # Square Picometer
    "fm²": (1e30, 0),  # Square Femtometer
    "am²": (1e36, 0),  # Square Attometer
    "zm²": (1e42, 0),  # Square Zeptometer
    "ym²": (1e48, 0),  # Square Yoctometer
    "rm²": (1e54, 0),  # Square Rontometer
    "qm²": (1e60, 0),  # Square Quectometer

    # --- 2. Metric Land/Common ---
    "a": (1e-2, 0),  # Are
    "ha": (1e-4, 0),  # Hectare
    "decare": (1e-3, 0),  # Decare (1,000 m²)

    # --- 3. Imperial & US Customary ---
    "in²": (1 / 0.00064516, 0),  # Square Inch
    "ft²": (1 / 0.09290304, 0),  # Square Foot
    "yd²": (1 / 0.83612736, 0),  # Square Yard
    "rd²": (1 / 25.2929538, 0),  # Square Rod (Square Perch)
    "perch²": (1 / 25.2929538, 0),  # Square Perch (Synonym)
    "rood": (1 / 1011.71415, 0),  # Rood (1/4 acre)
    "acre": (1 / 4046.85642, 0),  # Acre (International)
    "mi²": (1 / 2589988.11, 0),  # Square Mile
    "sq in": (1 / 0.00064516, 0),  # Synonym
    "sq ft": (1 / 0.09290304, 0),  # Synonym
    "sq yd": (1 / 0.83612736, 0),  # Synonym
    "sq mi": (1 / 2589988.11, 0),  # Synonym

    # --- 4. US Surveying ---
    "acre-us": (1 / 4046.87261, 0),  # US Survey Acre
    "ft²-us": (1 / 0.0929034116, 0),  # US Survey Square Foot
    "rd²-us": (1 / 25.2929997, 0),  # US Survey Square Rod
    "section": (1 / 2589998.47, 0),  # Section (1 sq mi, US Survey)
    "township": (1 / 93239944.9, 0),  # Township (36 sections)

    # --- 5. Historical & Regional (European) ---
    # French
    "arpent-fr-roi": (1 / 3418.89, 0),  # Arpent (Paris, 100 perches du roi)
    "perche²-fr-roi": (1 / 34.1889, 0),  # Perche carrée (du roi)
    "arpent-fr-ord": (1 / 4220.8, 0),  # Arpent (ordinaire, 100 perches ordinaires)
    "perche²-fr-ord": (1 / 42.208, 0),  # Perche carrée (ordinaire)
    "journal-fr": (1 / 3418.89, 0),  # Journal (Synonym for arpent)
    # Spanish
    "fanega-es": (1 / 6450, 0),  # Fanega (approx, varied)
    "cuerda-pr": (1 / 3930.3956, 0),  # Cuerda (Puerto Rico)
    "caballería-es": (1 / 38624, 0),  # Caballería (Spain)
    "caballería-cu": (1 / 134200, 0),  # Caballería (Cuba)
    # Portuguese
    "alqueire-pt-br": (1 / 24200, 0),  # Alqueire Paulista (Brazil)
    "alqueire-pt-mg": (1 / 48400, 0),  # Alqueire Mineiro (Brazil)
    # German/Dutch
    "morgen-pruss": (1 / 2553.22, 0),  # Morgen (Prussia)
    "morgen-nl": (1 / 8516, 0),  # Morgen (Netherlands)
    "hufe-de": (1 / 76590, 0),  # Hufe (Germany, approx)
    # Italian
    "braccio²-fl": (1 / 0.34, 0),  # Braccio quadro (Florence)
    "giornata-it": (1 / 3810, 0),  # Giornata (Piedmont)
    # Russian
    "desyatina-ru": (1 / 10925, 0),  # Desyatina
    "sotka-ru": (1 / 100, 0),  # Sotka (Synonym for Are)
    # Scandinavian
    "tunnland-se": (1 / 4936.4, 0),  # Tunnland (Sweden)
    "tønde-land-dk": (1 / 5516.2, 0),  # Tønde land (Denmark)
    # Irish
    "acre-ie": (1 / 6555.2, 0),  # Irish Acre

    # --- 6. Historical & Regional (Asian/Middle East) ---
    # Japanese
    "tsubo-jp": (1 / 3.305785, 0),  # Tsubo
    "tan-jp": (1 / 991.7355, 0),  # Tan (10 se)
    "se-jp": (1 / 99.17355, 0),  # Se (30 tsubo)
    "chō-jp": (1 / 9917.355, 0),  # Chō (10 tan)
    # Chinese
    "mǔ-cn": (1 / 666.67, 0),  # Mǔ
    "lí-cn": (1 / 66.67, 0),  # Lí (area)
    "qǐng-cn": (1 / 66666.67, 0),  # Qǐng (100 mǔ)
    # Indian
    "bigha-in-bengal": (1 / 1337.8, 0),  # Bigha (Bengal)
    "bigha-in-pucca": (1 / 2529.29, 0),  # Bigha (Pucca)
    "katha-in-bengal": (1 / 66.89, 0),  # Katha (Bengal)
    "gunta-in": (1 / 101.17, 0),  # Gunta
    "ankanam-in": (1 / 6.689, 0),  # Ankanam
    "ground-in": (1 / 222.96, 0),  # Ground (South India)
    # Thai
    "rai-th": (1 / 1600, 0),  # Rai
    "ngaan-th": (1 / 400, 0),  # Ngaan (1/4 rai)
    "wa²-th": (1 / 4, 0),  # Square Wa
    # Middle East
    "dunam-ot": (1 / 919.3, 0),  # Dunam (Ottoman)
    "dunam-met": (1 / 1000, 0),  # Dunam (Metric, Synonym for decare)
    "feddan-egy": (1 / 4200.83, 0),  # Feddan (Egypt)

    # --- 7. Historical (Ancient) ---
    "jugerum-rom": (1 / 2530, 0),  # Jugerum (Roman)
    "heredium-rom": (1 / 5060, 0),  # Heredium (2 jugera)
    "centuria-rom": (1 / 506000, 0),  # Centuria (100 heredia)
    "plethron-gr": (1 / 950, 0),  # Plethron (Greek, approx)

    # --- 8. Scientific & Specialized ---
    "barn": (1e28, 0),  # Barn (Physics)
    "shed": (1e52, 0),  # Shed (Physics)
    "outbuilding": (1e31, 0),  # Outbuilding (Physics)
    "circular-in": (1 / 5.067e-4, 0),  # Circular Inch
    "circular-mil": (1 / 5.067e-10, 0),  # Circular Mil
})

# Speed converter - Converts between different units of speed
# Base unit: Meter per Second with scale factor 1 and offset 0
Speed = Converter({
    # --- 1. Base Unit (SI) ---
    "m/s": (1, 0),  # Meter per Second
    "mps": (1, 0),  # Synonym

    # --- 2. SI (Metric) System ---

    # Terameter (Tm)
    "Tm/s": (1e12, 0),
    "Tm/min": (16666666666.666666, 0),
    "Tm/h": (277777777.7777778, 0),
    "Tm/d": (11574074.074074075, 0),

    # Gigameter (Gm)
    "Gm/s": (1e9, 0),
    "Gm/min": (16666666.666666668, 0),
    "Gm/h": (277777.7777777778, 0),
    "Gm/d": (11574.074074074075, 0),

    # Megameter (Mm)
    "Mm/s": (1e6, 0),
    "Mm/min": (16666.666666666668, 0),
    "Mm/h": (277.7777777777778, 0),
    "Mm/d": (11.574074074074074, 0),

    # Kilometer (km)
    "km/s": (1000, 0),
    "km/min": (16.666666666666668, 0),
    "km/h": (0.2777777777777778, 0),  # (1000 / 3600)
    "kph": (0.2777777777777778, 0),  # Synonym
    "km/d": (0.011574074074074073, 0),

    # Hectometer (hm)
    "hm/s": (100, 0),
    "hm/min": (1.6666666666666667, 0),
    "hm/h": (0.027777777777777776, 0),
    "hm/d": (0.0011574074074074074, 0),

    # Decameter (dam)
    "dam/s": (10, 0),
    "dam/min": (0.16666666666666666, 0),
    "dam/h": (0.002777777777777778, 0),
    "dam/d": (0.00011574074074074074, 0),

    # Meter (m)
    "m/min": (0.016666666666666666, 0),  # (1 / 60)
    "m/h": (0.0002777777777777778, 0),  # (1 / 3600)
    "m/d": (1.1574074074074073e-05, 0),  # (1 / 86400)

    # Decimeter (dm)
    "dm/s": (0.1, 0),
    "dm/min": (0.0016666666666666668, 0),
    "dm/h": (2.777777777777778e-05, 0),
    "dm/d": (1.1574074074074074e-06, 0),

    # Centimeter (cm)
    "cm/s": (0.01, 0),
    "cm/min": (0.00016666666666666666, 0),
    "cm/h": (2.777777777777778e-06, 0),
    "cm/d": (1.1574074074074074e-07, 0),

    # Millimeter (mm)
    "mm/s": (1e-3, 0),
    "mm/min": (1.6666666666666667e-05, 0),
    "mm/h": (2.777777777777778e-07, 0),
    "mm/d": (1.1574074074074074e-08, 0),

    # Micrometer (μm or um)
    "um/s": (1e-6, 0),
    "um/min": (1.6666666666666667e-08, 0),
    "um/h": (2.777777777777778e-10, 0),
    "um/d": (1.1574074074074074e-11, 0),
    "μm/s": (1e-6, 0),
    "μm/min": (1.6666666666666667e-08, 0),
    "μm/h": (2.777777777777778e-10, 0),
    "μm/d": (1.1574074074074074e-11, 0),

    # Nanometer (nm)
    "nm/s": (1e-9, 0),
    "nm/min": (1.6666666666666667e-11, 0),
    "nm/h": (2.777777777777778e-13, 0),
    "nm/d": (1.1574074074074074e-14, 0),

    # Picometer (pm)
    "pm/s": (1e-12, 0),
    "pm/min": (1.6666666666666667e-14, 0),
    "pm/h": (2.777777777777778e-16, 0),
    "pm/d": (1.1574074074074073e-17, 0),

    # --- 3. Imperial & US Customary System ---

    # Miles (mi)
    "mi/s": (1609.344, 0),
    "mi/min": (26.8224, 0),
    "mi/h": (0.44704, 0),  # (1609.344 / 3600)
    "mph": (0.44704, 0),  # Synonym
    "mi/d": (0.018626666666666668, 0),

    # Furlong (fur)
    "fur/s": (201.168, 0),
    "fur/min": (3.3528, 0),
    "fur/h": (0.05588, 0),
    "fur/d": (0.0023283333333333334, 0),

    # Yard (yd)
    "yd/s": (0.9144, 0),
    "yd/min": (0.01524, 0),
    "yd/h": (0.000254, 0),
    "yd/d": (1.0583333333333334e-05, 0),

    # Foot (ft)
    "ft/s": (0.3048, 0),
    "fps": (0.3048, 0),  # Synonym
    "ft/min": (0.00508, 0),
    "fpm": (0.00508, 0),  # Synonym
    "ft/h": (8.466666666666667e-05, 0),
    "ft/d": (3.527777777777778e-06, 0),

    # Inch (in)
    "in/s": (0.0254, 0),
    "ips": (0.0254, 0),  # Synonym
    "in/min": (0.0004233333333333333, 0),
    "in/h": (7.055555555555556e-06, 0),
    "in/d": (2.9398148148148148e-07, 0),

    # --- 4. Nautical & Aviation ---
    "nmi/s": (1852, 0),
    "nmi/min": (30.866666666666667, 0),
    "nmi/h": (0.5144444444444445, 0),  # (1852 / 3600)
    "knots": (0.5144444444444445, 0),  # Synonym
    "knot": (0.5144444444444445, 0),  # Synonym
    "kn": (0.5144444444444445, 0),  # Synonym
    "nmi/d": (0.021435185185185185, 0),

    # --- 5. Scientific & Astronomical ---
    "c": (299792458, 0),  # Speed of Light
    "mach": (343, 0),  # Mach 1 (approx. at sea level)

    # Astronomical Unit (AU)
    "AU/s": (149597870700, 0),
    "AU/min": (2493297845.0, 0),
    "AU/h": (41554964.083333336, 0),
    "AU/d": (1731456.8368055556, 0),
    "AU/year": (4740.47036326615, 0),  # (per 365.25 days)

    # Light-year (ly)
    "ly/s": (9.4607304725808e15, 0),
    "ly/min": (1.5767884120968e14, 0),
    "ly/h": (2.627980686828e12, 0),
    "ly/d": (1.094991952845e11, 0),
    "ly/year": (299792458.00000006, 0),  # (Effectively 1 * c)

    # Parsec (pc)
    "pc/s": (3.08567758149137e16, 0),
    "pc/min": (5.142795969152284e14, 0),
    "pc/h": (8.571326615253806e12, 0),
    "pc/d": (3.571386089689086e11, 0),
    "pc/year": (977792.208107572, 0),  # (per 365.25 days)
})


