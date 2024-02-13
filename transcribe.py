#!/usr/bin/env python
"""The main"""


import pynini
from pynini.lib import rewrite
from g2g_transcribe_rules import G2G_transcribe


def ukr2pl_transcribe(ukrainian_string):
    polonized_string = rewrite.one_top_rewrite(ukrainian_string, G2G_transcribe)
    return polonized_string

def main():
    ukr_name = input("Enter the Ukrainian name(s):  ")
    pl_name_transcribed = ukr2pl_transcribe(ukr_name)
    print(f"The transcribed Polish name(s): {pl_name_transcribed}")

if __name__ == "__main__":
    main()
    
    
    
