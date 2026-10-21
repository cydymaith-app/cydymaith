#!/usr/bin/env python3
"""Builds the site: python3 build.py [OUTDIR] [--project DIR] [--edition NAME] [--strict]. The generator is the framework
submodule in framework/; see framework/phrasebook/cli.py for the options."""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "framework"))

from phrasebook.cli import main  # noqa: E402

if __name__ == "__main__":
    main(projects_dir=HERE / "content")
