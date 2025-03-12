;Sa se citeasca un sir de caractere 
;si un caracter de la tastatura si 
;sa se afiseze pe ecran daca caracterul apare in sir.
;Exemplu:
;S: "ana are mere"
;C: 'a'
;rezultat: "DA"


assume cs:code,ds:data

data segment

	S dd 100, ? , 100 dup (?)
	caracter db ?
	rezultat db 0
	mesaj_afirmativ db 'DA$'
	mesaj_negativ db 'NU$'

data ends


;codul:

code segment
start:

	mov AX, data
	mov DS, AX

; operatiile programului:

	;citire sir
	mov AH, 0Ah
	mov DX, offset S 
	int 21h
	
	; Cod pentru a afișa un rând nou
		mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
		mov AH, 02h        
		int 21h            

		mov DL, 10         ; Line feed (cod ASCII 10, '\n')
		mov AH, 02h        
		int 21h 
	
	; citire caracter 
	mov AH, 01h
	int 21h
	
	mov caracter, AL
	
	
	mov CL, byte ptr S[1]   ; lungime sir
	mov CH, 0
	add CX, 2               ; pr compararea cu SI din bucle
	mov SI, 2               ; primul caracter
	
	calcul:
		
		mov BL, byte ptr S[SI]
		CMP BL, caracter
		JNE peste
		
		
		mov rezultat, 1
		
		peste:
			inc SI
	loop calcul
	
	; Cod pentru a afișa un rând nou
		mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
		mov AH, 02h        
		int 21h            

		mov DL, 10         ; Line feed (cod ASCII 10, '\n')
		mov AH, 02h        
		int 21h 
	
	
	cmp rezultat, 0
	JE nu_apare
	
	
	; apare
	mov DX, offset mesaj_afirmativ
	mov AH, 09h
	int 21h
	jmp final
	
	nu_apare:
		; NU apare
		mov DX, offset mesaj_negativ
		mov AH, 09h
		int 21h

	final:
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start


