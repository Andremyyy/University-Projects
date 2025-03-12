; SET A - siruri de OCTETI

;CERINTA: (problema 2)
;	Se dau doua siruri de octeti S1 si S2. 
;	Sa se construiasca sirul D 
;		prin concatenarea elem. S1 1uate de la STANGA spre DREPATA 
;   	si a elementelor S2 luate de la DREAPTA spre STANGA. 

;EXEMPLU:

;S1: 1, 2, 3, 4      S2: 5, 6, 7
; =>
;D: 1, 2, 3, 4, 7, 6, 5

assume cs:code,ds:data

; datele programului:

data segment

	S1 db 1,2,3,4
	lenS1 EQU $-S1
	S2 db 5,6,7
	lenS2 EQU $-S2
	D db lenS1+lenS2 dup(0)

data ends

;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:


mov SI, 0	;registru index pt sirul S1
mov DI, 0	;registru index pt sirul D

mov CX, lenS1 	; nr de repetari pentru loop repetaS1

repetaS1:
	mov AL, S1[SI]
	mov D[DI], AL
	inc SI 
	inc DI
loop repetaS1


mov SI, lenS2 - 1	;registru index pt sirul S2

mov CX, lenS2 	; nr de repetari pentru loop repetaS2

repetaS2:
	mov AL, S2[SI]
	mov D[DI], AL
	sub SI, 1 ; dec 
	inc DI
loop repetaS2


;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start