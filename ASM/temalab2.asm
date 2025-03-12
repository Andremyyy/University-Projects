;CERINTA:

;2. Se dau doua cuvinte A si B. Sa se obtina cuvântul C:

;	- bitii 0-2 si bitul 10 ai lui C au valoarea 0
;	- bitii 3-6 ai lui C coincid cu bitii 5-8 ai lui A
;	- bitii 7-9 ai lui C coincid cu bitii 0-2 ai lui B
;	- bitii 11-15 ai lui C coincid cu bitii 5-9 ai lui B


; SCHITA:

	; a = a0a1a2a3a4a5a6a7a8a9a10a11a12a13a14a15
	; b = b0b1b2b3b4b5b6b7b8b9b10b11b12b13b14b15
;		=>	
	; c = 0 0 0 a5a6a7a8b0b1b2 0 b5 b6 b7 b8 b9



; EXEMPLE:

; 1. 

;	a = a0a1a2a3a4a5a6a7a8a9a10a11a12a13a14a15
;	  = 1 1 0 1 1 0 1 0 1 0 1  0  1  0  1  0 (binar) = DAAA (hex)
;
;	b =	b0b1b2b3b4b5b6b7b8b9b10b11b12b13b14b15
;	  = 1 0 1 0 1 1 0 0 1 1 0  0  1  1  0  0 (binar) = ACCC (hex)
;
;		=> a5a6a7a8 = 0101, 
;	   		b0b1b2 = 101, 
;	   		b5b6b7b8b9 = 10011.
; 	DECI,  
;		c = 0 0 0 a5a6a7a8b0b1b2 0 b5 b6 b7 b8 b9
;		  = 0 0 0 0 1 0 1 1 0 1  0 1  0  0  1  1   (binar)
;		  = B53 (hex)


; 2.

;	a = a0a1a2a3a4a5a6a7a8a9a10a11a12a13a14a15
;	  = 0 0 1 1 1 1 0 0 0 1 0  0  1  1  1  1 (binar) = 3C4F  (hex)
;
;	b =	b0b1b2b3b4b5b6b7b8b9b10b11b12b13b14b15
;	  = 0 1 1 1 1 0 1 0 0 0 0  1  1  1  0  1 (binar) = 7A1D  (hex)
;		
;		=> a5a6a7a8 = 1000, 
;	   		b0b1b2 = 011, 
;	   		b5b6b7b8b9 = 01000.
; 	DECI,  
;		c = 0 0 0 a5a6a7a8b0b1b2 0 b5 b6 b7 b8 b9
;		  = 0 0 0 1 0 0 0 0 1 1  0 0  1  0  0  0   (binar)
;		  = 10C8 (hex)
 
 
 
assume cs:code,ds:data

; datele programului:

data segment

a dw 0011110001001111b
b dw 0111101000011101b
c dw 0       ; rezultatul cerut

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov AX, a
shl AX, 2		; AX = a2a3a4a5a6a7a8a9a10a11a12a13a14a1500
and AX, 0001111000000000b    ; AX = 000a5a6a7a8000000000

mov BX, AX

mov AX, b
shr AX, 7       ;AX = 0000000b0b1b2b3b4b5b6b7b8
and AX, 0000000111000000b    ; AX = 0000000b0b1b2000000

or BX, AX        ; BX = 000a5a6a7a8b0b1b2000000


mov AX, b
shr AX,6		; AX = 000000b0b1b2b3b4b5b6b7b8b9
AND AX, 0000000000011111b     ; AX = 00000000000b5b6b7b8b9


or BX,AX       ; BX = 0 0 0 a5a6a7a8b0b1b2 0 b5 b6 b7 b8 b9

mov c,BX       ; c = rezultat = 0 0 0 a5a6a7a8b0b1b2 0 b5 b6 b7 b8 b9



;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start