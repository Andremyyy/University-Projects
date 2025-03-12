;3. z=(3+(c*c))/(6-(b*b))+((a*a-b*b)/(a*a+c*c))


; a - byte 
; b - byte
; c - byte

; pt a = 2, b = 1, c = 2 => z = 1 
; pt a = 2 , b = 4 , c = 3 => z = -1



assume cs:code,ds:data

; datele programului:

data segment
	
	a db 2
	b db 1
	c db 2
	
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; z=(3+(c*c))/(6-(b*b))+((a*a-b*b)/(a*a+c*c))
	
	; 6 - b * b in BX 
	
	mov AL, b
	imul b 		; AX = b * b 
	
	mov BX, 6
	sub BX, AX  ; BX = 6 - b * b
	
	; 3 + c * c in AX 
	
	mov AL, c 
	imul c 
	add AX, 3 	; AX = 3 + c * c 
	
	; pregatim impartirea, adica DX:AX / BX  => AX - cat, DX - rest
	
	cwd    ; mov DX, 0  ( e positiv in orice caz) 
	idiv BX   ; AX - cat 
	
	; salvam primul cat in CX 
	mov CX, AX    	; CX = (3+(c*c))/(6-(b*b))
	
	; a * a + c * c 
	
	mov AL, a
	imul a 
	
	mov BX, AX  ; BX = a * a 
	
	mov AL, c
	imul c 
	
	add BX, AX  ; BX = a * a + c * c 
	
	; a * a - b * b 
	
	mov AL, a 
	imul a 
	
	mov DX, AX  ; DX = a * a 
	
	mov AL, b 
	imul b 
	
	sub DX, AX   ; DX = a * a - b * b 
	
	; pregatim impartirea ...
	
	mov AX, DX 
	cwd    ; sau mov DX, 0 
	idiv BX 
	
	; catul este in AX 
	
	add CX, AX   ; CX = rezultat
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start