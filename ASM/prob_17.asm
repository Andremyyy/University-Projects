;Sa se citeasca de la tastatura un sir de caractere S
;si sa se inlocuiasca toate cifrele cu simbolul '%'. 
;Sa se afiseze sirul rezultat pe ecran.
;Exemplu:
;S: "Ana are 3 mere si 4 pere."
;rezultat: "Ana are % mere si % pere."

assume cs:code,ds:data

data segment

	S dd 100, ? , 100 dup (?)
	procent db '%'

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
	
	
	mov CL, byte ptr S[1]   ; lungime sir
	mov CH, 0
	add CX, 2               ; pr compararea cu SI din bucle
	mov SI, 2               ; primul caracter
	
	calcul:
		
		mov BL, byte ptr S[SI]
		CMP BL, '0'
		JL peste
		
		cmp BL, '9'
		JG peste
		
		; este cifra => o inlocuiesc cu '%'
		
		mov BL, procent
		mov byte ptr S[SI], BL
		
		peste:
			inc SI
	loop calcul
	
	mov BL, '$'
	mov byte ptr S[SI], BL
	mov DX, offset S
	mov AH, 09h
	int 21h
	
;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start

