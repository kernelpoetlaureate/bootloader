import subprocess
import os
import sys

BOOTLOADER_ASM = "bootloader.asm"
BOOTLOADER_BIN = "bootloader.bin"

# Check if NASM is installed

def check_nasm():
    try:
        subprocess.run(["nasm", "-v"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def assemble_bootloader():
    print("[+] Assembling bootloader...")
    result = subprocess.run([
        "nasm", "-f", "bin", BOOTLOADER_ASM, "-o", BOOTLOADER_BIN
    ])
    if result.returncode != 0:
        print("[-] NASM failed to assemble the bootloader.")
        sys.exit(1)
    print(f"[+] Created {BOOTLOADER_BIN}")

def run_qemu():
    print("[+] Running bootloader in QEMU...")
    try:
        subprocess.run(["qemu-system-x86_64", BOOTLOADER_BIN])
    except FileNotFoundError:
        print("[-] QEMU is not installed or not in PATH.")
        sys.exit(1)

def main():
    if not check_nasm():
        print("[-] NASM assembler is not installed or not in PATH.")
        print("    Download from https://www.nasm.us/ and add to your PATH.")
        sys.exit(1)
    if not os.path.exists(BOOTLOADER_ASM):
        print(f"[-] {BOOTLOADER_ASM} not found in the current directory.")
        sys.exit(1)
    assemble_bootloader()
    run_qemu()

if __name__ == "__main__":
    main()
