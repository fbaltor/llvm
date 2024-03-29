#!/usr/bin/python3

import argparse
from pathlib import Path


LLVM_VERSIONS = ["11", "12", "13", "14", "15", "16", "17", "18", "19"]

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


def symlink_with_version(version):
    if version not in LLVM_VERSIONS:
        raise TypeError("LLVMVersionLinkFixer: error: Not a valid llvm version")

    llvm_bin_dir = Path(f"/usr/lib/llvm-{version}/bin")
    if not llvm_bin_dir.is_dir():
        raise OSError(
            f"LLVMVersionLinkFixer: error: {str(llvm_bin_dir)} does not exists"
        )

    existent_tools = [item.name for item in llvm_bin_dir.iterdir()]
    diff_tools = list(set(LLVM_TOOLS) - set(existent_tools))
    if diff_tools:
        print("Missing the following tools")
        print(*diff_tools, sep=", ")
        raise OSError(
            f"LLVMVersionLinkFixer: error: {str(llvm_bin_dir)} does not contain all llvm tools"
        )

    usr_bin_dir = Path("/usr/bin")
    for tool in LLVM_TOOLS:
        link = usr_bin_dir / tool
        if link.is_file():
            link.unlink()
        link.symlink_to(llvm_bin_dir / tool)


def symlink_with_src(src):
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(
        prog="LLVMVersionLinkFixer",
        description="Naive program to create symlinks in /usr/bin of an installed llvm \
                version under Unix systems",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-v", "--version")
    group.add_argument("--src")
    args = parser.parse_args()

    if args.version and args.src:
        raise TypeError(
            "LLVMVersionLinkFixer: error: \
                    argument --src: not allowed with argument -v/--version"
        )

    if args.version is None and args.src is None:
        raise TypeError(
            "LLVMVersionLinkFixer: error: \
                    one of the arguments -v/--version --src is required"
        )

    if args.version is not None:
        symlink_with_version(args.version)

    if args.src is not None:
        symlink_with_src(args.src)


if __name__ == "__main__":
    main()
