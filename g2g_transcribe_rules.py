"""
Rules for Polish-Ukrainian transcription

Based on:
Państwowe Wydawnictwo Naukowe. (n.d.). Transliteracja i transkrypcja współczesnego alfabetu ukraińskiego. Słownik Języka Polskiego PWN. Retrieved May 21, 2022, from https://sjp.pwn.pl/zasady/Transliteracja-i-transkrypcja-wspolczesnego-alfabetu-ukrainskiego;629710.html 

It is assumed that input strings follow standard capitalization rules,
where capitalization is applied only word-initially or not applied at all.
"""


import pynini
from pynini.lib import rewrite
from g2g_alphabets import SIGMA_STAR
from g2g_alphabets import ukr_vowels
from g2g_alphabets import ukr_consonants_lower


G2G_transcribe = (

# rules for surname suffixes:
pynini.cdrewrite(pynini.cross("ський", "ski"), "", "[EOS]", SIGMA_STAR) # '-ський' --> '-ski'
@ pynini.cdrewrite(pynini.cross("цький", "cki"), "", "[EOS]", SIGMA_STAR) # '-цький' --> '-cki'
@ pynini.cdrewrite(pynini.cross("ий", "y"), "", "[EOS]", SIGMA_STAR) # '-ий' --> '-y'


# rules for <Є> and <є> transcription:
@ pynini.cdrewrite(pynini.cross("Є", "Je"), pynini.union("[BOS]", " ", "-", ukr_vowels),  "", SIGMA_STAR) 
# Є --> 'Je' word-initially, after vowels, and after the apostrophe
@ pynini.cdrewrite(pynini.cross("є", "je"), pynini.union("[BOS]", " ", "-", ukr_vowels), "", SIGMA_STAR) 
# є --> 'je' word-initially, after vowels, and after the apostrophe
@ pynini.cdrewrite(pynini.cross("є", "e"), pynini.union("Л", "л"), "", SIGMA_STAR)
# є --> e after <Л> and <л>
@ pynini.cdrewrite(pynini.cross("є", "ie"), 
pynini.union("б", "г", "в", "ґ", "д", "ж", "з", "к", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
"Б", "Г", "Ґ", "Д", "Ж", "З", "К", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ"), "", SIGMA_STAR)
# є --> ie after all consonants except for <Л> and <л>


# rules for <Ю> and <ю> transcription:
@ pynini.cdrewrite(pynini.cross("Ю", "Ju"), pynini.union("[BOS]", " ", "-", ukr_vowels, "'" ), "", SIGMA_STAR)
# Ю --> 'Ju' word-initially, after vowles, and after the apostrophe
@ pynini.cdrewrite(pynini.cross("ю", "ju"), pynini.union("[BOS]", " ", "-", ukr_vowels, "'" ), "", SIGMA_STAR)
# ю --> 'ju' word-initially, after vowles, and after the apostrophe
@ pynini.cdrewrite(pynini.cross("ю", "u"), pynini.union("Л", "л"), "", SIGMA_STAR) # ю --> u after <Л> and <л>
@ pynini.cdrewrite(pynini.cross("ю", "iu"), 
pynini.union("б", "г", "в", "ґ", "д", "ж", "з", "к", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
"Б", "Г", "Ґ", "Д", "Ж", "З", "К", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ"), "", SIGMA_STAR)
# ю --> 'iu' after all consonants except for <Л> and <л> (see the rules for <Є> and <є> transcription)


# rules for <Я> and <я> transcription:
@ pynini.cdrewrite(pynini.cross("Я", "Ja"), pynini.union("[BOS]", " ", "-", ukr_vowels, "'" ), "", SIGMA_STAR)
# Я --> 'Ja' word-initially, after vowles, and after the apostrophe
@ pynini.cdrewrite(pynini.cross("я", "ja"), pynini.union("[BOS]", " ", "-", ukr_vowels, "'" ), "", SIGMA_STAR)
# я --> 'ja' word-initially, after vowles, and after the apostrophe
@ pynini.cdrewrite(pynini.cross("я", "a"), pynini.union("Л", "л"), "", SIGMA_STAR) # я --> a after <Л> and <л>
@ pynini.cdrewrite(pynini.cross("я", "ia"), 
pynini.union("б", "г", "в", "ґ", "д", "ж", "з", "к", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ",
"Б", "Г", "Ґ", "Д", "Ж", "З", "К", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ"), "", SIGMA_STAR)
# я --> 'ia' after all consonants except for <Л> and <л> (see the rules for <Є> and <є>, and <Ю> and <ю> transcription)


# rules for <Л> and <л> transcription:
@ pynini.cdrewrite(pynini.cross("Льо", "Lo"), "", "", SIGMA_STAR) # Льо --> Lo always!
@ pynini.cdrewrite(pynini.cross("льо", "lo"), "", "", SIGMA_STAR) # льо --> lo always!
@ pynini.cdrewrite(pynini.cross("Л", "L"), "", pynini.union("я", "є", "ю", "і", "ї", "ь"), SIGMA_STAR)
# Л --> L before <я>, <є>, <ю>, <і>, <ї>, <ь>
@ pynini.cdrewrite(pynini.cross("л", "l"), "", pynini.union("я", "є", "ю", "і", "ї", "ь"), SIGMA_STAR)
# л --> l before <я>, <є>, <ю>, <і>, <ї>, <ь>
@ pynini.cdrewrite(pynini.cross("Л", "Ł"), "", pynini.union("а", "е", "и", "о", "у", ukr_consonants_lower, "[EOS]"), SIGMA_STAR)
# Л --> Ł before <а>, <е>, <и>, <о>, <у>, consonants, and word-finally
@ pynini.cdrewrite(pynini.cross("л", "ł"), "", pynini.union("а", "е", "и", "о", "у", ukr_consonants_lower, "[EOS]"), SIGMA_STAR)
# л --> ł before <а>, <е>, <и>, <о>, <у>, consonants, and word-finally


# palatalization rules for <ь> transcription:
@ pynini.cdrewrite(pynini.cross("З", "Ź"), "", "ь", SIGMA_STAR) # Зь --> Ź palatalization
@ pynini.cdrewrite(pynini.cross("з", "ź"), "", "ь", SIGMA_STAR) # зь --> ź palatalization
@ pynini.cdrewrite(pynini.cross("С", "Ś"), "", "ь", SIGMA_STAR) # Сь --> Ś palatalization
@ pynini.cdrewrite(pynini.cross("с", "ś"), "", "ь", SIGMA_STAR) # сь --> ś palatalization
@ pynini.cdrewrite(pynini.cross("Ц", "Ć"), "", "ь", SIGMA_STAR) # Ць --> Ć palatalization
@ pynini.cdrewrite(pynini.cross("ц", "ć"), "", "ь", SIGMA_STAR) # ць --> ć palatalization
@ pynini.cdrewrite(pynini.cross("н", "ń"), "", "ь", SIGMA_STAR) # нь --> ń palatalization
# Polish forbids <ń> from occuring word-initially and therefore doesn't have to be capitalized
@ pynini.cdrewrite(pynini.cross("о", "io"), "ь", "", SIGMA_STAR) # ьо --> io palatalization
# Ukrainian forbids the soft sign form occuring word-initially, hence no need to capitalize


# everything else:
@ pynini.cdrewrite(pynini.cross("А", "A"), "", "", SIGMA_STAR) # А --> A everywhere
@ pynini.cdrewrite(pynini.cross("а", "a"), "", "", SIGMA_STAR) # а --> a everywhere
@ pynini.cdrewrite(pynini.cross("Б", "B"), "", "", SIGMA_STAR) # Б --> B everywhere
@ pynini.cdrewrite(pynini.cross("б", "b"), "", "", SIGMA_STAR) # б --> b everywhere
@ pynini.cdrewrite(pynini.cross("В", "W"), "", "", SIGMA_STAR) # В --> W everywhere
@ pynini.cdrewrite(pynini.cross("в", "w"), "", "", SIGMA_STAR) # в --> w everywhere
@ pynini.cdrewrite(pynini.cross("Г", "H"), "", "", SIGMA_STAR) # Г --> H everywhere
@ pynini.cdrewrite(pynini.cross("г", "h"), "", "", SIGMA_STAR) # г --> h everywhere
@ pynini.cdrewrite(pynini.cross("Ґ", "G"), "", "", SIGMA_STAR) # Ґ --> G everywhere
@ pynini.cdrewrite(pynini.cross("ґ", "g"), "", "", SIGMA_STAR) # ґ --> g everywhere
@ pynini.cdrewrite(pynini.cross("Д", "D"), "", "", SIGMA_STAR) # Д --> D everywhere
@ pynini.cdrewrite(pynini.cross("д", "d"), "", "", SIGMA_STAR) # д --> d everywhere
@ pynini.cdrewrite(pynini.cross("Е", "E"), "", "", SIGMA_STAR) # Е --> E everywhere
@ pynini.cdrewrite(pynini.cross("е", "e"), "", "", SIGMA_STAR) # е --> e everywhere
@ pynini.cdrewrite(pynini.cross("Ж", "Ż"), "", "", SIGMA_STAR) # Ж --> Ż everywhere
@ pynini.cdrewrite(pynini.cross("ж", "ż"), "", "", SIGMA_STAR) # ж --> ż everywhere
@ pynini.cdrewrite(pynini.cross("З", "Z"), "", "", SIGMA_STAR) # З --> Z everywhere
@ pynini.cdrewrite(pynini.cross("з", "z"), "", "", SIGMA_STAR) # з --> z everywhere
@ pynini.cdrewrite(pynini.cross("И", "Y"), "", "", SIGMA_STAR) # И --> Y everywhere
@ pynini.cdrewrite(pynini.cross("и", "y"), "", "", SIGMA_STAR) # и --> y everywhere
@ pynini.cdrewrite(pynini.cross("І", "I"), "", "", SIGMA_STAR) # І --> I everywhere
@ pynini.cdrewrite(pynini.cross("і", "i"), "", "", SIGMA_STAR) # і --> i everywhere
@ pynini.cdrewrite(pynini.cross("Ї", "Ji"), "", "", SIGMA_STAR) # Ї --> 'Ji' everywhere
@ pynini.cdrewrite(pynini.cross("ї", "ji"), "", "", SIGMA_STAR) # ї --> 'ji' everywhere
@ pynini.cdrewrite(pynini.cross("Й", "J"), "", "", SIGMA_STAR) # Й --> J everywhere
@ pynini.cdrewrite(pynini.cross("й", "j"), "", "", SIGMA_STAR) # й --> j everywhere
@ pynini.cdrewrite(pynini.cross("К", "K"), "", "", SIGMA_STAR) # К --> K everywhere
@ pynini.cdrewrite(pynini.cross("к", "k"), "", "", SIGMA_STAR) # к --> k everywhere
@ pynini.cdrewrite(pynini.cross("М", "M"), "", "", SIGMA_STAR) # М --> M everywhere
@ pynini.cdrewrite(pynini.cross("м", "m"), "", "", SIGMA_STAR) # м --> m everywhere
@ pynini.cdrewrite(pynini.cross("Н", "N"), "", "", SIGMA_STAR) # Н --> N everywhere
@ pynini.cdrewrite(pynini.cross("н", "n"), "", "", SIGMA_STAR) # н --> n everywhere
@ pynini.cdrewrite(pynini.cross("О", "O"), "", "", SIGMA_STAR) # О --> O everywhere
@ pynini.cdrewrite(pynini.cross("о", "o"), "", "", SIGMA_STAR) # о --> o everywhere
@ pynini.cdrewrite(pynini.cross("П", "P"), "", "", SIGMA_STAR) # П --> P everywhere
@ pynini.cdrewrite(pynini.cross("п", "p"), "", "", SIGMA_STAR) # п --> p everywhere
@ pynini.cdrewrite(pynini.cross("Р", "R"), "", "", SIGMA_STAR) # Р --> R everywhere
@ pynini.cdrewrite(pynini.cross("р", "r"), "", "", SIGMA_STAR) # р --> r everywhere
@ pynini.cdrewrite(pynini.cross("С", "S"), "", "", SIGMA_STAR) # С --> S everywhere
@ pynini.cdrewrite(pynini.cross("с", "s"), "", "", SIGMA_STAR) # с --> s everywhere
@ pynini.cdrewrite(pynini.cross("Т", "T"), "", "", SIGMA_STAR) # Т --> T everywhere
@ pynini.cdrewrite(pynini.cross("т", "t"), "", "", SIGMA_STAR) # т --> t everywhere
@ pynini.cdrewrite(pynini.cross("У", "U"), "", "", SIGMA_STAR) # У --> U everywhere
@ pynini.cdrewrite(pynini.cross("у", "u"), "", "", SIGMA_STAR) # у --> u everywhere
@ pynini.cdrewrite(pynini.cross("Ф", "F"), "", "", SIGMA_STAR) # Ф --> F everywhere
@ pynini.cdrewrite(pynini.cross("ф", "f"), "", "", SIGMA_STAR) # ф --> f everywhere
@ pynini.cdrewrite(pynini.cross("Х", "Ch"), "", "", SIGMA_STAR) # Х --> Ch everywhere
@ pynini.cdrewrite(pynini.cross("х", "ch"), "", "", SIGMA_STAR) # х --> ch everywhere
@ pynini.cdrewrite(pynini.cross("Ц", "C"), "", "", SIGMA_STAR) # Ц --> C everywhere
@ pynini.cdrewrite(pynini.cross("ц", "c"), "", "", SIGMA_STAR) # ц --> c everywhere
@ pynini.cdrewrite(pynini.cross("Ч", "Cz"), "", "", SIGMA_STAR) # Ч --> Cz everywhere
@ pynini.cdrewrite(pynini.cross("ч", "cz"), "", "", SIGMA_STAR) # ч --> cz everywhere
@ pynini.cdrewrite(pynini.cross("Ш", "Sz"), "", "", SIGMA_STAR) # Ш --> Sz everywhere
@ pynini.cdrewrite(pynini.cross("ш", "sz"), "", "", SIGMA_STAR) # ш --> sz everywhere
@ pynini.cdrewrite(pynini.cross("Щ", "Szcz"), "", "", SIGMA_STAR) # Щ --> Szcz everywhere
@ pynini.cdrewrite(pynini.cross("щ", "szcz"), "", "", SIGMA_STAR) # щ --> szcz everywhere


# cleaning up the soft signs and apostrophes
@ pynini.cdrewrite(pynini.cross("ь", ""), "", "", SIGMA_STAR) # removes the soft sign
@ pynini.cdrewrite(pynini.cross("'", ""), "", "", SIGMA_STAR) # removes the apostrophe

).optimize()