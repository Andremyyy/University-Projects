;10.z=(a*a+b*b)/(a*a-b*b-5).

assume cs:code,ds:data


; a - byte
; b - byte

; 36/ 30 = 1  ( pt a = 6, b = 1)

; datele programului:

data segment
	
	a db 6
	b db 1
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; (a*a+b*b)/(a*a-b*b-5)

	; PARANTEZA A DOUA
	
	mov AL, a
	imul a 
	mov CX, AX 
	mov AL, b 
	imul b 
	sub CX, AX 
	sub CX, 5 
	
	; CX = a doua paranteza 
	
	; prima paranteza 
	
	mov AL, a 
	imul a 
	mov BX, AX 
	
	mov AL, b 
	imul b 
	add BX, AX
	
	; impartirea:
	
	mov AX, BX 
	cwd 
	idiv CX   ; AX = cat = rezultat 
	
	
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start