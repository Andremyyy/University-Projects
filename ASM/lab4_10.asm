;10. Se citeste un sir de caractere de la tastatura. 
;Se da un constanta K reprezentand o litera. 
;Sa se determine numarul de aparitii a lui K in sirul citit. 
;Sa se afiseze acest numar pe ecran.



ASSUME cs:code, ds:data

data SEGMENT
    sir db 25, ?, 25 dup(?) 	; Șirul citit
    k db 'A'                	; Litera căutată
    nr dw 0                 	; Număr de apariții
    nrcifre dw 0            	; Numărul de cifre pentru afișare
data ENDS

code SEGMENT

afisare proc
    mov nrcifre, 0
    mov ax, nr             
	repeta:
		mov DX, 0
		mov bX, 10
		div bx                 ; Împărțim ax:dx la 10
		push dx                ; Stocăm restul (o cifră) pe stivă
		inc nrcifre            ; Incrementăm numărul de cifre
		cmp ax, 0
		jne repeta             ; Continuăm dacă ax nu este 0
		
	mov cx, nrcifre        	   ; Pregătim să iterăm cifrele
	
	caracter:
		pop dx                 ; Recuperăm o cifră din stivă
		add dl, '0'            ; Convertim cifra în ASCII
		mov ah, 02h
		int 21h                ; Afișăm cifra
	loop caracter          	   ; Repetăm pentru toate cifrele
	
	ret
	
afisare endp

start:
    mov ax, data
    mov ds, ax

    ; Citire șir
    mov ah, 0Ah
    mov dx, offset sir
    int 21h

    ; Linie nouă după citire
    mov dl, 0Dh
    mov ah, 02h
    int 21h
    mov dl, 0Ah
    int 21h

    ; Lungimea șirului
    mov cl, byte ptr sir[1]
    mov ch, 0

    ; Procesare șir
    mov si, 2              ; Pointerul în șir (după lungime)
    mov word ptr nr, 0     ; Resetăm contorul

procesare:
    cmp cl, 0              
    je sfarsit
	
    mov al, byte ptr sir[si]
	
    cmp al, 0Dh            ; Ignorăm ENTER
    je urmatorul
	
    cmp al, k              ; Comparăm cu litera
    jne urmatorul
	
	; este litera din k
    inc word ptr nr        ; Incrementăm contorul

	urmatorul:
		inc si
		dec cl
		jmp procesare

	sfarsit:
		call afisare           ; Afișăm rezultatul
		mov ax, 4C00h
		int 21h

code ENDS
END start
