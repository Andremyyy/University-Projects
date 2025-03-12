;Sa se citeasca de la tastatura un sir de octeti S si sa se afiseze pe ecran diferenta lor.
;Exemplu:
;S: 12, 3, 4, 6
;Diferenta: -1
 

assume cs:code,ds:data

data segment

	S db 20, ? , 20 dup (?)
	diferenta db 0
	numar_curent db 0
	zece db 10

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
	
	mov numar_curent, 0
	
	primul_numar:
		cmp SI, CX 
		JGE peste
		
		mov BL, byte ptr S[SI]
		CMP BL, ' ' 
		je peste
		
		sub BL, '0'
		mov AL, numar_curent
		mul zece
		mov AH, 0
		add AL, BL
		mov numar_curent, AL
		inc SI
		jmp primul_numar
		
	peste:
		mov BL, numar_curent
		mov diferenta, BL
		mov numar_curent, 0
		inc SI
	
	transf_caract_in_cifre:
		cmp SI, CX 
		JGE finalizeaza_diferenta
		
		mov BL, byte ptr S[SI]
		cmp BL, ' '     ; compar cu spatiu
		je finalizeaza_numar
		
		sub BL, '0'
		mov AL, numar_curent
		mul zece
		mov AH, 0
		add AL, BL
		mov numar_curent, AL
		inc SI 
		JMP transf_caract_in_cifre
		
		
		finalizeaza_numar:
			mov BL, numar_curent
			sub diferenta, BL
			mov numar_curent, 0
			inc SI
			jmp transf_caract_in_cifre
			
		finalizeaza_diferenta:
			; dacă ultimul număr nu a fost procesat din cauza lipsei spațiului
			cmp numar_curent, 0
			je afisare_diferenta
			mov BL, numar_curent
			sub diferenta, BL
		
			
	afisare_diferenta:
		; Cod pentru a afișa un rând nou
		mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
		mov AH, 02h        
		int 21h            

		mov DL, 10         ; Line feed (cod ASCII 10, '\n')
		mov AH, 02h        
		int 21h   
		
		
		
		mov CX, 0  ; nr cifre diferenta
		
		mov AL, diferenta
		cmp AL, 0
		JGE transf_cifre_in_caract
		
		; e negativ => afisez '-' si transform in nr pozitiv
		mov AH, 02h
		mov DL, '-'
		int 21h
		mov AL, diferenta
		neg AL
		
		transf_cifre_in_caract:
		
			mov AH, 0
			mov DX, 0
			mov BX, 10
			div BX      ; ax - cat, dx - rest
			push DX
			inc CX
			cmp AX, 0
			JNE transf_cifre_in_caract
			
		
			
		afisare_cifre:
			pop DX 
			mov DH, 0
			add DL, '0'
			mov AH, 02h
			int 21h
		loop afisare_cifre

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
