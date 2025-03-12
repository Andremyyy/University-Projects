;10. Se da un sir de dublucuvinte. 
;Sa se calculeze si sa se salveze in sirul D 
;toti octetii superiori ai wordurilor inferioare care au valoare impara si pozitiva.

assume cs:code,ds:data

; datele programului:

data segment

	S dd 12345578h, 87654321h, 23456889h, 00002345h
	lenS EQU $-S
	D db lenS dup(0)
	
	; in MEMORIE:

; 78 55 34 12 21 43 65 87 89 68 45 12 45 23 00 00
;    --          --          --          --          

	; octetii -- sunt octetii inferiori ai cuvintelor superioare


	; deci => (in zecimal: 55h = 85, 43h = 67, 23h = 35)
	
	; d = 55h, 43h, 23h
	

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
	mov AL, byte ptr S[SI+1]
	
	cmp AL, 0
	JL peste
	
	cbw							;AL->AX
	mov BL, 2
	idiv BL						; AL = cat si AH = rest
	
	CMP AH, 1
		JNE peste
	
	
	mov AL, byte ptr S[SI+1]
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