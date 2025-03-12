;13. Se citeste de la tastatura un numar. 
;Sa se afiseze acest numar decrementat cu 1.

assume cs:code,ds:data

; datele programului:

data segment

	zonaCitire db 20, ?, 20 dup (?)
	zece dw 10
	mesaj db 'Numarul decrementat: $'
	numar dw 0
	nrcifre dw 0
	minus db 0
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; CITIRE numar
	mov AH, 0Ah
	mov DX, offset zonaCitire
	int 21h
	
	mov SI, offset zonaCitire + 2  ; zonaCitire + 2 contine primul caracter
	
	; afisez mesaj:
    mov AH, 09h       
    mov DX, offset mesaj     ; mesajul "Numarul decrementat: "
    int 21h

    convert_to_number:
		mov BL, [SI]
		
		cmp BL, 0Dh       ; verificam daca am ajuns la Enter 
		je end_conversion 
		
		cmp BL, '-'
		jne peste

		; e negativ 
		
		; afisez '-'
		mov DL, '-'
		mov AH, 02h
		int 21h
		mov minus, 1
		
		jmp sfarsit
		
		peste:
			sub BL, '0'
			mov AL, BL
			cbw
			mov BX, AX
			mov AX, numar
			mul zece
			add AX, BX
			mov numar, AX
			
		sfarsit:
			inc SI
			
		JMP convert_to_number
	
	end_conversion:
		cmp minus, 0
		jne nr_negativ
		
		; e pozitiv, deci scad 1
		mov AX, numar
		sub AX, 1
		mov numar, AX
		jmp transforma_numar_in_caractere
		
		nr_negativ:
			; e negativ, deci adaug 1
			mov AX, numar
			add AX, 1
			mov numar, AX
		
	
		
	transforma_numar_in_caractere:
		mov BX, numar  ; copie
		calc_nr_cifre:
			mov AX, BX
			mov DX, 0
			idiv zece      ; AX - cat, DX - rest
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