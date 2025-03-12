;1. z=1/(a*a+b*b-5)+2/(a*a-b*b+4)

; pt a = 2 si b = 3 => z = -2 => FFFEh

; a - byte
; b - byte

assume cs:code,ds:data

; datele programului:

data segment
	
	a db 2
	b db 3
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; a * a si salvam in CX 
	
	mov AL, a
	mov BL, a
	imul BL     ; AX = a * a
	mov CX, AX  ; CX = a * a
	
	; b * b si salvam in BX 
	
	mov AL, b
	mov BL, b
	imul BL		; AX = b * b
	mov BX, AX   ; BX = b * b
	
	; a * a + b * b - 5  si calculam in CX 
	
	add CX, BX 
	sub CX, 5
	
	; CX = a * a + b * b - 5
	
	; pregatim impartirea ( DX:AX / CX  -> AX - cat, DX - rest ) si salvam catul in CX 
	
	mov AX, 1
	mov DX, 0
	idiv CX    ; AX - cat, DX - rest 
	mov CX, AX    ; CX = 1 / ( a*a+b*b-5)
	
	; a * a 
	
	mov AL, a
	mov DL, a
	imul DL     ; AX = a * a
	
	; calculam in AX a * a - b * b + 4 si stocam rezulatul in BX 
	
	sub AX, BX   ; AX = a * a - b * b
	add AX, 4
	mov BX, AX 	; BX = a * a - b * b + 4
	
	; pregatim impartirea ( DX:AX / BX  -> AX - cat, DX - rest ) si salvam catul in BX 
	
	mov AX, 2
	mov DX, 0
	idiv BX 	; AX - cat, DX - rest
	
	mov BX, AX  
	
	
	; efectuam adunarea caturilor pt rezultatul final
	
	add CX, BX  ; CX = rezultatul final
	
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start