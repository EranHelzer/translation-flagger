import argparse

parser = argparse.ArgumentParser()

parser.add_argument("files", nargs="+", help="Files to check")
parser.add_argument("--skip", nargs="*", help="Stages to skip")
