; 14.z= ((a*c-b*d)/f +(a+b)*c/d)/h

assume cs:code,ds:data


; a - word
; b - word
; c - word
; d - word
; f - word
; h - byte

; 4/ 2 = 2  ( a = 2, b = 3, c = 1, d = 1, f = 1, h = 2)
; -4 / 2 = -2 = FEh

; datele programului:

data segment
	
	a dw -2
	b dw 3
	c dw 1
	d dw 1
	f dw 1
	h db 2
	interm dd 0
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; ((a*c-b*d)/f +(a+b)*c/d)/h
	
	; (a * c - b * d ) / f 
	
	mov AX, a 
	imul c 
	
	; DX:AX  = a * c 
	
	mov word ptr interm, AX 
	mov word ptr interm + 2, DX 
	
	mov AX, b 
	imul d 
	
	sub word ptr interm, AX 
	sbb word ptr interm + 2, DX  ; interm = (a * c - b * d )
	
	mov AX, word ptr interm 
	mov DX, word ptr interm + 2 
	
	idiv f     ; AX = (a * c - b * d ) / f => CX 
	mov CX, AX 
	
	; (a+b)*c/d
	
	mov AX, a 
	add AX, b 
	imul c   ; DX:AX 
	idiv d   ; AX = cat = (a+b)*c/d
	
	; facem paranteza mare, adica ((a*c-b*d)/f +(a+b)*c/d)
	
	add AX, CX   ; AX = ((a*c-b*d)/f +(a+b)*c/d)
	
	; IMPARTIM LA h
	
	idiv h    ; AL = cat = rezultat
	
	
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start