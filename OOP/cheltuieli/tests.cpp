//
// Created by ema_a on 4/8/2024.
//
#include <iostream>
using namespace std;
#include <cstring>

#include "tests.h"
#include "Cheltuieli.h"
#include "Repo.h"
#include "cassert"
#include "Service.h"
#include <vector>
using namespace std;

void testCheltuieli(){
    Cheltuieli c1;
    assert (c1.getzi() == 0 );
    assert (c1.getsuma() == 0);
    assert (c1.gettip() == nullptr);

    char * tip = "menaj";
    Cheltuieli c2(4,200,tip);

    assert (strcmp(c2.gettip(), "menaj" ) == 0);
    assert(c2.getsuma() == 200);
    assert (c2.getzi() == 4);

    c2.setzi(5);
    assert(c2.getzi() == 5);

}

void testRepo(){
    Cheltuieli c1(5,100,"altele");
    Cheltuieli c2(25,360,"internet");
    Cheltuieli c3(23,120,"mancare");
    Cheltuieli c4(15,635,"haine");
    Cheltuieli c5(15,400,"menaj");

    Repo r;
    r.addElem(c1);
    r.addElem(c2);
    r.addElem(c3);
    r.addElem(c4);
    r.addElem(c5);

    vector <Cheltuieli> a = r.getAll();
    int size = r.dim();

    assert(a[0] == c1);
    assert(size == 5);
    assert(a[3] == c4);

    r.deleteElem(1);
    assert(r.dim() == 4);

    Cheltuieli chelt(25,635,"haine");
    r.updateElem(3, chelt);
    a = r.getAll();
    assert(a[3].getzi() == 25);

}

