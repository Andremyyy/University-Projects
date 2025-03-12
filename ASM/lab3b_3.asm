;3. Se da un sir A de cuvinte. Construiti doua siruri de octeti  
; - B1: contine ca elemente partea superioara a cuvintelor din A
; - B2: contine ca elemente partea inferioara a cuvintelor din A 

assume cs:code,ds:data

; datele programului:

data segment

	A dw 1234h, 1A2Bh, 3C4Dh , 5678h, 302Bh
	lenA EQU $-A
	B1 db lenA/2 dup(0)
	B2 db lenA/2 dup(0)
	doi db 2
	
	; in MEMORIE:

	;  34 12 2B 1A 4D 3C 78 56 2B 30
	;     --    --    --    --    --

	; octetii -- sunt partea superioara a cuvintelor din A


	; deci => 
	; B1 = 12h, 1Ah, 3Ch, 56h, 30h
	; B2 = 34h, 2Bh, 4Dh, 78h, 2Bh
	

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov CX, lenA   				
	mov SI, 0						; pt A
	mov DI, 0       				; pt B1
	mov BX, 0						; pt B2

	repeta:
		
		mov AX, SI   ; COPIE
		idiv doi
		cmp AH, 0
		JE inferior
		
		;parte superioara => in B1
		
		mov AL, byte ptr A[SI]
		
		mov B1[DI], AL
		inc DI 
		jmp peste
		
		inferior: 
			mov AL, byte ptr A[SI]
			mov B2[BX], AL
			inc BX
			
		peste:
			inc SI
			
	loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
