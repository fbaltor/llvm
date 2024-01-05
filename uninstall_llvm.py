#!/usr/bin/python3

import argparse
import subprocess

LLVM_VERSIONS = ["11", "12", "13", "14", "15", "16", "17", "18"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", required=True)
    args = parser.parse_args()
    llvm_version = args.version

    if llvm_version not in LLVM_VERSIONS:
        raise TypeError(f"llvm version must be one of {LLVM_VERSIONS}")

    packages_to_uninstall = [
        f"clang-{llvm_version}",
        f"lldb-{llvm_version}",
        f"lld-{llvm_version}",
        f"clangd-{llvm_version}",
        f"clang-tidy-{llvm_version}",
        f"clang-format-{llvm_version}",
        f"clang-tools-{llvm_version}",
        f"llvm-{llvm_version}-dev",
        f"llvm-{llvm_version}-tools",
        f"libomp-{llvm_version}-dev",
        f"libc++-{llvm_version}-dev",
        f"libc++abi-{llvm_version}-dev",
        f"libclang-common-{llvm_version}-dev",
        f"libclang-{llvm_version}-dev",
        f"libclang-cpp{llvm_version}-dev",
        f"libunwind-{llvm_version}-dev",
        f"libclang-rt-{llvm_version}-dev",
        f"libpolly-{llvm_version}-dev",
    ]

    command = ["sudo", "apt", "purge"]
    command.extend(packages_to_uninstall)
    subprocess.run(command)


if __name__ == "__main__":
    main()
