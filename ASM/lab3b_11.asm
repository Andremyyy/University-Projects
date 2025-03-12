;11. Se da un sir de dublucuvinte. 
;Sa se calculeze si sa se salveze in sirul D 
;toti octetii superiori ai wordurilor superioare 
;care au ultima cifra egala cu 8.

assume cs:code,ds:data

; datele programului:

data segment

	S dd 12345578h, 87654321h, 6C456889h, 58002345h
	lenS EQU $-S
	D db lenS dup(0)
	
	; in MEMORIE:

; 78 55 34 12 21 43 65 87 89 68 45 6C 45 23 00 58
;          --          --          --          --          

	; octetii -- sunt octetii superiori ai cuvintelor superioare


	; deci => (in zecimal: 12h = 18, 6Ch = 108, 58h = 88)
	
	; d = 12h, 6Ch, 58h
	

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov CX, lenS/4    				; pt loop repeta
mov SI, 0						; pt a parcurge sirul S
mov DI, 0       				; pt a parcurge sirul D 

repeta:
	mov AL, byte ptr S[SI+3]
	
	cmp AL, 0
	JGE ulitima_cifra
	
	; e negativ
	neg AL
	
	ulitima_cifra:
		cbw							;AL->AX
		mov BL, 10
		idiv BL						; AL = cat si AH = rest
		
		CMP AH, 8
			JNE peste
		
		
		mov AL, byte ptr S[SI+3]
		mov D[DI], AL
		inc DI
			
		peste:
			add SI, 4
		
loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start