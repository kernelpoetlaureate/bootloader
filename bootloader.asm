

bits 16                
start:

org 0x7C00
bits 16
start:
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x0000 
    mov si, message
    call print_string
    jmp $



print_string:
    lodsb
    or al, al
    jz .done
    mov ah, 0x0E
    mov bh, 0x00
    int 0x10
    jmp print_string
.done:
    ret


message db "Hello, Buttloader!", 0
times 510 - ($ - $$) db 0
dw 0xAA55
