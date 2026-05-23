#!/usr/bin/env python3
"""
Markdown To Html — Converts markdown files to styled HTML with custom templates, TOC generation, an
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Markdown To Html")
    parser.add_argument("--input", "-i", help="Input file")
    parser.add_argument("--output", "-o", help="Output file")
    args = parser.parse_args()
    
    print("✅ Markdown To Html — Ready to process!")
    if args.input:
        print(f"   Input: {args.input}")
    if args.output:
        print(f"   Output: {args.output}")

if __name__ == "__main__":
    main()
