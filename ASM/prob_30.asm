;Se dau A si B de tip byte, C word si D doubleword. 
;Sa se calculeze expresia: C+(A*B-D+3)/(B*B-C) 
;si sa se afiseze rezultatul pe ecran.
;Exemplu:
;A = 12
;B = 104
;C = 12325
;D = 75412
;rezultat: 12374



;C+(A*B-D+3)/(B*B-C)
;
; 1. A*B
; 2. B*B
; 3. B*B-C 
; 4. A*B-D+3
; 5. (A*B-D+3)/(B*B-C)
; 6. C+(A*B-D+3)/(B*B-C)

assume cs:code,ds:data

; datele programului:


data segment

	A db 12
	B db 104
	C dw 12325
	D dd 75412
	rez dw 0
	mesaj_eroare db 'Impartitorul este 0!'

suma dw 0

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	

	mov AL, A     
	mov BL, B
	imul BL
	
	mov DX, AX   ; DX = A * B 
	
	mov AL, B
	mov BL, B 
	imul BL 
	
	sub AX, C   ; AX = B * B - C
	JZ divide_by_zero
	
	mov SI, AX   ; SI = B*B-C 
	
	mov AX, DX         ; AX = A * B
    mov DX, word ptr D ; DX = partea inferioară a lui D
    sub AX, DX         ; AX = A * B - D_low
    sbb DX, word ptr D[2] ; DX = partea superioară a lui D   SBB - scadere cu imprimut
    add AX, 3          ; AX = A * B - D + 3
    cwd                
	
	mov CX, SI 
	idiv CX 
	mov BX, AX
	
	mov AX, C 
	add AX, BX 
	
	mov rez, AX
	
	
	afisare_stiva_C_baza_10:
		mov BX, 0   ; nr_cifre
		pe_stiva:
			mov AX, rez
			mov DX, 0
			mov CX, 10
			div CX 
			
			inc BX
			;catul
			mov rez, AX
			
			; restul merge pe stiva
			push DX
			
			cmp AX, 0
			JNE pe_stiva
			
		mov CX, BX
		din_stiva:
			pop DX
			add DL, '0'
			mov AH, 02h
			int 21h
		loop din_stiva
		
	jmp final
		
	divide_by_zero:
		mov DX, offset mesaj_eroare
		mov AH, 09h
		int 21h
		
	final:

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start