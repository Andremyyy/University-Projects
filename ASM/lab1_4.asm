; 4. z=(a*3+b*b*5)/(a*a+a*b)-a-b


; a - byte
; b - byte

; pt a = 2, b = 2 => z = 3 - 4 = -1  = ffff
; pt a = 10, b = 1 => z = 0 - 11 = -11  = fff5

assume cs:code,ds:data

; datele programului:

data segment
	
	a db 2
	b db 2
	interm dd 0
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; z=(a*3+b*b*5)/(a*a+a*b)-a-b
	
	
	; a * a + a * b 
	
	mov AL, a 
	imul a 
	
	mov BX, AX 
	
	mov AL, a 
	imul b 
	
	add BX, AX   ; BX = a * a + a * b 
	
	; a*3+b*b*5
	
	mov AL, a
	mov CL, 3 
	imul CL 
	mov CX , AX   ; CX = a * 3 
	
	mov AL, b 
	imul b 
	mov DX, 5 
	imul DX   ; DX:AX = b * b * 5
	
	mov word ptr interm, AX 
	mov word ptr interm + 2 , DX 
	
	mov AX, CX 
	cwd 		; DX:AX = a * 3
	
	add  word ptr interm , ax
	adc  word ptr interm + 2, DX
	
	; interm = a * 3 + b * b * 5
	
	; a * a + a * b 
	
	mov AL, a 
	imul a 
	
	mov BX , AX 
	
	mov AL, a 
	imul b 
	
	add BX, AX   ; BX = a * a + a * b 
	
	; impartirea :
	
	mov AX, word ptr interm 
	mov DX, word ptr interm + 2
	
	idiv BX    ; AX = cat 
	
	mov CX , AX   ; CX = impartirea  
	
	
	; impartire - a - b 
	
	mov AL, a 
	cbw 
	sub CX, AX    ; CX = impartirea - a 
	
	
	mov Al, b 
	cbw 
	sub CX, AX    ; CX = rez final
	
		
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start