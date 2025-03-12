;11. Se dau 2 siruri de octeti A si B. 
;Sa se construiasca sirul R care 
;sa contina doar elementele impare si pozitive din cele 2 siruri. 
;Exemplu:
;A: 2, 1, 3, -3
;B: 4, 5, -5, 7
;R: 1, 3, 5, 7

assume cs:code,ds:data

; datele programului:

data segment

	A db 2, 1, 3, -3
	lenA EQU $-A
	B db 4, 5, -5, 7
	lenB EQU $-B
	R db lenA+lenB dup(0)

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:


	mov SI, 0
	mov DI, 0	

	mov CX, lenA

	repetaA:
		mov AL, A[SI]
		cmp AL, 0
		JL pesteA
		
		cbw
		mov DL, 2
		idiv DL
		cmp AH, 0
		JE pesteA
		
		; e pozitiv si impar
		mov AL, A[SI]
		mov R[DI], AL
		inc DI
		
		pesteA:
			inc SI 
		
	loop repetaA
	
	mov SI, 0
	mov CX, lenB

	repetaB:
		mov AL, B[SI]
		cmp AL, 0
		JL pesteB
		
		cbw
		mov DL, 2
		idiv DL
		cmp AH, 0
		JE pesteB
		
		; e pozitiv si impar
		mov AL, B[SI]
		mov R[DI], AL
		inc DI
		
		pesteB:
			inc SI 
		
	loop repetaB



;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
