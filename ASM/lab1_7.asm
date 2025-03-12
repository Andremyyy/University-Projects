;7.z=(5*a-b/7)/(3/b+a*a) la fel ca prob 7 din lab1

assume cs:code,ds:data


; a - byte
; b - word

; 12 / 9 => 1 ( pt a = 3, b = 21)
; - 18 / 9 => -2 ( pt a = -3, b = 21)


; datele programului:

data segment
	
	a db -3
	b dw 21
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; (5*a-b/7)/(3/b+a*a)
	
	
	; 3 / b + a * a
	
	mov AX, 3
	mov DX, 0 
	idiv b    ; AX = cat  => CX 
	mov CX , AX 
	
	mov AL, a 
	imul a 
	
	add CX, AX   ; CX = a doua paranteza
	
	; 5 * a - b / 7
	
	mov AX, b 
	mov BL, 7 
	idiv BL   ; AL = cat => BL 
	mov BL, AL 
	
	mov AL, 5 
	imul a    ; AX = 5 * a => DX 
	mov DX, AX 
	
	mov AL, BL 
	cbw 
	; AX = b/7
	
	sub DX, AX   ; DX = prima paranteza
	
	;impartirea:
	
	mov AX, DX 
	cwd 
	idiv CX   ; AX - cat, DX - rest 
	
	; AX = rezultat
		
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start