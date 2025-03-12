;14. Se da un sir de dublucuvinte. 
;Sa se determine si sa se salveze in sirul D 
;toti octetii care au numar impar de biti in 
;reprezentarea binara.

assume cs:code,ds:data

data segment

s dd 11, 10, -3, 523, 4, 14315
len EQU ($-s)/4
D db len*4 dup(0)   

data ends

;11 (decimal) = 00000000 00000000 00000000 00001011 (binar) = 0B 00 00 00 (hexa little-endian) 
;10 (decimal) = 00000000 00000000 00000000 00001010 (binar) = 0A 00 00 00 (hexa little-endian)
;-3 (decimal) = 11111111 11111111 11111111 11111101 (binar) = FD FF FF FF (hexa little-endian)
;523 (decimal) = 00000000 00000000 00000010 00001011 (binar) = 0B 02 00 00 (hexa little-endian)
;4  (decimal) = 00000000 00000000 00000000 00000100 (binar) = 04 00 00 00 (hexa little-endian)
;14315 (decimal) = 00000000 00000000 00110111 11001011 (binar) = CB 37 00 00 (hexa little-endian)

; (REZULTATUL IN ) D = 0B FD 0B 02 04 CB 



;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov SI, 0	  ; index pt parcurgerea sirului S
mov DI, 0     ; index pt parcurgerea sirului D
mov CX, len*4   ;contor pt loop (len*4 pentru ca verific fiecare octet din fiecare dublucuvint)

repeta:
	mov AL, byte ptr s[SI]
	
	mov BX, 0    ; contor pt calcularea nr de biti de 1 din octetul de pe pozitia s[SI]
	mov DX, 8  

	; suma bitilor de 1
	numara_biti:
		test AL, 1     ; cel mai puțin semnificativ bit
		jz   urmator   
		inc BX         
	urmator:
		shr AL, 1  		; shift la dreapta pt a verifica toti bitii 
		dec DX
		jnz numara_biti
		
	test BX, 1 			; verific daca nr de biti este impar
	jz nu_e_impar
	
	mov AL, byte ptr s[SI]
	mov D[DI], AL
	inc DI
	
	nu_e_impar:
		inc SI
	
loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start