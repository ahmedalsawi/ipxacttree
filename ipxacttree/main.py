import argparse
import json

def main():
    from ipxacttree.ipxacttree import IPXACTTree

    # Command line parser
    parser = argparse.ArgumentParser(description="ipxact parser and generator")

    parser.add_argument("ipxactfile")
    args = parser.parse_args()

    t = IPXACTTree(args.ipxactfile)
    print(t)
