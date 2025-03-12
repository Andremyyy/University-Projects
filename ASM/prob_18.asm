;Sa dau doua sirurui de octeti A si B. 
;Sa se construiasca sirul D1 care sa contina
;doar numerele pare si pozitive din A si B 
;si sirul D2 care sa contina numerele negative
;divizibile cu 3 din sirurile A si B. 
;Sa se afiseze pe ecran sirurile rezultat.
;Exemplu:
;A: 2, 1, -3, 3, -4, 12, 6
;B: 4, 5, 7, -18, 2, 1
;D1: 2, 12, 6, 4, 2
;D2: -3, -18


;!!!NU MERGE

assume cs:code,ds:data

; datele programului:

data segment

	A db 2, 1, -3, 3, -4, 12, 6
	lenA EQU $-A
	B db 4, 5, 7, -18, 2, 1
	lenB EQU $-B
	D1 db lenA+lenB dup (0)
	D2 db lenA+lenB dup (0)
	nr_cifre dw 0

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0  ; pt A si B
	mov DI, 0  ; pt D1
	mov BX, 0  ; pt D2
	
	mov CX, lenA
	
	repeta_A:
		mov AL, A[SI]
		cmp AL, 0
		JGE peste_A
		
		; e negativ => verific daca e div cu 3
		neg AL
		mov AH, 0
		mov DL, 3
		div DL
		cmp AH, 0
		JNE peste_A
		
		; e negativ si div cu 3 => in D2
		
		mov AL, A[SI]
		mov D2[BX], AL
		inc BX
		
		peste_A:
			inc SI
	loop repeta_A
	
	mov CX, lenA
	mov SI, 0
	
	repeta_A_2:
	
		mov AL, A[SI]
		cmp AL, 0
		JL peste_A_2
			
			
		; verific daca e par
		mov AH, 0
		mov DL, 2
		div DL
		cmp AH, 0
		JNE peste_A_2
				
		; e pozitiv si par => in D1
				
		mov AL, A[SI]
		mov D1[DI], AL
		inc DI 
		
		peste_A_2:
			inc SI
	loop repeta_A_2
		
	
	mov SI, 0
	mov CX, lenB
	
	repeta_B:
		mov AL, B[SI]
		cmp AL, 0
		JGE peste_B
		
		; e negativ => verific daca e div cu 3
		neg AL
		mov AH, 0
		mov DL, 3
		div DL
		cmp AH, 0
		JNE peste_B
		
		; e negatic si div cu 3 => in D2
		
		mov AL, B[SI]
		mov D2[BX], AL
		inc BX
		
		
		peste_B:
			inc SI
	loop repeta_B
	
	
	mov CX, lenB
	mov SI, 0
	
	repeta_B_2:
	
		mov AL, B[SI]
		cmp AL, 0
		JL peste_B_2
			
			
		; verific daca e par
		mov AH, 0
		mov DL, 2
		div DL
		cmp AH, 0
		JNE peste_B_2
				
		; e pozitiv si par => in D1
				
		mov AL, B[SI]
		mov D1[DI], AL
		inc DI 
		
		peste_B_2:
			inc SI
	loop repeta_B_2
	
	
	
	; afisez fiecare sir 
	
	inc DI
	mov CX, DI 
	mov DI, 0 
	
	; Cod pentru a afișa un rând nou
		mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
		mov AH, 02h        
		int 21h            

		mov DL, 10         ; Line feed (cod ASCII 10, '\n')
		mov AH, 02h        
		int 21h 
	
	afisare_D1:
	
		stiva:
		 
			mov nr_cifre, 0
			din_cifre_pe_stiva_final:
				mov AL, D1[DI]
				mov AH, 0
				mov DX, 0
				mov CX, 10
				div CX
				mov D1[DI], AL
				push DX
				inc nr_cifre
				cmp AX, 0
				JNE din_cifre_pe_stiva_final
					
			
			de_pe_stiva_in_caractere_final:
				CMP nr_cifre, 0
				JE gata_D1
				pop DX
				add DL, '0'
				mov AH, 02h
				int 21h
				dec nr_cifre
				jmp de_pe_stiva_in_caractere_final
				
			gata_D1:
				inc DI
				mov DL, ','
				mov AH, 02h
				int 21h
	loop afisare_D1
	
	inc BX
	mov CX, BX
	mov BX, 0
	
	; Cod pentru a afișa un rând nou
	mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
	mov AH, 02h        
	int 21h            

	mov DL, 10         ; Line feed (cod ASCII 10, '\n')
	mov AH, 02h        
	int 21h   
	
	afisare_D2:
		stiva_D2:
		 
			mov nr_cifre, 0
			din_cifre_pe_stiva_final_D2:
				mov AL, D2[BX]
				cbw
				cwd
				mov CX, 10
				idiv CX
				mov D2[BX], AL
				push DX
				inc nr_cifre
				cmp AX, 0
				JNE din_cifre_pe_stiva_final_d2
					
			
			de_pe_stiva_in_caractere_final_D2:
				CMP nr_cifre, 0
				JE gata_D2
				pop DX
				add DL, '0'
				mov AH, 02h
				int 21h
				dec nr_cifre
				jmp de_pe_stiva_in_caractere_final_D2
				
			gata_D2:
				inc BX
				mov DL, ','
				mov AH, 02h
				int 21h
	loop afisare_D2

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start