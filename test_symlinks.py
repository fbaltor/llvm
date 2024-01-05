#!/usr/bin/python3

import argparse
from pathlib import Path

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", required=True)
    args = parser.parse_args()

    usr_bin_dir = Path("/usr/bin")
    llvm_bin_dir = Path(f"/usr/lib/llvm-{args.version}/bin")

    if not llvm_bin_dir.is_dir():
        raise OSError

    ok = []
    failed = []
    for tool in LLVM_TOOLS:
        if (usr_bin_dir / tool).resolve() == (llvm_bin_dir / tool).resolve():
            ok.append(tool)
            print(f"{tool}: OK")
        else:
            failed.append(tool)
            print(f"{tool}: FAILED")

    if not failed:
        print("\nAll tools are properly symlinked")
    else:
        print("\nThe following tools failed to be verified:")
        print(*failed, sep=", ")


if __name__ == "__main__":
    main()
