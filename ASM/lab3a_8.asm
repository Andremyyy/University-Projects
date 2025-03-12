;8.Se da un sir de octeti S. 
;Sa se construiasca un sir D1 care sa contina toate numerele pozitive 
;si un sir D2 care sa contina toate numerele negative din S. 
;Exemplu:
;S: 1, 3, -2, -5, 3, -8, 5, 0
;D1: 1, 3, 3, 5, 0
;D2: -2, -5, -8

assume cs:code,ds:data

; datele programului:

data segment

	S db 1, 3, -2, -5, 3, -8, 5, 0
	l EQU $-S
	D1 db l dup (0)
	D2 db l dup (0)

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0  ; pt S
	mov DI, 0  ; pt D1
	mov BX, 0  ; pt D2
	
	mov CX, l
	
	repeta:
		mov AL, S[SI]
		cmp AL, 0
		JGE pozitiv
		
		; element negativ => in D2
		mov D2[BX], AL
		inc BX
		jmp peste
		
		pozitiv: 	
			; element pozitiv => in D1
			mov D1[DI], AL
			inc DI
			
		peste:
			inc SI
	loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start