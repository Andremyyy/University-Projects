; 15.z=((a+b*c-d)/f+h)/g

assume cs:code,ds:data


; a - word
; b - byte
; c - byte
; d - word
; f - byte
; h - byte
; g - byte

; -1  ( a = 2, b = 3, c = 1, d = 3, f = 1, h = 1, g = 1) 

; datele programului:

data segment
	
	a dw -2
	b db 3
	c db 1
	d dw 3
	f db 1
	h db 1
	g db 1 
	interm dd 0
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; ((a+b*c-d)/f+h)/g
	
	; a + b * c - d
	
	mov AL, b 
	imul c 
	add AX, a 
	sub AX, d   ; AX = a + b * c - d 
	
	idiv f 		; AL = (a+b*c-d)/f
	
	add AL, h	; AL = (a+b*c-d)/f + h 
	
	; impartire
	
	cbw   ; AX = paranteza mare 
	
	idiv g    ; AL = cat = rezultatul
	
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start