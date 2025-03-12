;15. Se dau 2 siruri de octeti S1 si S2 de aceeasi lungime. 
;Sa se construiasca sirul D astfel incat 
;fiecare element din D sa reprezinte minumul dintre elementele 
;de pe pozitiile corespunzatoare din S1 si S2. 
;Exemplu:
;S1: 1, 3, 6, 2, 3, 7
;S2: 6, 3, 8, 1, 2, 5
;D: 1, 3, 6, 1, 2, 5


assume cs:code,ds:data

; datele programului:

data segment

	S1 db 1, 3, 6, 2, 3, 7
	len EQU $-S1
	S2 db 6, 3, 8, 1, 2, 5
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

	mov CX, len	

	repeta:
		mov AL, S1[SI]
		mov BL, S2[SI]
		cmp AL, BL
		JGE bigger_AL
		
		; al < bl
		mov D[DI], AL 
		jmp peste
		
		bigger_AL:
			mov D[DI], BL
		
		peste:
			inc SI 
			inc DI
	loop repeta



;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start


