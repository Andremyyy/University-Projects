;6. Se da un sir S de dublucuvinte. 
;Sa se obtina sirul D format din octetii inferiori 
;ai cuvintelor inferioare din elementele sirului de dublucuvinte, 
;care sunt multiplii de 7. 
;Exemplu:
;s DD 12345607h, 1A2B3C15h, 13A33412h
;d DB 07h, 15h

assume cs:code,ds:data

; datele programului:

data segment

	S dd 12345607h, 1A2B3C15h, 13A33412h
	lenS EQU $-S
	D db lenS dup(0)
	
	; in MEMORIE:

; 07 56 34 12 15 3C 2B 1A 12 34 A3 13
; --          --          --          

	; octetii -- sunt octetii inferiori ai cuvintelor inferioare


	; deci => (in decimal 15h = 21 si 12h = 18 )
	
	; d = 07h, 15h
	

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

	mov CX, lenS/4    				; pt loop repeta
	mov SI, 0						; pt a parcurge sirul S
	mov DI, 0       				; pt a parcurge sirul D 

	repeta:
		mov AL, byte ptr S[SI]
		cbw							;AL->AX
		mov BL, 7
		idiv BL						; AL = cat si AH = rest
		
		CMP AH, 0
		JNE peste
		
		; e multiplu de 7
		mov AL, byte ptr S[SI]
		mov D[DI], AL
		inc DI
		
		peste:
			add SI, 4
			next:
	loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start