; SET B - siruri de CUVINTE/DUBLUCUVINTE

; CERINTA: (problema 2)

;	Se da un sir de dublucuvinte. 
;	Sa se obtina sirul format din octetii superiori ai cuvitelor superioare 
;		din elementele sirului de dublucuvinte care sunt divizibili cu 3.



assume cs:code,ds:data

; datele programului:

data segment

	S dd 12345678h, 1A2B3C4Dh, 122B3C4Dh, 2E2B3C4Dh , 18345678h, 302B3C4Dh
	lenS EQU $-S
	D db lenS dup(0)
	
	; in MEMORIE:

; 78 56 34 12 4D 3C 2B 1A 4D 3C 2B 12 4D 3C 2B 2E 78 56 34 18 4D 3C 2B 30
;          --          --          --          --          --          --

	; octetii -- sunt octetii superiori ai cuvintelor superioare


	; deci => (in decimal 18h = 24 si 30h = 36, 2Eh = 46, 1A = 26)
	
	; d = 12h, 12h, 18h, 30h
	

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
	cbw							;AL->AX
	mov BL, 3
	idiv BL						; AL = cat si AH = rest
	
	CMP AH, 0
		JE isDiv
		JNE isNotDiv
	
	isDiv:
		mov AL, byte ptr S[SI+3]
		mov D[DI], AL
		inc DI
		add SI, 4
		JMP next
	isNotDiv:
		add SI, 4
		next:
loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start