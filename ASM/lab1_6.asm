; 6.z=(a-b*c/d)/(c+2-a/b)+5

assume cs:code,ds:data

; rez = 15 = 0F ( a = 15, b = 5, c = 2, d = 2 )


; datele programului:

data segment
	
	a dw 15
	b db 5
	c db 2
	d db 2
	interm dd 0
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; z=(a-b*c/d)/(c+2-a/b)+5
	
	
	; c + 2 - a / b 
	
	mov AX, a 
	idiv b    ; al - cat , ah - rest 
	
	mov BL, c
	add BL, 2 
	sub BL, AL 
	
	; BL = c + 2 - a / b 
	
	; (a-b*c/d)
	
	mov AL, b 
	imul c   ; AX = b * c 
	idiv d   ; AL - cat 
	
	cbw      ; AX = b * c / d 
	mov CX, a 
	sub CX, AX    ; CX = (a-b*c/d)
	
	
	; impartirea:
	mov AX, CX
	idiv BL      ; AL = cat 
	
	add AL, 5    

	; AL = rezultat 
		
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start