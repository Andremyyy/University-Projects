;9. Se da un sir de dublucuvinte. 
;Sa se calculeze si sa se salveze in sirul D 
;toti octetii inferiori ai wordurilor superioare care au valoare para si negativa.

assume cs:code,ds:data

; datele programului:

data segment

	S dd 12345678h, 12FC3434h , 1234FFFEh, 12FE3456h, 12FF1212h
	lenS EQU $-S
	D db lenS dup(0)
	
	; in MEMORIE:

; 78 56 34 12 34 34 FC 12 FE FF 34 12 56 34 FE 12 12 12 FF 12
;       --          --          --          --          --

	; octetii -- sunt octetii inferiori ai cuvintelor superioare


	; deci => 
	
	; d = FCh, FEh
	

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
	mov AL, byte ptr S[SI+2]
	
	cmp AL, 0
	JGE peste
	
	cbw							;AL->AX
	neg AX
	mov BL, 2
	idiv BL						; AL = cat si AH = rest
	
	CMP AH, 0
		JNE peste
	
	
	mov AL, byte ptr S[SI+2]
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