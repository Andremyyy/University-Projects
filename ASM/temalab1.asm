;Sa se calculeze expresiile :

; 2. z=a+b*b-(2/(b*b)/(1+(2/(b*b)))

; am considerat: 

; a cuvant

; b byte 

;preconditie: b != 0

; la impartiri ne intereseaza doar CATUL


; teste efectuate:
; - pt a = 5, b = 2 => rezultatul este 5+4-0 = 9
; - pt a = 3, b = 1 => rezultatul este 3+1-0 = 4


assume cs:code,ds:data

; datele programului:

data segment

a dw 3
b db 1
z dw 0  ; rezultatul final

data ends


;codul:

code segment
start:

mov AX, data
mov DS, AX

; operatiile programului:

mov AL, b
; imul - CU semn
; mul - FARA semn
imul b
;in AX avem b*b (cuvant - 16 biti)

; salvez b*b în CX pentru a ma folosi din nou de acest rezultat
mov CX, ax ; CX = b*b


mov BX, 2 ; BX = 2 (cuvant)
cwd ;convertesc cuvantul din BX in dublucuvant pt impartire (dx:ax)
;idiv - CU semn (+ sau -)
;div - FARA semn(+)
idiv CX ; impart DX:AX la CX 
;catul este in AX = 2 / (b*b) 

mov DX, AX ; salvez in DX 2/(b*b) pt a il folosi la alte operatii

mov AX, 1 ; AX = 1
add AX,DX ;AX = 1 + (2 / (b*b))

mov BX, AX ; BX = 1 + (2 / (b*b))
mov AX, DX; AX = 2/(b*b)
cwd ; convertesc cuvantul din AX in dublucuvant pt impartire
idiv BX ; impart DX:AX la BX
; catul este în AX = (2 / (b*b) / (1 + (2 / (b*b))))

mov DX, AX  ; DX = (2 / (b*b) / (1 + (2 / (b*b))))


mov AX, a ; AX = a
add AX, CX; AX = a+(b*b)

sub AX, DX; AX = a+(b*b) - (2 / (b*b) / (1 + (2 / (b*b))))


mov z, AX



;terminarea programului
mov ah, 4ch       
int 21h

code ends

end start
