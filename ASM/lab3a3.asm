;3.Se dau doua siruri de octeti S1 si S2 de aceeasi lungime. 
;Sa se construiasca sirul D astfel: 
;fiecare element de pe pozitiile pare din D este suma elementelor de pe pozitiile corespunzatoare din S1 si S2,
; iar fiecare element de pe pozitiile impare are ca si valoare diferenta elementelor de pe pozitiile corespunzatoare din S1 si S2. 

;Exemplu:
;S1: 1, 2, 3, 4
;S2: 5, 6, 7, 8
;D: 6, -4, 10, -4

assume cs:code,ds:data

; datele programului:

data segment

	S1 db 1,2,3,4
	len EQU $-S1
	S2 db 5,6,7,8
	D db len dup(0)
	doi db 2

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0	; pt S1
	mov BX, 0	; pt S2
	mov DI, 0   ; pr D
	mov CX, len
	
	repeta:
		mov AX, DI
		idiv doi		; AL = cat si AH = rest
		cmp AH, 1	
		je impar
		
		; pozitie para => suma
		
		mov AL, S1[SI]
		add AL, S2[BX]
		mov D[DI], AL
		jmp peste
		
		impar:
			mov AL, S1[SI]
			sub AL, S2[BX]
			mov D[DI], AL
		
		peste:
			inc SI 
			inc BX 
			inc DI 
			
	loop repeta
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start