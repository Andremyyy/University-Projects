;4. Se da un sir de octeti S. 
;Sa se construiasca sirul D astfel: 
;sa se puna mai intai elementele de pe pozitiile pare din S 
;iar apoi elementele de pe pozitiile impare din S. 

;Exemplu:
;S: 1, 2, 3, 4, 5, 6, 7, 8, 9
;D: 1, 3, 5, 7, 9, 2, 4, 6, 8


assume cs:code,ds:data

; datele programului:

data segment

	S db 1, 2, 3, 4, 5, 6, 7, 8, 9
	len EQU $-S
	D db len dup(0)

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0
	mov DI, 0
	
	mov AL, len
	mov AH, 0
	mov BL, 2
	div BL
	cmp AH, 1
	JE impar
	
	;lungime para => len/2 si len/2
	mov CX, len/2
	jmp repeta_poz_pare
	
	impar:
		; lungime impara => len/2 + 1 si len/2
		mov CX, len/2 + 1
	
	repeta_poz_pare:
		mov AL, S[SI]
		mov D[DI], AL
		inc DI
		add SI, 2
	loop repeta_poz_pare
	
	mov SI, 1
	mov CX, len/2
	
	repeta_poz_impare:
		mov AL, S[SI]
		mov D[DI], AL
		inc DI
		add SI, 2
	loop repeta_poz_impare


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start