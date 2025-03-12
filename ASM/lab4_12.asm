;12. Dandu-se un sir de cuvinte in data segment 
;sa se tipareasca pe ecran suma octetilor superiori 
;din cuvintele acestui sir.

;  1234h, 1A2Bh, 5678h, -2h (= FFFEh)
; in memorie:
; 34  12  2B  1A  78  56  FE FF
; -----------------------------
;  0  1   2    3   4   5  6  7
; octetii superiori sunt cei de pe pozitile impare!!!!

assume cs:code,ds:data

; datele programului:

data segment

	sir dw 1234h, 1A2Bh, 5678h, -2h
	len EQU $-sir
	suma dw 0
	nrcifre dw 0
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0
	mov CX, len/2
	
	repeta:
	
		mov AL, byte ptr sir[SI+1]
		cbw
		add suma, AX
		add SI, 2
	
	loop repeta
	
	transforma_numar_in_caractere:
		mov BX, suma  ; copie
		calc_nr_cifre:
			mov AX, BX
			mov DX, 0
			mov CX, 10
			idiv CX      ; AX - cat, DX - rest
			mov BX, AX
			push DX
			inc nrcifre
			CMP AX, 0
			JNE calc_nr_cifre
			
	afiseaza_numarul:
		mov CX, nrcifre
		afiseaza:
			pop DX
			add DL, '0'
			mov AH, 02h
			int 21h
		loop afiseaza
		
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start