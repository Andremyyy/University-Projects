assume cs:code,ds:data

; datele programului:


data segment

a db 00001010b ; 10 -> 2
b db 00111111b ; 63 -> 7
;c db 10101010b ; 170 -> 5
c db 11111011b ; -5 -> -6
d db 11110101b ; 245(-11) -> -5

suma dw 0

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov AL, a
cbw
sar AX, 2    ;extind semnul
and AX, 00000111b
add DX, AX


mov AL, b
cbw
sar AX, 2    ;extind semnul
and AX, 00000111b
add DX, AX

mov AL, c
cbw                 
sar AX, 2           
and AX, 00000111b     
add DX, AX          

mov AL, d
cbw
sar AX, 2    ;extind semnul
and AX, 00000111b
add DX, AX

mov suma, DX

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start