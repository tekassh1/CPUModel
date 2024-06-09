; read a byte from stdin
mov eax, 3		; sys_read system call
push dword 1		; input length
push dword variable	; address to pass to
push dword 0		; read from standard input
push eax
int 0x80		; call the kernel
add esp, 16		; move back the stack pointer

; write a byte to stdout
mov eax, 4		; sys_write system call
push dword 1		; output length
push dword variable	; memory address
push dword 1		; write to standard output
push eax
int 0x80		; call the kernel
add esp, 16		; move back the stack pointer

; quit the program
mov eax, 1		; sys_exit system call
push dword 0		; program return value
push eax
int 0x80		; call the kernel