;Se da un numar n (0<n<256) in segmentul de date. 
;Sa se genereze primii n termeni din sirul lui Fibonacci 
;si sa se afiseze pe ecran al n-lea termen.
;Exemplu:
;n = 6
;rezultat: 8

assume cs:code,ds:data

; datele programului:

data segment

	n db 11
	a db 1
	b db 1
	contor db 0
	nr_cifre dw 0
	; rezultat pt n = 11 => 89

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	
	mov AL, n
	cmp AL, 1
	JE afiseaza_1
	
	inc contor
	
	mov AL, n
	dec AL
	mov n, AL
	
	cmp AL, 1
	JE afiseaza_1
	
	continua:
		
		calcul:
			cmp contor, AL
			JGE afiseaza_b
			
			; a devine b
			; b devine a + b
			
			mov BL, a
			mov CL, b 
			mov a, CL 
			add CL, BL 
			mov b, CL 
			
			inc contor
			mov AL, n
			
			jmp calcul
	
	afiseaza_1:
		mov DL, '1'
		mov AH, 02h
		int 21h
	
	afiseaza_b:	
		
		mov DL, b
		
		cmp DL, 10
		JGE stiva
		
		add DL, '0'
		mov AH, 02h
		int 21h
		jmp gata
		
		stiva:
			mov nr_cifre, 0
			din_cifre_pe_stiva_final:
				mov AL, b
				mov AH, 0
				mov DX, 0
				mov CX, 10
				div CX
				mov b, AL
				push DX
				inc nr_cifre
				cmp AX, 0
				JNE din_cifre_pe_stiva_final
				
				
			mov CX, nr_cifre
			de_pe_stiva_in_caractere_final:
				pop DX
				add DL, '0'
				mov AH, 02h
				int 21h
			loop de_pe_stiva_in_caractere_final	
			
	gata:
			
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start