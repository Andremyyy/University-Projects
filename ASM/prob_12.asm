;Se da un sir de dublucuvinte. 
;Sa se genereze sirul D care sa contina 
;toti octetii inferiori ai word-urilor inferioare
; care au valoare para si negativa. Sa se afiseze sirul D (in baza 10) pe ecran.
;Exemplu:
;S: 123456D4h, ABCDEFABh, C5F3B1E2H 
;D: D4h, E2h
;rezultat: -44, -30


assume cs:code,ds:data

; datele programului:

data segment

	S dd 123456D4h, 12FC3434h , 1234FFFEh, 12FE34E2h
	lenS EQU $-S
	D db lenS dup(0)
	nr_cifre dw 0
	
	; in MEMORIE:

; D4 56 34 12 34 34 FC 12 FE FF 34 12 E2 34 FE 12 
; --          --          --          --          

	; octetii -- sunt octetii inferiori ai cuvintelor superioare


	; deci => 
	
	; d = D4h, FEh, E2h
	
	; se va afisa:
	; -44, -2, -30
	

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
		mov AL, byte ptr S[SI]
		
		cmp AL, 0
		JGE peste
		
		cbw							;AL->AX
		neg AX
		mov BL, 2
		idiv BL						; AL = cat si AH = rest
		
		CMP AH, 0
			JNE peste
		
		
		mov AL, byte ptr S[SI]
		mov D[DI], AL
		inc DI
			
		peste:
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
		
		; afisez '-'
		mov DL, '-'
		mov AH, 02h
		int 21h
		
		mov AL, D[SI]
		neg AL
		
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