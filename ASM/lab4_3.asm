; 3. Se da un sir de litere mari si mici. 
;Sa se afiseze literele mici pe ecran si 
;sa se afiseze numarul acestor litere pe ecran.

assume cs:code,ds:data

; datele programului:

data segment

	sir db 'ABDHVUBE'
	len EQU $-sir
	nr db 0              ; numarul de litere mici 

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov SI, 0
	mov CX, len
	
	repeta:
	
		mov BL, sir[SI]
		CMP BL, 'a'
		JL peste
		
		; este litera mica
		
		; maresc numarul
		inc nr
		
		; afisez caracterul
		mov DL, BL
		mov AH, 02h
		int 21h
		
		;afisez ' '
		mov DL, ' '
		mov AH, 02h
		int 21h
		
		peste:
			inc SI
	
	
	loop repeta
	
	
	; Cod pentru a afișa un rând nou
	mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
	mov AH, 02h        
	int 21h            

	mov DL, 10         ; Line feed (cod ASCII 10, '\n')
	mov AH, 02h        
	int 21h            
	
	
	; afisez nr de litere mici
	add nr, '0'
	mov DL, nr
	mov AH, 02h
	int 21h


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start