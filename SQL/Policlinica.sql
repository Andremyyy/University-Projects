CREATE DATABASE Policlinica;

USE Policlinica
GO

CREATE TABLE Doctor(
	CNP VARCHAR(14) PRIMARY KEY,
	NUME VARCHAR(50),
	PRENUME VARCHAR(100),
	NR_TEL VARCHAR(20),
	EMAIL VARCHAR(50),
	SALARIU FLOAT,
	SPECIALIZARE VARCHAR(25)

);


CREATE TABLE Pacient(
	ID_PACIENT INT PRIMARY KEY,
	NUME VARCHAR(50),
	PRENUME VARCHAR(100),
	NR_TEL VARCHAR(20),
	EMAIL VARCHAR(50),
);

CREATE TABLE Programari(
	ID_DOCTOR VARCHAR(14),
	ID_PACIENT INT,
	PRIMARY KEY(ID_DOCTOR, ID_PACIENT),
	FOREIGN KEY(ID_DOCTOR) REFERENCES Doctor(CNP) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(ID_PACIENT) REFERENCES Pacient(ID_PACIENT) ON DELETE CASCADE ON UPDATE CASCADE,
	PRET FLOAT,
	DATA_CALEN DATE,
	ORA FLOAT,
	MOTIV_CONSULT VARCHAR(100)
);


CREATE TABLE Cabinet(
	ID_CABINET INT PRIMARY KEY,
	ETAJ INT,
	SPECIALIZARE VARCHAR(100)
);

CREATE TABLE Tura(
	ID_TURA INT PRIMARY KEY,
	ORA_INCEPUT FLOAT,
	ORA_SFARSIT FLOAT,
	ID_CABINET INT,
	CNP_ANGAJAT VARCHAR(14),
	FOREIGN KEY (ID_CABINET) REFERENCES Cabinet(ID_CABINET) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (CNP_ANGAJAT) REFERENCES Doctor(CNP) ON DELETE CASCADE ON UPDATE CASCADE,

);

