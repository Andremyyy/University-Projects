;12. Se dau 2 siruri de octeti A si B. 
;Sa se construiasca sirul R care sa contina 
;doar elementele pare si negative din cele 2 siruri. 
;Exemplu:
;A: 2, 1, 3, -3, -4, 2, -6
;B: 4, 5, -5, 7, -6, -2, 1
;R: -4, -6, -6, -2

assume cs:code,ds:data

; datele programului:

data segment

	A db 2, 1, 3, -3, -4, 2, -6
	lenA EQU $-A
	B db 4, 5, -5, 7, -6, -2, 1
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
		JGE pesteA
		
		cbw
		neg AX
		mov DL, 2
		idiv DL
		cmp AH, 1
		JE pesteA
		
		; e negativ si par
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
		JGE pesteB
		
		cbw
		neg AX
		mov DL, 2
		idiv DL
		cmp AH, 1
		JE pesteB
		
		; e negativ si par
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