void testService() {

    Service s;



    //test adaugare:
    s.addElem(600, "haine");
    assert(s.getElem(0).getsuma() == 600);




    //test insert:
    s.insertElem(12, 750, "altele");
    assert(s.getElem(1).getzi() == 12);

    s.addElem(2000, "mancare");
    assert(s.getElem(2).getsuma() == 2000);




    //test update:
    s.updateElem(12, 750, "altele", 13, 560, "menaj");
    assert(s.getElem(1).getzi() == 13);




    //test delete:
    s.deleteElem(13, 560, "menaj");
    assert(s.getElem(1).getsuma() == 2000);
    assert(s.getElem(1).getzi() == s.today());




    // test getAll:
    vector < Cheltuieli > c = s.getAll();
    assert(c[0].getsuma() == 600);

    // s:
    // 21,600,"haine" (today)
    // 21, 2000,"mancare" (today)
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"haine"




    // test getsize:

    assert(s.getsize() == 2);

    s.addElem(21, "menaj");
    s.insertElem(14, 650, "menaj");
    s.addElem(300, "internet");
    s.insertElem(15, 750, "mancare");
    s.insertElem(20, 850, "haine");




    //test deleteCheltZi:

    assert (s.deleteCheltZi(22) == 4);
    assert (s.deleteCheltZi(1) == 0);

    // s:
    // 14,650,"menaj"
    // 15,750,"mancare"
    // 20,850,"haine"

    assert (s.getsize() == 3);
    assert (s.deleteCheltZi(20) == 1);

    // s:
    // 14,650,"menaj"
    // 15,750,"mancare"

    assert (s.getsize() == 2);





    //test deleteCheltInterval:

    s.addElem(21, "menaj");
    s.insertElem(14, 650, "menaj");
    s.addElem(300, "internet");
    s.insertElem(15, 750, "mancare");
    s.insertElem(20, 850, "haine");
    s.insertElem(13, 850, "haine");
    s.insertElem(12, 850, "haine");
    s.insertElem(24, 850, "haine");
    s.insertElem(22, 850, "haine");

    // s:
    // 14,650,"menaj"
    // 15,750,"mancare"
    // 21,21,"menaj" (today)
    // 14,650,"menaj" (today)
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"haine"
    // 13,850,"haine"
    // 12,850,"haine"
    // 24,850,"haine"
    // 22,850,"haine"

    Cheltuieli c0(14, 650, "menaj");
    Cheltuieli c1(15, 750, "mancare");
    Cheltuieli c2(21, 21, "menaj");  //IL STERGE
    Cheltuieli c3(14, 650, "menaj");
    Cheltuieli c4(21, 300, "internet"); // IL STERGE
    Cheltuieli c5(15, 750, "mancare");
    Cheltuieli c6(20, 850, "haine"); //IL STERGE
    Cheltuieli c7(13, 850, "haine");
    Cheltuieli c8(12, 850, "haine");
    Cheltuieli c9(24, 850, "haine");
    Cheltuieli c10(22, 850, "haine"); //IL STERGE

    assert(s.getsize() == 11);

    assert (s.deleteCheltInterval(20, 23) == 4);
    assert(s.getsize() == 7);

    assert (s.getElem(0) == c0);
    assert (s.getElem(1) == c1);
    assert (s.getElem(2) == c3);
    assert (s.getElem(3) == c5);
    assert (s.getElem(4) == c7);
    assert (s.getElem(5) == c8);
    assert (s.getElem(6) == c9);

    // s:
    // 14,650,"menaj"
    // 15,750,"mancare"
    // 14,650,"menaj" (today)
    // 15,750,"mancare"
    // 13,850,"haine"
    // 12,850,"haine"
    // 24,850,"haine"

    assert (s.deleteCheltInterval(14, 14) == 2);
    assert(s.getsize() == 5);

    // s:
    // 15,750,"mancare"
    // 15,750,"mancare"
    // 13,850,"haine"
    // 12,850,"haine"
    // 24,850,"haine"

    assert (s.deleteCheltInterval(15, 13) == 3);
    assert(s.getsize() == 2);

    // s:
    // 12,850,"haine"
    // 24,850,"haine"

    assert (s.deleteCheltInterval(20, 23) == 0);
    assert(s.getsize() == 2);




    // test getElem:


    // s:
    // 12,850,"haine"
    // 24,850,"haine"

    assert(s.getElem(0) == c8);
    assert(s.getElem(1) == c9);





    //test deleteCheltTip:

    // s:
    // 12,850,"haine"
    // 24,850,"haine"

    s.addElem(21, "menaj");
    s.insertElem(14, 650, "menaj");
    s.addElem(300, "internet");
    s.insertElem(15, 750, "mancare");
    s.insertElem(20, 850, "transport");
    s.insertElem(13, 850, "menaj");
    s.insertElem(12, 850, "menaj");
    s.insertElem(24, 850, "internet");
    s.insertElem(22, 850, "haine");

    // s:
    // 12,850,"haine"
    // 24,850,"haine"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 13,850,"menaj"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 22,850,"haine"

    assert(s.getsize() == 11);

    assert(s.deleteCheltTip("haine") == 3);
    assert(s.getsize() == 8);

    // s:
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 13,850,"menaj"
    // 12,850,"menaj"
    // 24,850,"internet"

    assert(s.deleteCheltTip("haine") == 0);

    assert(s.deleteCheltTip("menaj") == 4);
    assert(s.getsize() == 4);

    // s:
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 24,850,"internet"

    assert(s.deleteCheltTip("transport") == 1);
    assert(s.getsize() == 3);

    // s:
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 24,850,"internet"





    // test getSizeTip:

    s.addElem(21, "menaj");
    s.insertElem(14, 650, "menaj");
    s.addElem(300, "internet");
    s.insertElem(15, 750, "mancare");
    s.insertElem(20, 850, "transport");
    s.insertElem(13, 850, "menaj");
    s.insertElem(12, 850, "menaj");
    s.insertElem(24, 850, "internet");
    s.insertElem(22, 850, "haine");

    // s:
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21,13,850,"menaj" (today)
    // 12,850,"menaj"
    // 24,850,"internet"
    // 22,850,"haine"

    assert(s.getSizeTip("internet") == 4);
    assert(s.getSizeTip("transport") == 1);
    assert(s.getSizeTip("menaj") == 4);
    assert(s.getSizeTip("mancare") == 2);
    assert(s.getSizeTip("haine") == 1);
    assert(s.getSizeTip("altele") == 0);





    // test getSizeTipBiggerThanSuma:

    // s:
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21,13,850,"menaj" (today)
    // 12,850,"menaj"
    // 24,850,"internet"
    // 22,850,"haine"

    assert(s.getSizeTipBiggerThanSuma("internet", 300) == 2);
    assert(s.getSizeTipBiggerThanSuma("internet", 299) == 4);
    assert(s.getSizeTipBiggerThanSuma("menaj", 850) == 0);
    assert(s.getSizeTipBiggerThanSuma("mancare", 200) == 2);
    assert(s.getSizeTipBiggerThanSuma("haine", 820) == 1);
    assert(s.getSizeTipBiggerThanSuma("altele", 1000) == 0);

    // test getSizeTipEqualSuma:

    // s:
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 13,850,"menaj"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 22,850,"haine"

    assert(s.getSizeTipEqualSuma("internet", 300) == 2);
    assert(s.getSizeTipEqualSuma("internet", 299) == 0);
    assert(s.getSizeTipEqualSuma("menaj", 850) == 2);
    assert(s.getSizeTipEqualSuma("mancare", 200) == 0);
    assert(s.getSizeTipEqualSuma("haine", 850) == 1);
    assert(s.getSizeTipEqualSuma("altele", 1000) == 0);




    //test detSumaTip:

    // s:
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 13,850,"menaj"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 22,850,"haine"

    assert(s.detSumaTip("transport") == 850);
    assert(s.detSumaTip("internet") == 2300);
    assert(s.detSumaTip("menaj") == 2371);
    assert(s.detSumaTip("mancare") == 1500);
    assert(s.detSumaTip("haine") == 850);
    assert(s.detSumaTip("altele") == 0);



    //test detZiMaxSuma:

    // s:
    // 21, 300,"internet" (today)
    // 15,750,"mancare"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 13,850,"menaj"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 22,850,"haine"

    assert(s.detZiMaxSuma() == 24);




    // test getSizeZi:

    // s:
    // 22, 300,"internet" (today)
    // 15,750,"mancare"
    // 24,850,"internet"
    // 22,21,"menaj" (today)
    // 14,650,"menaj"
    // 22,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 13,850,"menaj"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 22,850,"haine"

    assert(s.getSizeZi(22) == 4);
    assert(s.getSizeZi(15) == 2);
    assert(s.getSizeZi(24) == 2);

    assert(s.getSizeZi(20) == 1);
    assert(s.getSizeZi(1) == 0);





    //test getSizeTipZi:

    s.updateElem(22, 850, "haine", 21, 3457, "internet");
    s.updateElem(13, 850, "menaj", 14, 3450, "menaj");
    s.updateElem(14, 3450, "menaj", 21, 300, "internet");
    s.updateElem(15, 750, "mancare", 14, 3450, "menaj");

    // s:
    // 21, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"

    assert(s.getSizeTipZi("menaj", 14) == 2);
    assert(s.getSizeTipZi("internet", 24) == 2);
    assert(s.getSizeTipZi("menaj", 22) == 1);
    assert(s.getSizeTipZi("mancare", 16) == 0);
    assert(s.getSizeTipZi("internet", 22) == 2);
    assert(s.getSizeTipZi("altele", 21) == 0);





    //test getSizeTipLessThanSuma

    // s:
    // 21, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"

    assert(s.getSizeTipLessThanSuma("menaj", 3451) == 4);
    assert(s.getSizeTipLessThanSuma("internet", 301) == 3);
    assert(s.getSizeTipLessThanSuma("menaj", 851) == 3);
    assert(s.getSizeTipLessThanSuma("mancare", 750) == 0);
    assert(s.getSizeTipLessThanSuma("internet", 3457) == 5);
    assert(s.getSizeTipLessThanSuma("altele", 2100) == 0);





    //test getAllTip

    vector < Cheltuieli > a1 = s.getAllTip("menaj");
    vector < Cheltuieli > a2 = s.getAllTip("internet");
    vector < Cheltuieli > a3 = s.getAllTip("mancare");
    vector < Cheltuieli > a4 = s.getAllTip("haine");
    vector < Cheltuieli > a5 = s.getAllTip("altele");
    vector < Cheltuieli > a6 = s.getAllTip("transport");


    // s:
    // 21, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"

    assert(a1.size() == 4);
    assert(a2.size() == 6);
    assert(a3.size() == 1);
    assert(a4.size() == 0);
    assert(a5.size() == 0);
    assert(a6.size() == 1);




    //test getAllTipEqualSuma

    vector < Cheltuieli > s1 = s.getAllTipEqualSuma("menaj", 3450);
    vector < Cheltuieli > s2 = s.getAllTipEqualSuma("internet", 300);
    vector < Cheltuieli > s3 = s.getAllTipEqualSuma("mancare", 751);
    vector < Cheltuieli > s4 = s.getAllTipEqualSuma("haine", 200);
    vector < Cheltuieli > s5 = s.getAllTipEqualSuma("altele", 1000);
    vector < Cheltuieli > s6 = s.getAllTipEqualSuma("transport", 850);


    // s:
    // 21, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"

    assert(s1.size() == 1);
    assert(s2.size() == 3);
    assert(s3.size() == 0);
    assert(s4.size() == 0);
    assert(s5.size() == 0);
    assert(s6.size() == 1);




    //test getAllTipBiggerThanSuma

    vector < Cheltuieli > b1 = s.getAllTipBiggerThanSuma("menaj", 3450);
    vector < Cheltuieli > b2 = s.getAllTipBiggerThanSuma("internet", 300);
    vector < Cheltuieli > b3 = s.getAllTipBiggerThanSuma("mancare", 749);
    vector < Cheltuieli > b4 = s.getAllTipBiggerThanSuma("haine", 200);
    vector < Cheltuieli > b5 = s.getAllTipBiggerThanSuma("altele", 1000);
    vector < Cheltuieli > b6 = s.getAllTipBiggerThanSuma("transport", 850);


    // s:
    // 21, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"

    assert(b1.size() == 0);
    assert(b2.size() == 3);
    assert(b3.size() == 1);
    assert(b4.size() == 0);
    assert(b5.size() == 0);
    assert(b6.size() == 0);




    //test getAllTipLessThanSuma

    vector < Cheltuieli > l1 = s.getAllTipLessThanSuma("menaj", 3450);
    vector < Cheltuieli > l2 = s.getAllTipLessThanSuma("internet", 300);
    vector < Cheltuieli > l3 = s.getAllTipLessThanSuma("mancare", 751);
    vector < Cheltuieli > l4 = s.getAllTipLessThanSuma("haine", 200);
    vector < Cheltuieli > l5 = s.getAllTipLessThanSuma("altele", 1000);
    vector < Cheltuieli > l6 = s.getAllTipLessThanSuma("transport", 850);


    // s:
    // 21, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 21,21,"menaj" (today)
    // 14,650,"menaj"
    // 21,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"

    assert(l1.size() == 3);
    assert(l2.size() == 0);
    assert(l3.size() == 1);
    assert(l4.size() == 0);
    assert(l5.size() == 0);
    assert(l6.size() == 0);




    //test getAllZiDescr:

    // s:
    // 22, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 22,21,"menaj" (today)
    // 14,650,"menaj"
    // 22,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"


    int solutie1[1000], solutie2[1000], solutie3[1000], solutie4[1000];

    s.getAllZiDescr(22, solutie1);
    s.getAllZiDescr(14, solutie2);
    s.getAllZiDescr(1, solutie3);
    s.getAllZiDescr(12, solutie4);

    int noChelt1 = s.getSizeZi(22);
    int noChelt2 = s.getSizeZi(14);
    int noChelt3 = s.getSizeZi(1);
    int noChelt4 = s.getSizeZi(12);

    assert(noChelt1 == 3);
    assert(solutie1[0] == 300);
    assert(solutie1[1] == 300);
    assert(solutie1[2] == 21);

    assert(noChelt2 == 2);
    assert(solutie2[0] == 3450);
    assert(solutie2[1] == 650);

    assert(noChelt3 == 0);

    assert(noChelt4 == 1);
    assert(solutie4[0] == 850);




    //test getAllTipCresc:

    // s:
    // 22, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 22,21,"menaj" (today)
    // 14,650,"menaj"
    // 22,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"


    // 22 - 600
    //24 - 1700
    //21 - 3757


    int tip1[1000], tip2[1000], tip3[1000], tip4[1000];
    int noS1 = 0, noS2 = 0, noS3 = 0, noS4 = 0;

    s.getAllTipCresc("internet", tip1, noS1);
    s.getAllTipCresc("haine", tip2, noS2);
    s.getAllTipCresc("mancare", tip3, noS3);
    s.getAllTipCresc("menaj", tip4, noS4);


    assert(noS1 == 3);
    assert(tip1[0] == 600);
    assert(tip1[1] == 1700);
    assert(tip1[2] == 3757);

    assert(noS2 == 0);

    assert(noS3 == 1);
    assert(tip3[0] == 750);

    assert(noS4 == 3);
    assert(tip4[0] == 21);
    assert(tip4[1] == 850);
    assert(tip4[2] == 4100);




    //test getAllTipZiCresc:

    // s:
    // 22, 300,"internet" (today)
    // 14,3450,"menaj"
    // 24,850,"internet"
    // 22,21,"menaj" (today)
    // 14,650,"menaj"
    // 22,300,"internet" (today)
    // 15,750,"mancare"
    // 20,850,"transport"
    // 21, 300,"internet"
    // 12,850,"menaj"
    // 24,850,"internet"
    // 21,3457,"internet"


    int zi1[1000], zi2[1000], zi3[1000], zi4[1000];
    int ultim1 = s.getSizeTipZi("internet", 22);
    int ultim2 = s.getSizeTipZi("internet", 24);
    int ultim3 = s.getSizeTipZi("haine", 12);
    int ultim4 = s.getSizeTipZi("menaj", 12);

    s.getAllTipZiCresc("internet", 22, zi1);
    s.getAllTipZiCresc("internet", 24, zi2);
    s.getAllTipZiCresc("haine", 12, zi3);
    s.getAllTipZiCresc("menaj", 12, zi4);


    assert(ultim1 == 2);
    assert(zi1[0] == 300);
    assert(zi1[1] == 300);

    assert(ultim2 == 2);
    assert(zi2[0] == 850);
    assert(zi2[1] == 850);

    assert(ultim3 == 0);

    assert(ultim4 == 1);
    assert(zi4[0] == 850);

}