CREATE TABLE Rezident(
	CNP VARCHAR(14) PRIMARY KEY,
	NUME VARCHAR(50),
	PRENUME VARCHAR(100),
	NR_TEL VARCHAR(20),
	EMAIL VARCHAR(50),
	AN INT,
	CNP_DOCTOR VARCHAR(14),
	FOREIGN KEY (CNP_DOCTOR) REFERENCES Doctor(CNP) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE Rezident
DROP TABLE Programari
DROP TABLE Tura
DROP TABLE Cabinet
DROP TABLE Doctor
DROP TABLE Pacient

INSERT INTO Doctor
VALUES ('2880409678942', 'Andurache', 'Ioana', '0743672815', 'ioana.alina@policlinica.ro', 3000, 'Medicina Generala')

INSERT INTO Doctor
VALUES ('1650215789923', 'Costache', 'Marcel', '0734589042', 'marcel.costache@policlinica.ro', 5000, 'Medicina Interna')

INSERT INTO Doctor
VALUES ('2560814786521', 'Dragomirescu', 'Mihaela', '0743267543' , 'mihaela.drago@policlinica.ro', 4300, 'Cardiologie')

INSERT INTO Doctor
VALUES ('2890704435241', 'Gita', 'Miruna', '0776543256', 'ghita.miru@policlinica.ro', 4800, 'Psihiatrie')

INSERT INTO Doctor
VALUES ('1560809345678', 'Giurgiuveanu', 'Stefan', '0765490987', 'stefan.giurgiuveanu@policlinica.ro', 3900, 'Reumatologie')

INSERT INTO Doctor
VALUES ('5761212546789', 'Lapusneanu', 'Viorel', '0765478654', 'vio.lapusneanu@policlinica.ro', 4500, 'Ortopedie')

INSERT INTO Doctor
VALUES ('1860530786530', 'Lefter', 'Nicolae','0708603021', 'nicolae.lefter@policlinica.ro', 4500, 'Pneumonie')

INSERT INTO Doctor
VALUES ('2980618675432', 'Manolache', 'Maria Magdalena', '0745690231', 'maria.magdalena@policlinica.ro', 3700, 'Imagistica')

INSERT INTO Doctor
VALUES ('1770207564536', 'Mihalache', 'Iulius', '0789565312', 'iulius.mhl@policlinica.ro', 5100, 'Dermatologie')

INSERT INTO Doctor
VALUES ('1721105678390', 'Mihalcea', 'George', '0776590011', 'george.mihalcea@policlinica.ro', 5500, 'Neurologie')

INSERT INTO Doctor
VALUES ('2590301786521', 'Necsulescu', 'Iulia', '0754062431', 'iulia.ncs@policlinica.ro', 4900, 'Pediatrie')

INSERT INTO Doctor
VALUES ('2990505345678', 'Papurica', 'Valeria', '0765489761', 'papu.valeria@policlinica.ro', 4800, 'Endocrinologie')

SELECT * FROM Doctor



INSERT INTO Pacient
VALUES ( 1, 'Alexandru', 'Ioana', '0733961991' , 'alexandru.ioana@gmail.com')

INSERT INTO Pacient
VALUES ( 2, 'Barbu', 'Ion', '0722191993' , 'barbu.ion@gmail.com')

INSERT INTO Pacient
VALUES ( 3, 'Dumitru', 'Dumitru', '0722311112' , 'dumitru.dumitru@gmail.com')

INSERT INTO Pacient
VALUES ( 4, 'Ghita', 'Ilinca', '0745987123' , 'ghita.ioana@gmail.com')

INSERT INTO Pacient
VALUES ( 5, 'Ilie', 'Alexandru', '0733112445' , 'ilie.alexandru@gmail.com')

INSERT INTO Pacient
VALUES ( 6, 'Ion', 'Alexandra', '0723673111' , 'ion.alexandra@gmail.com')

INSERT INTO Pacient
VALUES ( 7, 'Ion', 'Stefania', '0723512344' , 'ion.stefania@gmail.com')

INSERT INTO Pacient
VALUES ( 8, 'Ion', 'Mihai', '0722333134' , 'ion.mihai@gmail.com')

INSERT INTO Pacient
VALUES ( 9, 'Lipan', 'Victoria', '0787661223' , 'lipan.victoria@gmail.com')

INSERT INTO Pacient
VALUES ( 10, 'Manolache', 'Otilia', '0712331223' , 'manolache.otilia@gmail.com')

INSERT INTO Pacient
VALUES ( 11,'Marcu','Otilia', '0909001023', 'marcu.otilia@gmail.com')

SELECT * FROM Pacient




INSERT INTO Programari
VALUES ('2560814786521',1 ,250 ,'2023-02-02', 15 , 'Dureri toracice')

INSERT INTO Programari
VALUES ('2890704435241',2 ,175 ,'2024-04-04', 10 , 'Tulburari de personalitate')

INSERT INTO Programari
VALUES ('1560809345678',3 ,210 ,'2024-04-15', 18 , 'Dureri articulare')

INSERT INTO Programari
VALUES ('5761212546789',4 ,310 ,'2023-02-20', 11, NULL)

INSERT INTO Programari
VALUES ('1860530786530',5 ,275 ,'2023-02-14', 16 , 'Dureri pulmonare si dificultati in respiratie')

INSERT INTO Programari
VALUES ('2980618675432',6 ,190 ,'2024-05-23', 11 , NULL)

INSERT INTO Programari
VALUES ('1770207564536',7 ,240 ,'2024-05-24', 16 , NULL)

INSERT INTO Programari
VALUES ('1721105678390',8 ,450 ,'2024-05-24', 11 ,'Dureri de cap')

INSERT INTO Programari
VALUES ('2590301786521',9 ,230 ,'2023-06-06', 17, NULL )
INSERT INTO Programari
VALUES ('2990505345678',10 ,210 ,'2023-06-03', 19, NULL )


SELECT * FROM Programari 




INSERT INTO Cabinet
VALUES ( 1, 0, 'Ortopedie')
INSERT INTO Cabinet
VALUES ( 2, 0, 'Neurologie')
INSERT INTO Cabinet
VALUES ( 3, 1, 'Medicina Interna')
INSERT INTO Cabinet
VALUES ( 4, 1, 'Imagistica')
INSERT INTO Cabinet
VALUES ( 5, 2, 'Pediatrie')
INSERT INTO Cabinet
VALUES ( 6, 3, 'Reumatologie')
INSERT INTO Cabinet
VALUES ( 7, 3, 'Gastroenterologie')
INSERT INTO Cabinet
VALUES ( 8, 2, 'Endocrinologie')
INSERT INTO Cabinet
VALUES ( 9, 0, 'Oftalmologie')
INSERT INTO Cabinet
VALUES ( 10, 1, 'Dermatologie')
INSERT INTO Cabinet
VALUES ( 11, 0, 'Cardiologie')
INSERT INTO Cabinet
VALUES ( 12, 3, 'Psihiatrie')
INSERT INTO Cabinet
VALUES ( 13, 3, 'Pneumologie')
INSERT INTO Cabinet
VALUES (14, 0, 'Medicina Generala')

SELECT * FROM Cabinet


 
INSERT INTO Rezident 
VALUES ('1981111222333', 'Popescu', 'Andrei', '0712345678', 'popescu.andrei@policlinica.ro', 1, '1560809345678') --doctor: Giurgiuveanu Stefan
INSERT INTO Rezident 
VALUES('2990515223456', 'Ionescu', 'Maria', '0723456789', 'ionescu.maria@policlinica.ro', 2, '1650215789923') -- doctor: Costache Marcel
INSERT INTO Rezident 
VALUES('1970628334567', 'Georgescu', 'Alexandru', '0731122334', 'georgescu.alexandru@policlinica.ro', 3, '1721105678390') -- doctor: Mihalcea George
INSERT INTO Rezident 
VALUES('2000101023456', 'Dumitrescu', 'Cristina', '0745566778', 'dumitrescu.cristina@policlinica.ro', 4, '1560809345678') -- doctor: Giurgiuveanu Stefan 
INSERT INTO Rezident 
VALUES('1980223334567', 'Stan', 'Mihai', '0759988776', 'stan.mihai@policlinica.ro', 1, '1770207564536') -- doctor: Mihalache Iulius
INSERT INTO Rezident 
VALUES('2991209334567', 'Popa', 'Ioana', '0762233445', 'popa.ioana@policlinica.ro', 2, '1860530786530') -- doctor: Lefter Nicolae
INSERT INTO Rezident 
VALUES('1970308334567', 'Vasilescu', 'George', '0778899001', 'vasilescu.george@policlinica.ro', 3, '2560814786521') -- doctor: Dragomirescu Mihaela
INSERT INTO Rezident 
VALUES('2000710334567', 'Marin', 'Ana', '0786655443', 'marin.ana@policlinica.ro', 4, '2590301786521') -- doctor: Necsulescu Iulia
INSERT INTO Rezident 
VALUES('1990915334567', 'Radu', 'Darius', '0791122334', 'radu.darius@policlinica.ro', 1, '2880409678942') -- doctor: Andurache Ioana
INSERT INTO Rezident 
VALUES('1981222334567', 'Iliescu', 'Alina', '0719988776', 'iliescu.alina@policlinica.ro', 4, '2890704435241') -- doctor: Gita Miruna

SELECT * FROM Rezident



INSERT INTO Tura
VALUES ( 1, 7, 12,1 , '5761212546789')
INSERT INTO Tura
VALUES ( 2, 7,17,13 , '1860530786530')
INSERT INTO Tura
VALUES ( 3, 9, 14,12 , '2890704435241')
INSERT INTO Tura
VALUES ( 4, 7, 19,14 , '2880409678942')
INSERT INTO Tura
VALUES ( 5, 7,14 ,3 , '1650215789923')
INSERT INTO Tura
VALUES ( 6, 11,18 ,4 , '2980618675432')
INSERT INTO Tura
VALUES ( 7, 9, 18, 5, '2590301786521')
INSERT INTO Tura
VALUES ( 8, 11, 18, 6, '1560809345678')
INSERT INTO Tura
VALUES ( 9, 15, 19, 8, '2990505345678')

SELECT * FROM Tura

-- MODIFICARI:
--In comenzile de modificare / stergere folositi cel putin o data în clauza WHERE:
--	- operatori logici (AND, OR, NOT)
--	- operatori relationali (<, <=, =, >, >=, <>)
--	- IS [NOT] NULL


UPDATE Programari
SET MOTIV_CONSULT = 'Consult periodic'
WHERE id_pacient = 9 OR ORA = 16

SELECT * FROM Programari

UPDATE TURA
SET ORA_INCEPUT = 7
WHERE ORA_SFARSIT <= 14

SELECT * FROM TURA


-- STERGERI: (pe astea le va sterge)

--INSERT INTO Programari
--VALUES ('2990505345678',10 ,210 ,'2023-06-03', 19, NULL )
--INSERT INTO Programari
--VALUES ('2980618675432',6 ,190 ,'2024-05-23', 11 , NULL)
--INSERT INTO Programari
--VALUES ('5761212546789',4 ,310 ,'2023-02-20', 11, NULL)

DELETE FROM Programari
WHERE MOTIV_CONSULT IS NULL

SELECT * FROM Programari
-- 3 rows affected

SELECT * FROM Doctor
SELECT * FROM Programari
SELECT * FROM Pacient
SELECT * FROM Tura
SELECT * FROM Cabinet



--   LAB 3 



INSERT INTO Tura
VALUES ( 10, 14, 20,1 , '5761212546789')
INSERT INTO Tura
VALUES ( 11, 22, 24,1 , '5761212546789')
-- 5761212546789 are turele: 7-12, 14-20, 22-24
INSERT INTO Tura
VALUES ( 12, 22, 24,13 , '1860530786530')
-- 1860530786530 are turele: 7-17, 22-24
INSERT INTO Tura
VALUES ( 13, 22, 24,4 , '5761212546789')
-- 2980618675432 are turele: 11-18,22-24

INSERT INTO Doctor 
VALUES ('1990909090909', 'Popescu', 'Vasile', '0722222222', 'vasile.popescu@policlinica.ro', 3700, 'Gastroenterologie');

INSERT INTO Doctor 
VALUES ('1770707070707', 'Ionescu', 'Roxana', '0711111111', 'roxana.ionescu@policlinica.ro', 6000, 'Oftalmologie');

INSERT INTO Doctor 
VALUES ('1550505050505', 'Marin', 'Catalin', '0733333333', 'catalin.marin@policlinica.ro', 4200, 'Dermatologie');

INSERT INTO Pacient 
VALUES (12, 'Nistor', 'Vlad', '0700112233', 'nistor.vlad@gmail.com');

INSERT INTO Pacient 
VALUES (13, 'Barna', 'Diana', '0700665544', 'barna.diana@gmail.com');

INSERT INTO Pacient 
VALUES (14, 'Petrescu', 'Ana', '0755544332', 'petrescu.ana@gmail.com');

INSERT INTO Programari 
VALUES ('1990909090909', 12, 500, '2024-08-01', 9, 'Consult gastroenterologic');

INSERT INTO Programari 
VALUES ('1770707070707', 13, 150, '2024-08-02', 14, 'Control oftalmologic');

INSERT INTO Programari 
VALUES ('1550505050505', 14, 300, '2024-08-03', 11, 'Consult dermatologic');

INSERT INTO Programari 
VALUES ('2880409678942', 10, 200, '2024-07-20', 10, 'Control anual');

INSERT INTO Cabinet 
VALUES (15, 2, 'Gastroenterologie');
INSERT INTO Cabinet 
VALUES (16, 3, 'Oftalmologie');

INSERT INTO Tura 
VALUES (14, 8, 15, 15, '1990909090909'); -- Gastroenterologie
INSERT INTO Tura 
VALUES (15, 12, 18, 16, '1770707070707'); -- Oftalmologie
INSERT INTO Tura 
VALUES (16, 9, 14, 10, '1550505050505'); -- Dermatologie

INSERT INTO Rezident 
VALUES ('2991234567890', 'Matei', 'Radu', '0723456780', 'matei.radu@policlinica.ro', 1, '1990909090909'); -- doctor: Popescu Vasile

INSERT INTO Rezident 
VALUES ('2981234567890', 'Andrei', 'Mihai', '0712233445', 'andrei.mihai@policlinica.ro', 2, '1770707070707'); -- doctor: Ionescu Roxana

INSERT INTO Rezident 
VALUES ('2971234567890', 'Simion', 'Elena', '0733344556', 'simion.elena@policlinica.ro', 3, '1550505050505'); -- doctor: Marin Catalin

INSERT INTO Tura 
VALUES (17, 15, 19, 9, '1770707070707'); -- Tura pentru oftalmologie
INSERT INTO Tura 
VALUES (18, 7, 12, 11, '1990909090909'); -- Tura pentru gastroenterologie

INSERT INTO Programari 
VALUES ('1650215789923', 14, 450, '2024-06-20', 9, 'Consult cardiologic');

INSERT INTO Programari 
VALUES ('1550505050505', 13, 175, '2024-07-10', 13, 'Consultație dermatologică');

SELECT * FROM Doctor;
SELECT * FROM Pacient;
SELECT * FROM Programari;
SELECT * FROM Cabinet;
SELECT * FROM Tura;
SELECT * FROM Rezident;


--LAB 3


SELECT ID_CABINET from Tura
intersect
SELECT ID_CABINET from Cabinet
-- afiseaza doar ID-urile cabinetele care apar în ambele tabele

SELECT d.NUME AS Nume_Doctor, d.PRENUME AS Prenume_Doctor, p.NUME AS Nume_Pacient, p.PRENUME AS Prenume_Pacient, pr.DATA_CALEN, pr.PRET
FROM Doctor d
INNER JOIN Programari pr ON d.CNP = pr.ID_DOCTOR
INNER JOIN Pacient p ON pr.ID_PACIENT = p.ID_PACIENT;
-- Lista cu doctorii, pacienții și detaliile programărilor.

SELECT r.NUME AS NumeRezident, r.PRENUME AS PrenumeRezident, d.NUME AS NumeDoctor, d.PRENUME AS PrenumeDoctor
FROM Rezident r
RIGHT JOIN Doctor d ON r.CNP_DOCTOR = d.CNP;
--selectez toate tabelele Rezident și leg cu Doctor pentru a vedea dacă există doctori care nu au medici rezidenti:
-- => toți doctorii, iar în cazurile în care nu există rezidenti asignati doctorilor, valorile sunt NULL.



SELECT d.NUME, d.PRENUME, COUNT(pr.ID_PACIENT) AS NumarProgramari
FROM Doctor d
INNER JOIN Programari pr ON d.CNP = pr.ID_DOCTOR
GROUP BY d.NUME, d.PRENUME;
-- => nr de programări pentru fiecare doctor


SELECT d.NUME, d.PRENUME, SUM(pr.PRET) AS VenitTotal
FROM Doctor d
INNER JOIN Programari pr ON d.CNP = pr.ID_DOCTOR
GROUP BY d.NUME, d.PRENUME
HAVING SUM(pr.PRET) > 400;
-- doar doctorii cu salariu > 400.


SELECT SPECIALIZARE, COUNT(*) AS NumarDoctori
FROM Doctor
GROUP BY SPECIALIZARE;
-- nr de doctori pe specializare


SELECT NUME, PRENUME 
FROM Pacient 
WHERE ID_PACIENT IN (SELECT ID_PACIENT FROM Programari WHERE PRET < 250);
-- =>  pacienții care au avut o programare cu prețul < 250


SELECT NUME, PRENUME 
FROM Pacient 
WHERE ID_PACIENT IN (SELECT ID_PACIENT FROM Programari WHERE DATA_CALEN > '2024-01-01');
-- =>toti pacientii care au o programare dupa 1.01.2024


SELECT NUME, PRENUME
FROM Doctor d
WHERE EXISTS (SELECT 1 FROM Programari pr WHERE pr.ID_DOCTOR = d.CNP);
-- => doctorii care au cel puțin o programare:


SELECT NUME, PRENUME
FROM Doctor
WHERE EXISTS (SELECT 1 FROM Programari WHERE Programari.ID_DOCTOR = Doctor.CNP AND Programari.PRET > 200);
-- => doctorii care au mai mult de po progrmare cu pretul > 200


-- selectez programările în care prețul < 250  SAU data > 01-01-2024,
-- DAR exclud programările care au ca motiv "Consult periodic"
SELECT ID_DOCTOR, ID_PACIENT, PRET, DATA_CALEN, ORA, MOTIV_CONSULT
FROM Programari
WHERE (PRET < 250 OR DATA_CALEN > '2024-01-01')
  AND NOT (MOTIV_CONSULT = 'Consult periodic');


-- selectez toate specializările doctorilor distincte și afișează numele acestora
SELECT DISTINCT SPECIALIZARE
FROM Doctor;

-- selectez toți doctorii care au programări în care prețul > 300  SAU au pacienți 
-- cu prenumele care începe cu 'A', DAR exclud doctorii care au specializarea "Pediatrie"
-- JOIN = INNER JOIN
SELECT DISTINCT d.NUME, d.PRENUME, d.SPECIALIZARE
FROM Doctor d
JOIN Programari p ON d.CNP = p.ID_DOCTOR
JOIN Pacient pac ON p.ID_PACIENT = pac.ID_PACIENT
WHERE (p.PRET > 300 OR pac.PRENUME LIKE 'A%')
  AND NOT d.SPECIALIZARE = 'Pediatrie';


--LAB 4

--1. scrieti cate o procedura stocata care introduce date intr-un tabel, pentru cel putin trei tabele,
-- incluzand un tabel cu o cheie primara compusa;
 
 -- parametrii unei astfel de proceduri sunt atributele care descriu entitatile / relatiile din tabel, 
 -- mai putin coloanele cheilor primare (exceptie facand o procedura stocata care adauga date intr-o 
 -- tabela de legatura, pentru care se poate indica cheia primara);
 
 -- fiecare procedura va utiliza functii pentru validarea anumitor parametri; se cer cel putin trei functii user-defined (optional se pot utiliza, pe langa aceste trei functii, si functii sistem); 

--2. creati un view care combina date care provin din doua sau trei tabele; 

--3. implementati, pentru un tabel la alegere, un trigger pentru operatia de adaugare si unul pentru
 --cea de stergere; la executia fiecarui trigger se va afisa pe ecran un mesaj cu data si ora la care
 --s-a realizat operatia, tipul operatiei (Insert/Delete) si numele tabelului; optional, puteti crea
-- triggere similare si pentru alte tabele.


CREATE FUNCTION dbo.ValidareCNP(@CNP VARCHAR(14))
RETURNS BIT
AS
BEGIN
    RETURN CASE 
        WHEN len(@CNP)=13 THEN 1
        ELSE 0
    END
END;


CREATE FUNCTION dbo.ValidarePret(@pret float)
RETURNS BIT
AS
BEGIN
    RETURN CASE 
        WHEN @pret >= 0 THEN 1
        ELSE 0
    END
END;

CREATE FUNCTION dbo.ValidareNumeRezident(@nume VARCHAR(50))
RETURNS BIT
AS
BEGIN
    RETURN CASE 
        WHEN LEN(@nume) > 0 AND LEN(@nume) <= 50 THEN 1
        ELSE 0
    END
END;

CREATE FUNCTION dbo.ValidareAnRezident(@an INT)
RETURNS BIT
AS
BEGIN
    RETURN CASE 
        WHEN @an > 0 THEN 1
        ELSE 0
    END
END;

CREATE PROCEDURE AdaugaRezident
	@cnp VARCHAR(14),
    @nume VARCHAR(50),
	@prenume VARCHAR(100),
	@nr_tel VARCHAR(20),
	@email VARCHAR(50),
    @an int,
	@cnp_doctor VARCHAR(14)
AS
BEGIN
    IF dbo.ValidareNumeRezident(@nume) = 1 AND dbo.ValidareAnRezident(@an) = 1 AND dbo.ValidareCNP(@cnp_doctor) = 1
    BEGIN
        INSERT INTO Rezident (cnp, nume, prenume, nr_tel, email, an, cnp_doctor)
        VALUES (@cnp, @nume, @prenume, @nr_tel, @email, @an, @cnp_doctor);
        PRINT 'Rezient adaugat cu succes!';
    END
    ELSE
    BEGIN
        PRINT 'Parametri invalizi!';
    END
END;

select * from doctor
select * from Rezident

EXEC AdaugaRezident @cnp = '2601234555890' , @nume = 'Alexandrescu' , @prenume = 'Emilia', @nr_tel = '0786625443', @email = 'alexandrescu.emilia@policlinica.ro', @an = 3, @cnp_doctor = '1721105678390'
-- CNP_DOCTOR INVALID
EXEC AdaugaRezident @cnp = '2601234567890' , @nume = 'Alexandrescu' , @prenume = 'Emilia', @nr_tel = '0786625443', @email = 'alexandrescu.emilia@policlinica.ro', @an = 3, @cnp_doctor = '178390'


-- cheie primara compusa 
CREATE PROCEDURE AdaugaProgramare
	@id_doctor VARCHAR(14),
    @id_pacient INT,
	@pret FLOAT,
	@data_calen DATE,
	@ora FLOAT,
    @motiv_consult VARCHAR(100)
AS
BEGIN
    IF dbo.ValidarePret(@pret) = 1 AND dbo.ValidareAnRezident(@id_pacient) = 1 AND dbo.ValidareCNP(@id_doctor) = 1
    BEGIN
        INSERT INTO Programari (id_doctor, id_pacient, pret, data_calen, ora, motiv_consult)
        VALUES (@id_doctor, @id_pacient, @pret, @data_calen, @ora, @motiv_consult);
        PRINT 'Programare adaugata cu succes!';
    END
    ELSE
    BEGIN
        PRINT 'Parametri invalizi!';
    END
END;

select * from doctor
select * from pacient

EXEC AdaugaProgramare @id_doctor = '1860530786530', @id_pacient = 10, @pret = 250, @data_calen = '2024-11-01', @ora = 13, @motiv_consult = 'consult'
-- id_pacient invalid
EXEC AdaugaProgramare @id_doctor = '1860530786530', @id_pacient = -11, @pret = 250, @data_calen = '2024-11-01', @ora = 13, @motiv_consult = NULL


CREATE PROCEDURE AdaugaDoctor
	@cnp VARCHAR(14),
    @nume varchar(50),
	@prenume varchar(100),
	@nr_tel VARCHAR(20),
	@email VARCHAR(50),
	@salariu FLOAT,
	@specializare VARCHAR(25)

AS
BEGIN
    IF dbo.ValidareAnRezident(@salariu) = 1 AND dbo.ValidareCNP(@cnp) = 1 AND dbo.ValidareNumeRezident(@nume) = 1
    BEGIN
        INSERT INTO Doctor (cnp, nume, prenume, nr_tel, email, salariu, specializare )
        VALUES (@cnp, @nume, @prenume, @nr_tel, @email, @salariu, @specializare );
        PRINT 'Doctor adaugat cu succes!';
    END
    ELSE
    BEGIN
        PRINT 'Parametri invalizi!';
    END
END;

select * from doctor

EXEC AdaugaDoctor @cnp = '1580813786521', @nume = 'Dragomirescu', @prenume = 'Mihai', @nr_tel = '0743267543' , @email = 'mihai.drago@policlinica.ro', @salariu = 4800, @specializare = 'Medicina Generala'
-- nume invalid
EXEC AdaugaDoctor @cnp = '1580814786521', @nume = NULL, @prenume = 'Mihai', @nr_tel = '0743267543' , @email = 'mihai.drago@policlinica.ro', @salariu = 4800, @specializare = 'Medicina Generala'



CREATE VIEW VW_ProgramariPacientiDoctori AS
SELECT 
    p.id_pacient,
    p.prenume,
    p.nr_tel,
    d.cnp,
    d.nume,
    d.specializare,
    pr.pret,
    pr.data_calen,
    pr.ora,
    pr.motiv_consult
FROM 
    Programari pr
INNER JOIN 
    Doctor d ON pr.id_doctor = d.cnp
INNER JOIN 
    Pacient p ON pr.id_pacient = p.id_pacient;


select * from VW_ProgramariPacientiDoctori



CREATE TRIGGER Trig_Insert_Pacient
ON Pacient
AFTER INSERT
AS
BEGIN
    DECLARE @data_ora DATETIME;
    SET @data_ora = GETDATE();
    
    PRINT 'Operatia: INSERT';
    PRINT 'Tabelul: Pacient';
    PRINT 'Data si ora operatiei: ' + CONVERT(VARCHAR, @data_ora, 120);
END;


insert into Pacient 
Values (23, 'Marin', 'Marius', '0725252525', 'marius.marin@gmail.com')


CREATE TRIGGER Trig_Delete_Pacient
ON Pacient
AFTER DELETE
AS
BEGIN
    DECLARE @data_ora DATETIME;
    SET @data_ora = GETDATE();
    
    PRINT 'Operatia: DELETE';
    PRINT 'Tabelul: Pacient';
    PRINT 'Data si ora operatiei: ' + CONVERT(VARCHAR, @data_ora, 120);
END;


DELETE FROM Pacient
WHERE nume = 'Marin' AND prenume = 'Marius'


