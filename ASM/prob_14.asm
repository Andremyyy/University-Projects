;Se da un sir de dublucuvinte. Sa se genereze sirul D 
;care sa contina toti octetii inferiori ai word-urilor superioare
; care au ultima cifra egala cu 8. 
;Sa se afiseze sirul D (in baza 10) pe ecran.
;Exemplu:
;S: 12443478h, AB32CDABh, C576B1E5h
;D: 44h, 76h
;rezultat: 68, 118

assume cs:code,ds:data

; datele programului:

data segment

	S dd 123419D4h, 12443434h , 123273FEh, 127632E2h
	lenS EQU $-S
	D db lenS dup(0)
	nr_cifre dw 0
	
	; in MEMORIE:

; D4 19 34 12 34 34 44 12 FE 73 32 12 E2 32 76 12 
;       --          --          --          --          

	; octetii -- sunt octetii inferiori ai cuvintelor superioare


	; deci => 
	
	; d = 44h, 76h
	
	; se va afisa:
	; 68, 118
	

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
		mov AL, byte ptr S[SI+2]
		
		cmp AL, 0
		JGE pozitiv
		
		; e negativ 
		cbw 
		neg AX
		mov BL, 10
		idiv BL						; AL = cat si AH = rest
		
		CMP AH, 8
			JNE incrementare
			
		; negativ cu ult cifra 8	
		mov AL, byte ptr S[SI+2]
		mov D[DI], AL
		inc DI
		
		pozitiv:
			mov AH, 0
			mov BL, 10
			div BL						; AL = cat si AH = rest
			
			CMP AH, 8
				JNE incrementare
				
			; pozitiv cu ult cifra 8	
			mov AL, byte ptr S[SI+2]
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
