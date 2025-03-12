;Se da un sir de octeti S. 
;Sa se afiseze pe ecran suma lor in baza 16.
;Exemplu:
;S: 1, 2, 3, 4
;rezultat: A



assume cs:code,ds:data

; datele programului:

data segment

	sir db 1,2,3,4,10,7
	len EQU $-sir
	suma dw 0
	; suma = 27 (10) = 1B(16)
	contor dw 0

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	
	mov SI, 0
	mov CX, len
	
	mov AL, sir[SI]
	cbw
	mov suma, AX
	inc SI 
	dec CX
	
	repeta:
		mov AL, sir[SI]
		cbw
		add suma, AX
		inc SI
	loop repeta
	
	transformare_baza_16:
		mov AX, suma
		cwd
		mov BX, 16
		idiv BX         ; AX - cat, DX - rest
		mov suma, AX
		push DX
		inc contor
		cmp AX, 0
		JNE transformare_baza_16
		
	;dec contor
	mov CX, contor
	afisare:
		pop DX
		cmp DX, 10
		JGE altfel
		
		add DL, '0'
		mov AH, 02h
		int 21h
		
		altfel:
			cmp DX, 10
			jg peste_11
			
			mov DL, 'A'
			mov AH, 02h
			int 21h
			
			peste_11:
				cmp DX, 11
				jg peste_12
				
				mov DL, 'B'
				mov AH, 02h
				int 21h
				
				peste_12:
					cmp DX, 12
					jg peste_13
					
					mov DL, 'C'
					mov AH, 02h
					int 21h
					
					peste_13:
						cmp DX, 13
						jg peste_14
						
						mov DL, 'D'
						mov AH, 02h
						int 21h
						
						peste_14:
							cmp DX, 14
							jg peste_15
							
							mov DL, 'E'
							mov AH, 02h
							int 21h
							
							peste_15:
								cmp DX, 15
								jg peste
								mov DL, 'F'
								mov AH, 02h
								int 21h
								
		peste:
	loop afisare
			
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
