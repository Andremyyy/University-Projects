;15. Sa se citeasca de la intrarea standard doua numere naturale 
;(a, b, pozitive, mai mici decat 35535, a mai mic decat b) 
;si sa se calculeze R = a + b (aceasta nu trebuie afisata pe ecran).

assume cs:code,ds:data

; datele programului:

data segment

	zonaCitire_a db 20, ?, 20 dup (?)
	zece dw 10
	zonaCitire_b db 20, ?, 20 dup (?)
	a_numar dw 0
	b_numar dw 0

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:
	
	; CITIRE numar a
	mov AH, 0Ah
	mov DX, offset zonaCitire_a
	int 21h
	
	a_from_string_to_number:
		mov SI, offset zonaCitire_a + 2
		
		transform_a:
			mov AL, [SI]
			
			cmp AL, 0Dh     ; compar cu Enter
			je b_from_string_to_number
			
			sub AL, '0'
			mov AH, 0
			mov BX, AX
			mov AX, a_numar
			mul zece
			add AX, BX
			mov a_numar, AX
			inc SI 
			jmp transform_a
			
			
	b_from_string_to_number:
	
		; CITIRE numar b
		mov AH, 0Ah
		mov DX, offset zonaCitire_b
		int 21h
		
		mov SI, offset zonaCitire_b + 2
		
		transform_b:
			mov AL, [SI]
			
			cmp AL, 0Dh     ; compar cu Enter
			je compara
			
			sub AL, '0'
			mov AH, 0
			mov BX, AX
			mov AX, b_numar
			mul zece
			add AX, BX
			mov b_numar, AX
			inc SI 
			jmp transform_b
			
	compara:
		mov AX, a_numar
		cmp AX, b_numar
		JBE suma
		
		; a > b => trebuie invsersate
		mov BX, b_numar
		mov b_numar, AX
		mov a_numar, BX
		
	suma:
		mov AX, b_numar
		add AX, a_numar

;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start