;5. Se da un sir de octeti S de lungime l. 
;Sa se construiasca sirul D de lungime l-1 
;astfel incat elementele din D sa reprezinte
;diferenta dintre fiecare 2 elemente consecutive din S. 

;Exemplu:
;S: 1, 2, 4, 6, 10, 20, 25
;D: 1, 2, 2, 4, 10, 5

assume cs:code,ds:data

; datele programului:

data segment

	S db 1, 2, 4, 6, 10, 20, 25
	l EQU $-S
	D db l-1 dup (0)

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0
	mov DI, 0
	mov CX, l-1
	
	repeta:
		mov AL, S[SI]
		mov BL, S[SI+1]
		sub BL, AL
		mov D[DI], BL
		inc SI 
		inc DI 
	loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
