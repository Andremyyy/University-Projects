;6.Se da un sir de octeti S. 
;Sa se obtina sirul D1 ce contine toate numerele pare din S 
;si sirul D2 ce contine toate numerele impare din S. 

;Exemplu:
;S: 1, 5, 3, 8, 2, 9
;D1: 8, 2
;D2: 1, 5, 3, 9

assume cs:code,ds:data

; datele programului:

data segment

	S db 1, 5, 3, 8, 2, 9
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
		cbw
		mov DL, 2
		idiv DL
		cmp AH, 1
		JE impar
		
		; element par => in D1
		mov AL, S[SI]
		mov D1[DI], AL
		inc DI
		jmp peste
		
		impar: 	
			; element impar => in D2
			mov AL, S[SI]
			mov D2[BX], AL
			inc BX
			
		peste:
			inc SI
	loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
