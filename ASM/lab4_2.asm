;2. 
;Sa se citeasca cate un caracter de la tastatura, fara ecou. 
;Daca este cifra, sa se tipareasca pe ecran, 
;daca este caracterul '$', se termina programul, 
;in orice alta situatie se adauga caracterul intr-un buffer care se va tipari in final pe ecran.


assume cs:code,ds:data

data segment

buffer db 100 DUP('$')   ; buffer de 100 octeti
lenb dw 0


data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX


; operatiile programului:

repeta:
	mov AH, 08h
	int 21h
	; caracterul citit este in AL (reprezentare in codul ASCII)
	CMP AL, '$'   ; '$' in ASCII = 36 
	JE sfarsit
	
	
	; daca am ajuns aici => ori este cifra, ori este altceva 
		
	; verific daca este cifra ( >= '0' si <= '9')
		
	cmp AL, '0'
	JL adauga_buffer    ; daca este < '0' adaug in buffer
	CMP AL, '9'
	JG adauga_buffer    ; daca este > '9' adaug in buffer
		
	; daca am ajuns pana aici clar este cifra
	; => afisez cifra
		
	mov DL, AL
	mov AH, 02h
	int 21h
		
	JMP repeta
		
		
adauga_buffer:

	mov bx, word ptr lenb
    cmp bx, 99             ; verific daca am umplut buffer-ul
    jge sfarsit            
    mov si, bx
    mov byte ptr [buffer + si], AL ; mut ce caracter este in AL in buffer pe pozitia buffer+SI  
    inc word ptr lenb              
    jmp repeta

		

sfarsit:
	; afisez carcaterele din buffer
	; intai adaug '$' la buffer pt a-l putea tipari
	mov bx, word ptr lenb
    mov si, bx
    mov byte ptr [buffer + si], '$'  ; adaug la sfarsitul buffer-ului '$'
	inc word ptr lenb
	
	mov AH, 09h    ; functie pt afisarea unui sir de caractere 
	mov DX, offset buffer
	int 21h
	
	;terminarea programului
	mov ah, 4ch       
	int 21h

code ends

end start