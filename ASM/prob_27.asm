;Se citesc de la tastatura doua cuvinte A si B. Sa se calculeze si sa se afiseze 
;cuvantul pe ecran cuvantul C astfel:
;- bitii 0-3 ai lui C coincid cu bitii 6-9 ai lui A
;- bitii 4-6 ai lui C au valoarea 1
;- bitii 7-10 ai lui C coincid cu bitii 0-3 ai lui A
;- bitii 11-15 ai lui C coincid cu bitii 3-7 ai lui B
;Exemplu:
;A = 42590 = 1010011001011110
;B = 15955 = 0011111001010011
;C = 22393 = 1001111101011110


; !!!! NU ARE FACUTA CITIREA  !!!



; A = a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15
; B = b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15

; C = b6 b7 b8 b9 1 1 1 a0 a1 a2 a3 b3 b4 b5 b6 b7

; fie A = 1100111011010011 (2) = 52947 (10)
; fie B = 1011101101011110 (2) = 47966 (10)

; => C = 1101 1111 1001 1011 (2) = 57243 (10)




assume cs:code,ds:data

; datele programului:


data segment

	zonaCitire_A dw 17, ?, 20 dup(?)
	;zonaCitire_B dw 17, ?, 20 dup(?)
	A dw 52947 ; = 1100111011010011 (2)
	B dw 47966 ; = 1011101101011110 (2)
	C dw 0
	zece dw 10

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
	;mov AH, 0Ah
	;int 21h
	
	;mov CX, zonaCitire_A[1]
	;mov AX, 0
	;mov A, AX
	;mov SI, 2
	;dec CX
	
	;din_caract_in_numar:
	;	mov AX, zonaCitire_A[SI]
	;	sub AX, '0'
	;	mov BX, AX 
	;	mov AX, A 
	;	mov DX, 0 
	;	mul zece
	;	; ax - cat
	;	add AX, BX 
	;	mov A, AX 
	;	inc SI
	;loop din_caract_in_numar
	
	; CITIRE B 
	;mov DX, offset zonaCitire_B
	;mov AH, 09h
	;int 21h
	
	;call citire_baza_10
	;mov B, AX

	mov AX, B     ; AX = b0 b1 b2 b3 b4  b5  b6  b7  b8  b9  b10 b11 b12 b13 b14 b15
	shl AX, 6     ; AX = b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 0    0   0   0   0   0
	and AX, 1111000000000000b     ; AX = b6 b7 b8 b9 0 0 0 0 0 0 0 0 0 0 0 0
	
	or AX, 0000111000000000b      ; AX = b6 b7 b8 b9 1 1 1 0 0 0 0 0 0 0 0 0
	
	mov BX, A     ; BX = a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15
	shr BX, 7     ; BX =  0  0  0  0  0  0  0 a0 a1 a2 a3  a4  a5  a6  a7  a8
	and BX, 0000000111100000b
	or AX, BX
	
	mov BX, B     ; BX = b0 b1 b2 b3 b4  b5  b6  b7  b8  b9  b10 b11 b12 b13 b14 b15
	shr BX, 8	  ; BX = 0  0  0  0   0   0   0   0   b0 b1  b2  b3  b4   b5  b6  b7
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

