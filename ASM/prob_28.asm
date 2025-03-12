;Se citesc de la tastatura doua cuvinte A si B. 
;Sa se calculeze si sa se afiseze cuvantul pe ecran cuvantul C astfel:
;- bitii 0-3 ai lui C coincid cu bitii 4-7 ai lui A
;- bitii 4-7 ai lui C coincid cu bitii 1-4 ai lui B
;- bitii 8-10 ai lui C sunt 0
;- bitii 11-15 ai lui C coincid cu bitii 7-11 ai lui B
;Exemplu:
;A = 12487
;B = 35147
;C = 36956

; !!!! NU ARE FACUTA CITIREA  !!!



; A = a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15
; B = b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15

; C = a4 a5 a6 a7 b1 b2 b3 b4 0 0 0 b7 b8 b9 b10 b11

; fie A = 1100 1110 1101 0011 (2) = 52947 (10)
; fie B = 1011 1011 0101 1110 (2) = 47966 (10)

; => C = 1110 1011 0001 0101 (2) = 60181 (10)



assume cs:code,ds:data

; datele programului:


data segment

	;zonaCitire_A dw 17, ?, 20 dup(?)
	;zonaCitire_B dw 17, ?, 20 dup(?)
	A dw 52947 ; = 1100111011010011 (2)
	B dw 47966 ; = 1011101101011110 (2)
	C dw 0

suma dw 0

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; CITIRE A 
	;mov DX, offset zonaCitire_A
	;mov AH, 09h
	;int 21h
	
	;call citire_baza_10
	;mov A, AX
	
	; CITIRE B 
	;mov DX, offset zonaCitire_B
	;mov AH, 09h
	;int 21h
	
	;call citire_baza_10
	;mov B, AX

	mov AX, A     ; AX = a0 a1 a2 a3 a4 a5 a6  a7  a8  a9  a10 a11 a12 a13 a14 a15
	shl AX, 4     ; AX = a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 0    0   0   0   
	and AX, 1111000000000000b     ; AX = a4 a5 a6 a7 0 0 0 0 0 0 0 0 0 0 0 0
	
	
	mov BX, B     ; BX = b0 b1 b2 b3 b4  b5  b6  b7  b8  b9  b10 b11 b12 b13 b14 b15
	shr BX, 4     ; BX =  0  0  0  0 b0  b1  b2  b3  b4  b5  b6  b7  b8  b9  b10 b11
	and BX, 0000111100000000b
	or AX, BX 
	
	
	mov BX, B     ; BX = b0 b1 b2 b3 b4  b5  b6  b7  b8  b9  b10 b11 b12 b13 b14 b15
	shr BX, 4	  ; BX =  0  0  0  0 b0  b1  b2  b3  b4  b5  b6  b7  b8  b9  b10 b11
	and BX, 0000000000011111b
	or AX, BX 
	
	mov C, AX
	
	afisare_stiva_C_baza_10:
		mov BX, 0   ; nr_cifre
		pe_stiva:
			mov AX, C
			mov DX, 0
			mov CX, 10
			div CX 
			
			inc BX
			;catul
			mov C, AX
			
			; restul merge pe stiva
			push DX
			
			cmp AX, 0
			JNE pe_stiva
			
		mov CX, BX
		din_stiva:
			pop DX
			add DL, '0'
			mov AH, 02h
			int 21h
		loop din_stiva

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
