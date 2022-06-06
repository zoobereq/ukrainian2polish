"""Alphabets for Polish-Ukrainian transcritpion"""


import pynini


UKRAINIAN_upper = pynini.union(
    # upper-case Ukrainian graphemes
    "А", 
    "Б", 
    "В", 
    "Г", 
    "Ґ", 
    "Д", 
    "Е", 
    "Є", 
    "Ж", 
    "З", 
    "И", 
    "І", 
    "Ї", 
    "Й", 
    "К", 
    "Л", 
    "М", 
    "Н",
    "О",
    "П",
    "Р",
    "С",
    "Т",
    "У",
    "Ф",
    "Х",
    "Ц",
    "Ч",
    "Ш",
    "Щ",
    "Ь",
    "Ю",
    "Я"
)

UKRAINIAN_lower = pynini.union(
    # lower-case Ukrainian graphemes
    "а",
    "б",
    "в",
    "г",
    "ґ",
    "д",
    "е",
    "є",
    "ж",
    "з",
    "и",
    "і",
    "ї",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ь",
    "ю",
    "я"
)

# the Ukrainian alphabet
ukrainian = pynini.union(UKRAINIAN_upper, UKRAINIAN_lower)

ukr_vowels = pynini.union(
    # all Ukrainian vowel graphemes (upper and lower-case)
    "А", 
    "Е", 
    "Є", 
    "И", 
    "І", 
    "Ї", 
    "О", 
    "У", 
    "Ю", 
    "Я", 
    "а", 
    "е", 
    "є", 
    "и", 
    "і", 
    "ї", 
    "о", 
    "у", 
    "ю", 
    "я"
)

ukr_consonants_upper = pynini.union(
    # upper-case Ukrainian consonant graphemes
    "Б", 
    "Г", 
    "Ґ", 
    "Д", 
    "Ж", 
    "З", 
    "К", 
    "М", 
    "Н", 
    "П", 
    "Р", 
    "С", 
    "Т", 
    "Ф", 
    "Х", 
    "Ц", 
    "Ч", 
    "Ш", 
    "Щ"
)

ukr_consonants_lower = pynini.union(
    # lower-case Ukrainian consonant graphemes
    "б", 
    "г", 
    "в", 
    "ґ", 
    "д", 
    "ж", 
    "з", 
    "к", 
    "м", 
    "н", 
    "п", 
    "р", 
    "с", 
    "т", 
    "ф", 
    "х", 
    "ц", 
    "ч", 
    "ш", 
    "щ"
)

# all Ukrainian consonant graphemes
ukr_consonants = pynini.union(ukr_consonants_upper, ukr_consonants_lower)

POLISH_upper = pynini.union(
    # upper-case Polish graphemes
    "Ą",
    "Ć",
    "Ę",
    "Ł",
    "Ń",
    "Ó",
    "Ś",
    "Ź",
    "Ż",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "S",
    "T",
    "U",
    "W",
    "Y",
    "Z"
)

POLISH_lower = pynini.union(
# lower-case Polish graphemes
    "ą",
    "ć",
    "ę",
    "ł",
    "ń",
    "ó",
    "ś",
    "ź",
    "ż",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "w",
    "y",
    "z"
)

# the Polish alphabet
polish = pynini.union(POLISH_upper, POLISH_lower)

# the punctuation set
punctuation = pynini.union(" ", ",", "-")

SIGMA_STAR = pynini.union(ukrainian, polish, punctuation).closure().optimize()