;1. Se da un sir de octeti S de lungime l. 
;Sa se construiasca sirul D de lungime l-1 
;astfel incat elementele din D sa reprezinte 
;produsul dintre fiecare 2 elemente consecutive S(i) si S(i+1) din S. 

;Exemplu:
;S: 1, 2, 3, 4
;D: 2, 6, 12

assume cs:code,ds:data

; datele programului:

data segment

	S db 1,2,-1,3,4
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
		imul BL
		mov D[DI], AL
		inc SI 
		inc DI 
	loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start