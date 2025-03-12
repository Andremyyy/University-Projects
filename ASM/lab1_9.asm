; 9.z=((a+1)*(a+1)+2)^2/(b*b+c*c)

assume cs:code,ds:data


; a - byte
; b - byte
; c - byte

; 121 / 2 = 60  = 3Ch ( a = 2, b = 1, c = 1)

; datele programului:

data segment
	
	a db 2
	b db 1
	c db 1
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; ((a+1)*(a+1)+2)^2/(b*b+c*c)
	
	; b * b + c * c 
	
	mov AL, b 
	imul b 
	mov CX, AX 
	
	mov AL, c 
	imul c 
	add CX, AX   ; CX = a doua paranteza 
	
	; (a+1)^2 + 2 
	
	mov AL, a 
	add AL, 1 
	mov BL, AL 
	imul BL 
	add AX, 2  ; AX = (a + 1) ^ 2 + 2
	
	; AX ^ 2 
	
	mov BX, AX 
	imul BX   ; DX:AX = ((a+1)*(a+1)+2)^2
	
	; impartirea 
	
	idiv CX   ; AX = cat = rezultatul
	
	
	
	
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start