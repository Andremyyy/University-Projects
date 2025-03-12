;6.  Sa se citeasca un sir de cifre a. 
; Sa se salveze in sirul b doar cifrele pare. 
; Sa se afiseze sirul b pe ecran.

assume cs:code,ds:data

; datele programului:

data segment

	a db 20, ?, 20 dup (?)
	b db 20 dup (?)
	doi db 2

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; CITIRE SIR a
	mov AH, 0Ah
	mov DX, offset a
	int 21h
	
	
	lea SI, a + 2             ; adresa primului caracter din a
    mov CL, [a + 1]           ; lungimea sirului a
    lea DI, b                 ; adresa primului caracter din b
	
	
	repeta:
		mov AL, [SI]
		sub AL, '0'
		cbw
		idiv doi		; al - cat, ah - rest
		cmp AH, 0
		jne peste
		
		; este par
		
		mov AL, [SI]
		mov [DI], AL
		inc DI
		
		peste:
			inc SI
	loop repeta
	
	mov byte ptr [DI], '$'
	
	
	; Cod pentru a afișa un rând nou
	mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
	mov AH, 02h        
	int 21h            

	mov DL, 10         ; Line feed (cod ASCII 10, '\n')
	mov AH, 02h        
	int 21h   
	
	; AFISAREA SIRULUI b 
	mov AH, 09h
	mov DX, offset b
	int 21h


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start