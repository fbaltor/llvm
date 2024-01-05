#!/usr/bin/python3

import os
import argparse


LLVM_TOOLS = [
    "bugpoint",
    "clang",
    "clang++",
    "clang-cpp",
    "clangd",
    "count",
    "dsymutil",
    "FileCheck",
    "ld64.lld",
    "ld.lld",
    "llc",
    "lld",
    "lldb",
    "lldb-argdumper",
    "lldb-instr",
    "lldb-server",
    "lldb-vscode",
    "lld-link",
    "lli",
    "lli-child-target",
    "llvm-addr2line",
    "llvm-ar",
    "llvm-as",
    "llvm-bcanalyzer",
    "llvm-bitcode-strip",
    "llvm-cat",
    "llvm-cfi-verify",
    "llvm-config",
    "llvm-cov",
    "llvm-c-test",
    "llvm-cvtres",
    "llvm-cxxdump",
    "llvm-cxxfilt",
    "llvm-cxxmap",
    "llvm-debuginfo-analyzer",
    "llvm-debuginfod",
    "llvm-debuginfod-find",
    "llvm-diff",
    "llvm-dis",
    "llvm-dlltool",
    "llvm-dwarfdump",
    "llvm-dwarfutil",
    "llvm-dwp",
    "llvm-exegesis",
    "llvm-extract",
    "llvm-gsymutil",
    "llvm-ifs",
    "llvm-install-name-tool",
    "llvm-jitlink",
    "llvm-jitlink-executor",
    "llvm-lib",
    "llvm-libtool-darwin",
    "llvm-link",
    "llvm-lipo",
    "llvm-lto",
    "llvm-lto2",
    "llvm-mc",
    "llvm-mca",
    "llvm-ml",
    "llvm-modextract",
    "llvm-mt",
    "llvm-nm",
    "llvm-objcopy",
    "llvm-objdump",
    "llvm-opt-report",
    "llvm-otool",
    "llvm-pdbutil",
    "llvm-PerfectShuffle",
    "llvm-profdata",
    "llvm-profgen",
    "llvm-ranlib",
    "llvm-rc",
    "llvm-readelf",
    "llvm-readobj",
    "llvm-reduce",
    "llvm-remark-size-diff",
    "llvm-remarkutil",
    "llvm-rtdyld",
    "llvm-sim",
    "llvm-size",
    "llvm-split",
    "llvm-stress",
    "llvm-strings",
    "llvm-strip",
    "llvm-symbolizer",
    "llvm-tapi-diff",
    "llvm-tblgen",
    "llvm-tli-checker",
    "llvm-undname",
    "llvm-windres",
    "llvm-xray",
    "not",
    "obj2yaml",
    "opt",
    "sanstats",
    "split-file",
    "UnicodeNameMappingGenerator",
    "verify-uselistorder",
    "wasm-ld",
    "yaml2obj",
    "yaml-bench",
]


def validate_arg(args):
    return False


def main():
    parser = argparse.ArgumentParser(
        prog="LLVMVersionLinkFixer",
        description="Naive program to create symlinks in /usr/bin of an installed llvm version",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--version")
    group.add_argument("--src")
    args = parser.parse_args()


    if not validate_arg(args):
        print("error")


if __name__ == "__main__":
    main()
