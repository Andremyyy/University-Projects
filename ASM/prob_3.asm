;Se da un numar n (0<n<256) in segmentul de date. 
;Sa se genereze si sa se afiseze pe ecran secventa 3, 6, 9, ..., 3n-3, 3n.
;Exemplu:
;n = 6
;rezultat: 3, 6, 9, 12, 15, 18

assume cs:code,ds:data

; datele programului:

data segment

	n db 6
	maxim dw 0
	primul dw 3
	nr_cifre dw 0
	copie dw 0

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov AL, n
	mov BL, 3
	mul BL
	mov maxim, AX
	
	mov BX, maxim
	
	repeta:
		cmp primul, BX
		jge gata
		
		mov AX, primul
		mov copie, AX 
		
		; trebuie afisat numarul
		
		din_cifre_pe_stiva:
			mov AX, primul
			mov DX, 0
			mov CX, 10
			div CX
			mov primul, AX
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
		
		mov nr_cifre, 0
		mov AX, copie
		mov primul, AX
		add primul, 3
		jmp repeta
		
	gata:
		mov nr_cifre, 0
		din_cifre_pe_stiva_final:
			mov AX, primul
			mov DX, 0
			mov CX, 10
			div CX
			mov primul, AX
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
		
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
