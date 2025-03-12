;8.z=(a+b+c+1)^3/(a-b*c+d)

assume cs:code,ds:data


; a - byte
; b - byte
; c - byte
; d - word

; 125 / 5 = 25 = 19h  ( a = 2, b = 1, c = 1, d = 5)
; 125 / -5 = -25 = ffe7h  ( a = 2, b = 1, c = 1, d = -6)

; datele programului:

data segment
	
	a db 2
	b db 1
	c db 1
	d dw -6
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; (a+b+c+1)^3/(a-b*c+d)
	
	; a - b * c + d 
	
	mov AL, b 
	imul c   ; AX = b * c => CX 
	mov CX, AX 
	
	mov AL, a 
	cbw       ; AX = a 
	
	sub AX, CX 
	add AX, d    ; AX = a - b * c + d    => BX
	
	mov BX, AX   ; BX = a - b * c + d 
	
	
	; (a + b + c + 1 ) ^ 2 
	
	mov AL, a
	add AL, b 
	add AL, c 
	add AL, 1 
	mov CL, AL 
	imul CL     ; AX = (a + b + c + 1 ) ^ 2 
	
	
	; (a + b + c + 1 ) ^ 3 
	
	mov DX, AX   ; dx = paran la a doua
	mov AL, CL   ; a + b + c + 1 
	cbw          ; AX = a + b + c + 1
	imul DX      ; DX:AX = rezultat 
	
	
	; impartire 
	
	idiv BX    ; AX = cat = rezultat
	
	
		
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start