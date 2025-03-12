;Se da un sir de octeti S in segmentul de date. 
;Sa se afiseze pe ecran suma lor in baza 2.
;Exemplu:
;S: 1, 2, 3, 4
;rezultat: 1010

assume cs:code,ds:data

; datele programului:

data segment

	sir db 1,2,3,4,5
	len EQU $-sir
	suma dw 0
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
	
	repeta:
		mov AL, sir[SI]
		cbw
		add suma, AX
		inc SI
	loop repeta
	
	transformare_baza_2:
		mov AX, suma
		cwd
		mov BX, 2
		idiv BX         ; AX - cat, DX - rest
		mov suma, AX
		push DX
		inc contor
		cmp AX, 0
		JNE transformare_baza_2
		
	dec contor
	mov CX, contor
	afisare:
		pop DX
		add DL, '0'
		mov AH, 02h
		int 21h
	loop afisare
			
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start