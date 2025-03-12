;13.Se da un sir de dublucuvinte. 
;Sa se determine si sa se salveze in sirul D 
;toti octetii care au numarul de biti din reprezentarea binara 
;mai mic decat o valoare k (declarata in segmentul de date).

assume cs:code,ds:data

data segment

s dd 12345678h, 98765432h, 11101213h
len EQU ($-s)/4
D db len dup(0)
k dw 4

; d = 34h, 12h, 32h, 54h, 98h, 13h, 12h, 10h, 11h

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov SI, 0
mov DI, 0
mov CX, len*4

repeta:
	mov AL, byte ptr s[SI]
	
	mov BX, 0      ; contor biti 1
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
		
	
	
	mov AL, byte ptr s[SI]
	
	CMP BX, k
	JAE peste
	
	
	mov d[DI], AL
	inc DI
	
	peste:
		inc SI
loop repeta

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start