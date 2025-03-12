;4. Se da un sir A de dublucuvinte. Construiti doua siruri de octeti  
;- B1: contine ca elemente partea superioara a cuvintelor superioare din A
;- B2: contine ca elemente partea inferioara a cuvintelor inferioare din A 

assume cs:code,ds:data

; datele programului:

data segment

	A dd 12345678h, 1A2B3C4Dh, 122B3C4Dh, 2E2B3C4Dh , 18345678h 
	lenA EQU $-A
	B1 db lenA/4 dup(0)
	B2 db lenA/4 dup(0)
	
	; in MEMORIE:

; 78 56 34 12 4D 3C 2B 1A 4D 3C 2B 12 4D 3C 2B 2E 78 56 34 18 
; ==       -- ==       -- ==       -- ==       -- ==       -- 

	; octetii -- sunt partea superioara a cuvintelor superioare din A
	; octetii == sunt partea inferioara a cuvintelor inferioare din A


	; deci => 
	; B1 = 12h, 1Ah, 12h, 2Eh, 18h
	; B2 = 78h, 4Dh, 4Dh, 4Dh, 78h
	

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov CX, lenA/4   				
	mov SI, 3						; pt A
	mov DI, 0       				; pt B1
	mov BX, 0						; pt B2

	repeta_B1:
		
		
		mov AL, byte ptr A[SI]
		
		mov B1[DI], AL
		inc DI 
		add SI, 4
			
	loop repeta_B1
	
	
	mov CX, lenA/4
	mov SI, 0
	repeta_B2:
		mov AL, byte ptr A[SI]
		mov B2[BX], AL
		inc BX 
		add SI, 4
	loop repeta_B2


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start

