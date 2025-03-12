;14. Se dau 2 siruri de octeti A si B. 
;Sa se construiasca sirul R care sa contina elementele lui B in ordine inversa 
;urmate de elementele negative ale lui A. 
;Exemplu:
;A: 2, 1, -3, 3, -4, 2, 6
;B: 4, 5, 7, 6, 2, 1
;R: 1, 2, 6, 7, 5, 4, -3, -4

assume cs:code,ds:data

; datele programului:

data segment

	A db 2, 1, -3, 3, -4, 2, 6
	lenA EQU $-A
	B db 4, 5, 7, 6, 2, 1
	lenB EQU $-B
	R db lenA+lenB dup(0)

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov DI, 0    ; pt R

	mov SI, lenB - 1
	mov CX, lenB

	repetaB:
		mov AL, B[SI]
		mov R[DI], AL
		inc DI
		dec SI 
	loop repetaB


	mov SI, 0
	mov CX, lenA

	repetaA:
		mov AL, A[SI]
		
		cmp AL, 0
		JGE pesteA
		
		; e  negativ
		mov AL, A[SI]
		mov R[DI], AL
		inc DI
		
		pesteA:
			inc SI 
		
	loop repetaA
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
