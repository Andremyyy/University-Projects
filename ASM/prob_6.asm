;Sa se citeasca un sir de caractere 
;si sa se afiseze cate spatii sunt in sir.
;Exemplu:
;S: "ana are mere"
;rezultat: 2

assume cs:code,ds:data

data segment

	S dd 20, ? , 20 dup (?)
	rezultat db 0
	nr_cifre dw 10

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
	
	mov CL, byte ptr S[1]   ; lungime sir
	mov CH, 0
	add CX, 2               ; pr compararea cu SI din bucle
	mov SI, 2               ; primul caracter
	
	calcul:
		
		mov BL, byte ptr S[SI]
		CMP BL, ' ' 
		jne peste
		
		mov AL, rezultat
		inc AL
		mov rezultat, AL
		
		peste:
			inc SI
	loop calcul
	
	
	stiva:
		; Cod pentru a afișa un rând nou
		mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
		mov AH, 02h        
		int 21h            

		mov DL, 10         ; Line feed (cod ASCII 10, '\n')
		mov AH, 02h        
		int 21h  
		
		mov nr_cifre, 0
		din_cifre_pe_stiva_final:
			mov AL, rezultat
			mov AH, 0
			mov DX, 0
			mov CX, 10
			div CX
			mov rezultat, AL
			push DX
			inc nr_cifre
			cmp AX, 0
			JNE din_cifre_pe_stiva_final
				
				
		mov CX, nr_cifre
		
		de_pe_stiva_in_caractere_final:
			pop DX
			add DL, '0'
			mov AH, 02h
			int 21h
		loop de_pe_stiva_in_caractere_final	
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
