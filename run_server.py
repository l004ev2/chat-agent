# -*- coding: utf-8 -*-

import uvicorn
import argparse


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env_file", default="dev.env")
    args, unknown = parser.parse_known_args()
    return args


if __name__ == "__main__":
    args = args_parse()
    uvicorn.run("src:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                reload_includes="timestamp.tmp",
                env_file=args.env_file,
                reload_dirs=["./src"])
