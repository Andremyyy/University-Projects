;Se da un numar n (0<n<256) in segmentul de date. 
;Sa se genereze si sa se afiseze pe ecran 
;primele n numere din sirul lui Fibonnaci (incepand cu 0, 1).
;Exemplu:
;n = 10
;rezultat: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

; !!!NU MERGE

assume cs:code,ds:data

; datele programului:

data segment

	n db 10
	a dw 0
	b dw 1
	contor db 0
	nr_cifre dw 0

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	
	; afisez primul element
	mov DL, '0'
	mov AH, 02h
	int 21h
	
	mov DL, ' '
	mov AH, 02h
	int 21h
	
	mov contor, 1
	
	mov AL, n
	dec AL
	mov n, AL
	
	cmp AL, 1
	JNE continua
	
	continua:
		
		calcul:
			mov AL, n
			cmp contor, AL
			JGE gata
			
			; afisez b
			
			
			; trebuie afisat numarul
		
			mov nr_cifre, 0
			din_cifre_pe_stiva:
				mov AX, b
				mov DX, 0
				mov CX, 10
				div CL
				
				; catul
				mov b, AX
				
				;restul
				push DX
				inc nr_cifre
				cmp AX, 0
				JNE din_cifre_pe_stiva
			
			
			mov CX, nr_cifre
			de_pe_stiva_in_caractere:
				pop DX
				add DL, '0'
				mov AH, 02h
				int 21h
			loop de_pe_stiva_in_caractere
			
			
			mov DL, ' '
			mov AH, 02h
			int 21h
			
			; a devine b
			; b devine a + b
			
			mov BX, a
			mov CX, b 
			mov a, CX 
			add CX, BX
			mov b, CX
			
			inc contor
			mov AL, n
			
			jmp calcul
	
	gata:	
		; ultimul numar
		mov nr_cifre, 0
		
		din_cifre_pe_stiva_ultimul:
				mov AX, b
				mov DX, 0
				mov CX, 10
				div CL
				
				; catul
				mov b, AX
				
				;restul
				push DX
				inc nr_cifre
				cmp AX, 0
				JNE din_cifre_pe_stiva_ultimul
			
			
			mov CX, nr_cifre
			de_pe_stiva_in_caractere_ultimul:
				pop DX
				add DL, '0'
				mov AH, 02h
				int 21h
			loop de_pe_stiva_in_caractere_ultimul
			
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start