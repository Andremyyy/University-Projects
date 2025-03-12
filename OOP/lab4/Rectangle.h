//
// Created by ema_a on 3/18/2024.
//

#ifndef LAB4_RECTANGLE_H
#define LAB4_RECTANGLE_H


class Rectangle {
private:
    int x1;
    int x2;
    int y1;
    int y2;
public:

    // constructori:
    Rectangle(); //implicit

    Rectangle(int a, int b, int c, int d); // general

    Rectangle(const Rectangle &r); // de copiere

    //getteri:

    int getx1();

    int getx2();

    int gety1();

    int gety2();

    //deconstructor:

    ~Rectangle();

    //setteri:

    void setX1(int a);

    void setX2(int a);

    void setY1(int a);

    void setY2(int a);

    //metode:

    int detAria();

    double detSRA();

    // Suprascrierea operatorului ==
    bool operator == (const Rectangle& other)  {
        // Două dreptunghiuri sunt considerate egale dacă au aceleași coordonate
        return x1 == other.x1 && y1 == other.y1 && x2 == other.x2 && y2 == other.y2;
    }
};


#endif //LAB4_RECTANGLE_H
