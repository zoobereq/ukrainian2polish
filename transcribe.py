#!/usr/bin/env python
"""The main"""


import pynini
from pynini.lib import rewrite
from g2g_rules import G2G


def ukr2pl(ukrainian_string):
    polonized_string = rewrite.one_top_rewrite(ukrainian_string, G2G)
    return polonized_string

def main():
    ukr_name = input("Enter the Ukrainian name(s):  ")
    pl_name = ukr2pl(ukr_name)
    print(f"The transcribed Polish name(s): {pl_name}")

if __name__ == "__main__":
    main()
    
    
    