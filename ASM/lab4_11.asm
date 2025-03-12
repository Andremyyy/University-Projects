;11. Se citeste de la tastatura o litera L. 
;Se da un sir de caractere in data segment.
;Sa se inlocuiasca fiecare aparatie a lui L in sirul din data segment cu litera X. 
;Sa se afiseze acest sir nou rezultat pe ecran.



assume cs:code,ds:data

; datele programului:

data segment

	litera db ?
	sir db 'AvcbdDASAAvDt'
	len EQU $-sir
	X db 'X'
	mesaj_litera db 'Dati o litera de la tastatura: $'
	mesaj_sir_nou db 'Noul sir este : $'
	sir_nou db len+1 dup(?)                                 ; + 1 pentru terminator de sir '$'
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	; afisez primul mesaj
	mov AH, 09h
	mov DX, offset mesaj_litera
	int 21h

	; citesc litera 
	mov AH, 01h
	int 21h
	mov litera, AL 
	
	; parcurg sirul si inlocuiesc toate caracterele 'litera' cu caracterul X = 'X'
	
	mov CX, len
	mov SI, 0
	mov DI, 0
	
	repeta:
	
		mov AL, sir[SI]
		cmp AL, litera
		JNE nemodificat
		
		; salvez in sir_nou litera X
		mov BL, X
		mov sir_nou[DI], BL
		JMP incrementari
		
		nemodificat:
			; salvez in sir_nou caracterul de pe sir[SI]
			mov AL, sir[SI]
			mov sir_nou[DI], AL
			
		incrementari:
			inc SI
			inc DI
	
	loop repeta
	
	; Adaug terminator de linie
    mov byte ptr sir_nou[DI], '$'  
	
	
	; Cod pentru a afișa un rând nou
	mov DL, 13         ; Carriage return (cod ASCII 13, '\r')
	mov AH, 02h        
	int 21h            

	mov DL, 10         ; Line feed (cod ASCII 10, '\n')
	mov AH, 02h        
	int 21h 
	
	; afisez al doilea mesaj
	
	mov AH, 09h
	mov DX, offset mesaj_sir_nou
	int 21h
	
	; afisez noul sir
	
	mov AH, 09H
	mov DX, offset sir_nou
	int 21h
	

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start