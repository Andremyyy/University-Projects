;Se da un numar n (0<n<256) in segmentul de date. 
;Sa se genereze si sa se afiseze pe ecran 
;primii n termeni din sirul lui Fibonacci.
;Exemplu:
;n = 6
;rezultat: 1, 1, 2, 3, 5, 8


; !!! trebuie si transformarea unui nr mai de mare 10 in caractere (in prob_3)

assume cs:code,ds:data

; datele programului:

data segment

	n db 6
	a db 1
	b db 1
	contor db 0

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	
	; afisez primul element
	mov DL, '1'
	mov AH, 02h
	int 21h
	
	mov DL, ' '
	mov AH, 02h
	int 21h
	
	inc contor
	
	mov AL, n
	dec AL
	mov n, AL
	
	cmp AL, 1
	JNE continua
	
	continua:
		
		calcul:
			cmp contor, AL
			JGE gata
			
			; afisez b
			
			mov DL, b
			add DL, '0'
			mov AH, 02h
			int 21h
			
			mov DL, ' '
			mov AH, 02h
			int 21h
			
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
	
	gata:	
		; ultimul numar
		
		mov DL, b
		add DL, '0'
		mov AH, 02h
		int 21h
			
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
