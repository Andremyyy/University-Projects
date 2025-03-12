; 1. Se da un sir de octeti in segmentul de date. 
; Sa se afiseze elementele acestui sir la iesirea standard (ecran) in baza 2.

assume cs:code, ds:data

data segment
    sir db 0ABh, 0F2h, 55h, 0FFh  
    len EQU $ - sir              
data ends

code segment
start:
    mov ax, data       
    mov ds, ax 
	
	mov si, 0       
    mov cl, len  
	
repeta:
	mov AL, sir[SI]
	
	mov DI, 8
	
	mov BL, AL
	
	afiseaza:
		test al, 80h       ; testez bitul cel mai semnificativ
		jz bit_0           ; dacă este 0 => bit_0

		
		mov dl, '1'   
		jmp afisare_bit

		bit_0:
			mov dl, '0'

		afisare_bit:
			mov ah, 02h
			int 21h
		
		
		mov al, bl 
		shl al, 1          ; mut AL la stânga pentru a verifica următorul bit
		mov bl, al


		dec di
		cmp di, 0
		jne afiseaza     ; daca mai sunt biti
		
		
	; după ce am afisat cei 8 biți, afișez un spațiu între octeți
    mov dl, ' '
    mov ah, 2
    int 21h
	
	inc SI
	
loop repeta



;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start