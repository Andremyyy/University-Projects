; Se da un sir de octeti in segm de date.
; Sa se construiasca sirul d care sa contina diferenta elementelor consecutive din sirul S 
;si sa se afiseze acest sir pe ecran.
;Exemplu:
;S:4,2,5,3
;D:2,-3,2

assume cs:code,ds:data

; datele programului:

data segment

	S db 4,2,7,3
	lenS EQU $-S
	D db lenS dup (0)
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
	dec CX
	
	repeta:
		mov AL, S[SI]
		
		mov BL, S[SI+1]
		
		sub AL, BL
		
		mov D[DI], AL
		
		inc SI 
		inc DI 
		
	loop repeta
	
	; afisez sirul D 

	
	; Cod pentru a afișa un rând nou
	mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
	mov AH, 02h        
	int 21h            

	mov DL, 10         ; Line feed (cod ASCII 10, '\n')
	mov AH, 02h        
	int 21h   
	
	mov SI, 0
	mov CX, lenS
	dec CX
	mov nr_cifre, 0
	
	afisare_D:
	
		mov AL, D[SI]
		inc SI
		cmp AL, 0
		JGE pozitiv
		
		; e negativ => afisez '-' si il transform in pozitiv
		
		mov DL, '-'
		mov AH, 02h
		int 21h
		mov AL, D[SI-1]
		neg AL
		
		pozitiv:
			mov AH, 0
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
		
			
			mov DX, lenS
			dec DX
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