; 5. z=(a+b+c+1) *(a+b+c+1) /((a-b+d)*(a-b+d))

assume cs:code,ds:data

; rez = 12 = 0C ( a = 2, b = 2, c = 2, d = 2 )


; datele programului:

data segment
	
	a db 2
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

	; z=(a+b+c+1) *(a+b+c+1) /((a-b+d)*(a-b+d))
	
	
	; (a - b + d) ^ 2
	
	mov AL, a 
	sub AL, b
	add AL, d 
	
	mov BL, AL 
	imul BL 
	
	; AX = ( a - b + d ) ^ 2 
	mov CX, AX     ; CX = impartitorul 
	
	; (a + b + c + 1 ) ^ 2
	
	mov AL, a
	add AL, b 
	add AL, c 
	add AL, 1 
	
	mov BL, AL 
	imul BL 
	
	; AX = (a + b + c + 1 ) ^ 2
	
	; pregatim impartirea....
	
	cwd 
	idiv CX   ; AX = cat 
	
	mov CX, AX  ; CX = rez
		
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start