;Se da un sir de dublucuvinte. 
;Sa se genereze sirul D care sa contina 
;toti octetii superiori ai word-urilor inferioare
; care au valoare impara si divizibila cu 5. 
;Sa se afiseze sirul D (in baza 10) pe ecran.
;Exemplu:
;S: 12341978h, ABCD14ABh, C5F373E5h 
;D: 19h, 73h
;rezultat: 25, 115

assume cs:code,ds:data

; datele programului:

data segment

	S dd 123419D4h, 12FC3434h , 123473FEh, 12FE32E2h
	lenS EQU $-S
	D db lenS dup(0)
	nr_cifre dw 0
	
	; in MEMORIE:

; D4 19 34 12 34 34 FC 12 FE 73 34 12 E2 32 FE 12 
;    --          --          --          --          

	; octetii -- sunt octetii inferiori ai cuvintelor superioare


	; deci => 
	
	; d = 19h, 73h
	
	; se va afisa:
	; 25, 115
	

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov CX, lenS/4    				; pt loop repeta
	mov SI, 0						; pt a parcurge sirul S
	mov DI, 0       				; pt a parcurge sirul D 

	repeta:
		mov AL, byte ptr S[SI+1]
		
		cmp AL, 0
		JGE pozitiv
		
		; e negativ 
		cbw 
		neg AX
		mov BL, 5
		idiv BL						; AL = cat si AH = rest
		
		CMP AH, 0
			JNE incrementare
			
		mov AL, byte ptr S[SI+1]
		cbw
		neg AX
		mov BL, 2
		idiv BL
		cmp AH, 1
			JNE incrementare
			
		; negativ, div cu 5, impar	
		mov AL, byte ptr S[SI+1]
		mov D[DI], AL
		inc DI
		
		pozitiv:
			mov AH, 0
			mov BL, 5
			div BL						; AL = cat si AH = rest
			
			CMP AH, 0
				JNE incrementare
				
			mov AL, byte ptr S[SI+1]
			mov AH, 0
			mov BL, 2
			div BL
			cmp AH, 1
				JNE incrementare
				
			; pozitiv, div cu 5, impar	
			mov AL, byte ptr S[SI+1]
			mov D[DI], AL
			inc DI
			
		incrementare:
			add SI, 4
			
	loop repeta


	mov SI, 0   ; pt a parcurge D din nou
	
	; Cod pentru a afișa un rând nou
	mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
	mov AH, 02h        
	int 21h            

	mov DL, 10         ; Line feed (cod ASCII 10, '\n')
	mov AH, 02h        
	int 21h

	afisare:
		
		cmp SI, DI
		JGE final
		
		mov AL, D[SI]
		cmp AL, 0
		JGE nu_afisez_minus
		
		; afisez '-'
		mov DL, '-'
		mov AH, 02h
		int 21h
		
		mov AL, D[SI]
		neg AL
		
		nu_afisez_minus:
		
			mov nr_cifre, 0
			din_cifre_pe_stiva_final:
				mov AH, 0
				mov DX, 0
				mov CX, 10
				div CX
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
		
		
			inc SI
			
			cmp SI, DI
			JGE final
			
			mov DL, ','
			mov AH, 02h
			int 21h
	
	jmp afisare

final:

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
