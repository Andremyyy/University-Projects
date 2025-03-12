;Se da un sir de dublucuvinte. 
;Sa se genereze sirul D care sa contina 
;toti octetii inferiori ai word-urilor superioare 
;care au valoare divizibila cu 10. Sa se afiseze sirul D (in baza 10) pe ecran. 
;In cazul in care nu exista niciun octet corespunzator, sa se afiseze mesajul "Nu exista".
;Exemplu:
;S: 120A3478h, AB32CDABh, C5F3B1E5h
;D: 0Ah, 32h
;rezultat: 10, 50

assume cs:code,ds:data

; datele programului:

data segment

	S dd 390A3431h, 12FC3434h , 6B325BFEh, 1B78B1E2h
	lenS EQU $-S
	D db lenS dup(0)
	nr_cifre dw 0
	mesaj db 'Nu exista$'
	
	; in MEMORIE:

; D4 31 0A 39 34 34 FC 12 FE 5B 32 6B E2 B1 78 1B 
; 	    --          --          --          --          

	; octetii -- sunt octetii inferiori ai cuvintelor superioare


	; deci => 
	
	; d = 0Ah, 32h, 78h
	
	; se va afisa:
	; 10, 50, 120
	

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
		
		cbw							;AL->AX
		neg AX
		mov BL, 10
		idiv BL						; AL = cat si AH = rest
		
		CMP AH, 0
			JNE peste
			
		
		mov AL, byte ptr S[SI+2]
		mov D[DI], AL
		inc DI
		
		pozitiv:
			mov AH, 0
			mov BL, 10
			div BL						; AL = cat si AH = rest
			
			CMP AH, 0
				JNE peste
				
			
			mov AL, byte ptr S[SI+2]
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
	
	cmp DI, 0
	JNE afisare
	
	; nu exista elemente ca in cerinta
	
	mov DX, offset mesaj
	mov AH, 09h
	int 21h

	afisare:
		
		cmp SI, DI
		JGE final
		
		mov AL, D[SI]
		cmp AL, 0
		JGE pozitiv_afisare
		
		; afisez '-'
		mov DL, '-'
		mov AH, 02h
		int 21h
		
		mov AL, D[SI]
		neg AL
		
		pozitiv_afisare:
		
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

