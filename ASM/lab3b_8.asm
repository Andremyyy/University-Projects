;8.Se da un sir de dublucuvinte. 
;Sa se obtina sirul format din octetii superiori ai cuvintelor inferioare
; din elementele sirului de dublucuvinte, care sunt multiplii de 10. 
;Exemplu:
;Se da sirul de dublucuvinte: 
;s DD 12345678h, 1A2B3C4Dh, 1298DC76h 
;Sa se obtina sirul 
;d DB 3Ch, DCh.

assume cs:code,ds:data

; datele programului:

data segment

	S dd 12345678h, 1A2B3C4Dh, 1298DC76h
	lenS EQU $-S
	D db lenS dup(0)
	
	; in MEMORIE:

; 78 56 34 12 4D 3C 2B 1A 76 DC 98 12
;    --          --          --      

	; octetii -- sunt octetii superiori ai cuvintelor superioare


	; deci => (in decimal 56h = 86 si 3Ch = 60, DCh = 220)
	
	; d = 3Ch, DCh
	

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov CX, lenS/4    				; pt loop repeta
mov SI, 1						; pt a parcurge sirul S
mov DI, 0       				; pt a parcurge sirul D 

repeta:
	mov AL, byte ptr S[SI]
	cbw							;AL->AX
	mov BL, 10
	idiv BL						; AL = cat si AH = rest
	
	CMP AH, 0
	JNE peste
	
	; e multiplu de 10
	mov AL, byte ptr S[SI]
	mov D[DI], AL
	inc DI

	peste:
		add SI, 4
loop repeta


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
