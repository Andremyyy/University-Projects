;Se da un sir de cuvinte S in segmentul de date.
; Sa se construiasca sirul D care sa contina produsul
;octetilor fiecarui cuvant din sirul S 
; si sa se afiseze acest sir pe ecran.
; Se va folosi implementarea fara semn.

;Exemplu
;S: 1A2Bh, 2C46h, 78DCh, 1213h
;D: 1118, 3080, 26400, 342

assume cs:code,ds:data

; datele programului:

data segment

	S dw 1A2Bh, 2C46h, 78DCh, 1213h
	lenS EQU ($-S)/2
	D dw lenS dup (0)
	nr_cifre dw 0

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0  ; pt S
	mov DI, 0  ; pt D
	
	mov CX, lenS
	
	repeta:
		mov AX, S[SI]
		mov BL, AH
		mov AL, AL
		
		mul BL
		
		mov D[DI], AX
		
		add SI, 2
		add DI, 2
		
	loop repeta
	
	
	; afisez fiecare sir 
	
	
	
	; Cod pentru a afișa un rând nou
	mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
	mov AH, 02h        
	int 21h            

	mov DL, 10         ; Line feed (cod ASCII 10, '\n')
	mov AH, 02h        
	int 21h  

	mov CX, lenS
	mov SI, 0	
	mov nr_cifre, 0
	
	afisare_D:
	
		mov AX, D[SI]
		add SI, 2
		
		pozitiv:
			mov BX, 10
			pe_stiva:
				xor DX, DX
				div BX			; AX - cat , DX-rest
				push DX 
				inc nr_cifre
				cmp AX, 0
				JNE pe_stiva
		
			din_stiva:
				pop DX
				add DL, '0'
				mov AH, 02h
				int 21h
				dec nr_cifre
				jnz din_stiva
		
			
			mov DX, lenS*2
			cmp SI, DX
			JE skip_virgula
		
			mov DL, ','          ; Separator
			mov AH, 02h
			int 21h
			
			skip_virgula:
		
	loop afisare_D
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start