;5. Sa se implementeze un program de autentificare. 
;Programul are definit in segmentul de date un sir de caractere numit 'parola'. 
;Programul va cere utilizatorului sa introduca parola de la tastatura 
;si va verifica daca aceasta este identica cu sirul 'parola' din segmentul de date 
;si va afisa un mesaj corespunzator. 
;Programul tot cere utilizatorului parola, pana cand acesta o ghiceste.

assume cs:code, ds:data

data segment
    parola db 'Ana', 0                ; parola corectă terminată cu 0 
    mesaj_corect db 'Parola corecta', '$'
    mesaj_incorect db 'Parola incorecta. Incercati din nou!', '$'
    mesaj_prompt db 'Introduceti parola: ', '$'
    zonaCitire db 20, ?, 20 dup (?)   ; buffer pentru parola introdusă 
data ends

code segment
start:

    mov ax, data
    mov ds, ax

main_loop:
    
    mov ah, 09h
    mov dx, offset mesaj_prompt
    int 21h

    ; citesc parola de la utilizator
    mov ah, 0Ah
    mov dx, offset zonaCitire
    int 21h

    ; inlocuiesc Enter-ul (0Dh) cu 0 
    lea di, zonaCitire + 2         ; adresa primului caracter introdus
    mov cl, zonaCitire + 1         ; lungimea efectivă introdusă 
    add di, cx                     ; mut DI la sfârșitul șirului
    mov byte ptr [di], 0           ; inlocuiesc Enter-ul cu 0 

    ; compar parola introdusă cu parola corectă
    lea si, parola                 ; adresa parolei corecte
    lea di, zonaCitire + 2         ; adresa parolei introduse
	
compara:
    mov al, [si]                   ; preiau caracterul din parola corectă
    cmp al, [di]                   ; compar cu caracterul introdus
    jne parola_incorecta           ; daca diferă, parola este greșită
    
	cmp al, 0                      ; verific dacă am ajuns la terminator
    je parola_corecta              ; daca da, parola este corectă
    
	inc si                         ; trec la caracterul următor din parola corectă
    inc di                         ; trec la caracterul următor introdus
    jmp compara                    ; continui compararea caracter cu caracter

parola_incorecta:
    ; afisez mesajul de eroare
    mov ah, 09h
    mov dx, offset mesaj_incorect
    int 21h
    jmp main_loop                  ; revin la bucla principală

parola_corecta:
    ; afisez mesajul de succes
    mov ah, 09h
    mov dx, offset mesaj_corect
    int 21h
    jmp terminate                  ; ies din program

terminate:
    ; Terminarea programului
    mov ah, 4Ch
    int 21h

code ends
end start
