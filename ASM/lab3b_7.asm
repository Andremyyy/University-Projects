;7. Dandu-se un sir de dublucuvinte, 
;sa se obtina un alt sir de dublucuvinte 
;in care se vor pastra doar dublucuvintele 
;din primul sir care au un numar par de biti cu valoare 1.


; ! nu stiu daca e 100% corect

assume cs:code,ds:data

data segment

s dw -22, 145, -48, 35, 78
len EQU $-s
D db len dup(0)
contor db 0


data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov SI, 0
mov DI, 0

repeta:
	mov AX, word ptr s[SI]
	mov DX, word ptr s[SI+2]
	
	mov BX, 0      ; contor biti 1
	mov CX, 16     

	; suma bitilor de 1
	numara_biti_AX:
		test AX, 1     ; cel mai puțin semnificativ bit
		jz   urmator_AX   
		inc BX         
		urmator_AX:
			shr AX, 1  		; shift la dreapta pt a verifica toti bitii 
	loop numara_biti_AX
			
	mov CX, 16
	numara_bitii_DX:
		test DX, 1     ; cel mai puțin semnificativ bit
		jz   urmator_DX   
		inc BX         
		urmator_DX:
			shr DX, 1  		; shift la dreapta pt a verifica toti bitii 
	loop numara_bitii_DX
		
		
	
	mov AX, BX
	mov CL, 2
	div CL
	cmp AH, 0
	JNE peste
	
	; nr par de biti -> pun in sirul D dublucuvantul
	
	mov AX, word ptr s[SI]
	mov DX, word ptr s[SI+2]
	
	mov word ptr D[DI], AX
	mov word ptr D[DI+2], DX
	add DI, 4
	
	peste:
		add SI, 4
		inc contor
	
	mov AL, contor
	cmp AL, len/4
	jne repeta

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start