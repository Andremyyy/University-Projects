;Sa dau doua sirurui de octeti A si B. 
;Sa se construiasca sirul D1 care sa contina 
;doar numerele impare si pozitive din A si B si 
;sirul D2 care sa contina numerele negative divizibile cu 5
; din sirurile A si B. Sa se afiseze pe ecran sirurile rezultat.
;Exemplu:
;A: 2, 1, -3, 3, -5, 2, 6
;B: 4, 5, 7, -15, 2, 1
;D1: 1, 3, 5, 7, 1
;D2: -5, -15


; !!! NU MERGE

assume cs:code,ds:data

; datele programului:

data segment

	A db 2, 1, -3, 3, -5, 2, 6
	lenA EQU $-A
	B db 4, 5, 7, -15, 2, 1
	lenB EQU $-B
	D1 db lenA+lenB dup (0)
	D2 db lenA+lenB dup (0)

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
		JGE pozitiv_A
		
		; e negativ => verific daca e div cu 5
		neg AL
		mov AH, 0
		mov DL, 5
		div DL
		cmp AH, 0
		JNE peste
		
		; e negativ si div cu 5 => in D2
		
		mov AL, A[SI]
		mov D2[BX], AL
		inc BX
		jmp peste_A
		
		pozitiv_A:
			; verific daca e impar
			mov AH, 0
			mov DL, 2
			div DL
			cmp AH, 1
			JNE peste_A
			
			; e pozitiv si negativ => in D1
			
			mov AL, A[SI]
			mov D1[DI], AL
			inc DI 
		
		peste_A:
			inc SI
	loop repeta_A
	
	mov SI, 0
	mov CX, lenB
	
	repeta_B:
		mov AL, B[SI]
		cmp AL, 0
		JGE pozitiv
		
		; e negativ => verific daca e div cu 5
		neg AL
		mov AH, 0
		mov DL, 5
		div DL
		cmp AH, 0
		JNE peste
		
		; e negatic si div cu 5 => in D2
		
		mov AL, B[SI]
		mov D2[BX], AL
		inc BX
		jmp peste
		
		pozitiv:
			; verific daca e impar
			mov AH, 0
			mov DL, 2
			div DL
			cmp AH, 1
			JNE peste
			
			; e pozitiv si negativ => in D1
			
			mov AL, B[SI]
			mov D1[DI], AL
			inc DI 
		
		peste:
			inc SI
	loop repeta_B
	
	
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
		mov DL, D1[DI]
		add DL, '0'
		mov AH, 02h
		int 21h
		inc DI
		mov DL, ','
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
		mov DL, D2[BX]
		add DL, '0'
		mov AH, 02h
		int 21h
		inc BX
		mov DL, ','
		int 21h
	loop afisare_D2

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
