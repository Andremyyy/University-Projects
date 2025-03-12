;9. Se da un sir de litere mari si mici. 
;Sa se afiseze literele mari pe ecran si sa se afiseze numarul acestor litere pe ecran.

assume cs:code,ds:data

; datele programului:

data segment

	sir db 'AvcbdDGSVEvDtIbFyBcYTnbJ'
	len EQU $-sir
	mesaj_numar db 'Numarul literor mari este de : $'
	numar dw 0
	zece dw 10
	nr_cifre dw 0
	
data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov CX, len
	mov SI, 0
	
	
    repeta:
		mov Al, sir[SI]
		cmp AL, 'A'   
		jl peste       ; < 'A' = > peste
		cmp AL, 'Z'   
		jg peste       ; > 'Z' = > peste
		
		; este litera mare daca 'A' <= litera <= 'Z'
		
		mov DL, AL
		mov AH, 02h
		int 21h
		
		inc numar
		
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

	;mesaj
	mov AH, 09H
	mov DX, offset mesaj_numar
	int 21h
	
	
	
	; transfmor numarul din cifre in caractere
	
	transformare:
		mov AX, numar
		mov DX, 0
		div zece		; ax - cat, dx - rest
		mov numar, AX   ; salvez catul 
		push DX			; pun restul pe stiva
		inc nr_cifre
		cmp AX, 0
		JNE transformare
	
	mov CX, nr_cifre
	
	afisare_numar:
		
		pop DX
		add DL, '0'
		mov AH, 02h
		int 21h
	loop afisare_numar
   

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start