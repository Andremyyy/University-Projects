; 13.z=((a+b)/c + 2*d)/e

assume cs:code,ds:data


; a - doubleword
; b - doubleword
; c - word
; d - byte
; e - byte


; 9 ( pt a = 6, b = 1, c = 1, d = 1, e = 1 )
; -9 = f7h ( pt a = 6, b = 1, c = 1, d = 1, e = -1)

; datele programului:

data segment
	
	a dd 6
	b dd 1
	c dw 1 
	d db 1
	e db -1 
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	;((a+b)/c + 2*d)/e
	
	; (a + b ) / c 
	
	mov AX, word ptr a 
	mov DX, word ptr a + 2
	add AX, word ptr b 
	adc DX, word ptr b + 2 
	
	idiv c    ; AX = cat = ( a + b) / c  => CX 
	mov CX, AX 
	
	; 2*d 
	
	mov AL, 2
	imul d    ; AX = 2 * d 
	
	; prima paranteza 
	
	add AX, CX   ; AX = ((a+b)/c + 2*d)
	
	idiv e       ; AL = cat = rezultat
	
	
	
	
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start