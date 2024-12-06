bits 64
default rel

extern fopen
extern fclose
extern fgetc
extern putchar
extern printf
extern ExitProcess

section .text
global main  

%define EOF -1
%define EOL 10

; why not assembly? ;)

main:     
    push rbp
    mov rbp, rsp
    sub rsp, 128 ; Reserve stack shadow space + Preallocate general stack space

    lea rcx, [file_name_str]
    lea rdx, [file_open_mode]
    call fopen
    mov qword [file_handle], rax

    test rax, rax
    jnz _main_no_file_error
    lea rcx, [printf_file_error_fmt]
    call printf
_main_no_file_error:

    mov r12d, 0 ; r12d - x
    mov r13d, 0 ; r13d - y
    lea rdi, [file_contents]
_main_file_read_loop_begin:
    mov rcx, qword [file_handle]
    call fgetc
    mov r10d, eax
    
    cmp r10d, EOF
    je _main_file_read_loop_end

    cmp r10d, EOL
    jne _main_file_read_loop_not_EOL
    mov dword [width], r12d
    mov r12d, 0
    inc r13d
    jmp _main_file_read_loop_begin
_main_file_read_loop_not_EOL:

    cmp r10d, '^'
    jne _main_file_read_loop_not_guard
    mov dword [g_px], r12d
    mov dword [g_py], r13d
_main_file_read_loop_not_guard:

    mov byte [rdi], r10b
    inc rdi
    inc r12d
    jmp _main_file_read_loop_begin
_main_file_read_loop_end:
    inc r13d
    mov dword [height], r13d
    mov byte [rdi], 0

    mov rcx, qword [file_handle]
    call fclose

    ; replace ^ with . in the file contents
    mov ecx, dword [g_py]
    imul ecx, dword [width]
    add ecx, dword [g_px]
    lea rdx, [file_contents]
    add rdx, rcx
    mov byte [rdx], '.'

_main_core_loop_begin:
    mov r12d, dword [g_px] ; r12d - new x
    add r12d, dword [g_dx]
    mov r13d, dword [g_py] ; r13d - new y
    add r13d, dword [g_dy]

    cmp r12d, 0
    jl _main_core_loop_not_inside
    cmp r12d, dword [width]
    jge _main_core_loop_not_inside

    cmp r13d, 0
    jl _main_core_loop_not_inside
    cmp r13d, dword [height]
    jge _main_core_loop_not_inside

    ; is inside the bounds

    mov ecx, r13d
    imul ecx, dword [width]
    add ecx, r12d
    lea rdx, [file_contents]
    add rdx, rcx
    cmp byte [rdx], '#'
    jne _main_core_loop_not_colliding

    ; colliding with #
    ; rotate
    mov ecx, dword [g_dx]
    mov edx, dword [g_dy]
    imul edx, -1
    mov dword [g_dx], edx
    mov dword [g_dy], ecx
    jmp _main_core_loop_begin

_main_core_loop_not_colliding:
    ; move onwards
    mov ecx, dword [g_px]
    mov edx, dword [g_py]

    mov eax, edx
    imul eax, dword [width]
    add eax, ecx
    lea rbx, [file_contents]
    add rbx, rax
    mov byte [rbx], 'X'

    add ecx, dword [g_dx]
    add edx, dword [g_dy]

    mov dword [g_px], ecx
    mov dword [g_py], edx
    jmp _main_core_loop_begin
_main_core_loop_not_inside:
    mov eax, dword [g_py]
    imul eax, dword [width]
    add eax, dword [g_px]
    lea rbx, [file_contents]
    add rbx, rax
    mov byte [rbx], 'X'
    jmp _main_core_loop_end
_main_core_loop_end:

    mov rax, 0 
    lea rdi, [file_contents]
_main_result_loop_begin:
    mov r10b, byte [rdi]

    cmp r10b, 0
    je _main_result_loop_end

    cmp r10b, 'X'
    jne _main_result_loop_not_X
    inc rax
_main_result_loop_not_X:

    inc rdi
    jmp _main_result_loop_begin
_main_result_loop_end:

    lea rcx, [d_printf_fmt]
    mov edx, eax
    call printf

    mov rcx, 0
    call ExitProcess ; Restores stack shadow space

section .bss
align 4
file_handle: resq 1
file_contents: resb 20480
width: resd 1
height: resd 1
g_px: resd 1
g_py: resd 1

section .data
align 4
g_dx: dd 0
g_dy: dd -1

section .rodata
align 4
file_name_str: db "input.txt", 0
file_open_mode: db "r", 0
d_printf_fmt: db "%d", 10, 0
printf_file_error_fmt: db "Failed to open the input.txt file!", 10, 0