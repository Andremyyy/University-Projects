;1. Se da un sir de cuvinte s. 
;Sa se construiasca sirul de octeti d, 
;astfel incat d sa contina pentru fiecare pozitie din s:
;	- numarul de biti de 0, daca numarul este negativ
;	- numarul de biti de 1, daca numarul este pozitiv

;Exemplu:
;s: -22, 145, -48
;in binary: 
;1111111111101010, 10010001, 1111111111010000
;d: 3, 3, 5



assume cs:code,ds:data

data segment

s dw -22, 145, -48
len EQU ($-s)/2
D db len dup(0)

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov SI, 0
mov DI, 0
mov CX, len

repeta:
	mov AX, word ptr s[SI]
	
	mov BX, 0      ; contor biti 1
	mov DX, 16     

	; suma bitilor de 1
	numara_biti:
		test AX, 1     ; cel mai puțin semnificativ bit
		jz   urmator   
		inc BX         
	urmator:
		shr AX, 1  		; shift la dreapta pt a verifica toti bitii 
		dec DX
		jnz numara_biti
		
		
	mov AX, word ptr s[SI]
	test AX, 8000h            ; testez bitul semnului
	js negativ
	jns pozitiv
	negativ:
        mov DX, 16          
        sub DX, BX          ; 16 - nrBitiDe1 = nr biti de 0
        jmp save
    pozitiv:
		mov DX, BX         ; bx = nr de biti de 1
		
	save: 
		mov d[DI], DL
		inc DI
		inc SI
loop repeta

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start