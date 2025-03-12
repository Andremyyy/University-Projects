;15. Se da un sir de dublucuvinte. 
;Sa se salveze in sirul D in ordine inversa
; toate cuvintele din sirul initial.


; s in memorie:

;	78 56 34 12 32 54 76 98 13 12 10 11

assume cs:code,ds:data

data segment

s dd 12345678h, 98765432h, 11101213h
len EQU $-s
D dw len/2 dup(0)

; d = 1213h, 1110h, 5432h, 9876h, 5678h, 1234h

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov SI, len-1
mov DI, 0
mov CX, len/4

repeta:
	mov AL, byte ptr s[SI-2]
	mov AH, byte ptr s[SI-3]
	
	
	mov d[DI], AX
	add DI,2
	
	mov AL, byte ptr s[SI]
	mov AH, byte ptr s[SI-1]
	
	mov d[DI], AX
	add DI, 2
	
	sub SI, 4
loop repeta

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start