//
// Created by himan on 31-07-2024.
//
#include <graphics.h>
#include <iostream>
using namespace std;

int main() {
    initwindow(1920, 1080);
//    int gd = DETECT, gm;
//    initgraph(&gd, &gm, "");
    int x1 = 200, y1 = 332, x2 = 754, y2 = 936;
    int delx = x2 - x1, dely = y2 - y1;
    int tdelx = 2 * delx, tdely = 2 * dely;
    int idp = tdely - delx;
    int noofsteps = max(delx, dely);
    cout << x1 << "," << y1 << "," << x2 << "," << y2 << "," << delx << "," << dely << "," << noofsteps << "," << tdelx
         << "," << tdely << "," << idp << "," << endl;
    int incfacp = tdely - tdelx;
    int incfacn = tdely;
    int x = 0;
    while (x < noofsteps + 1) {
        if (idp > 0) {
            cout << x1 << "," << y1 << "," << endl;
            putpixel(x1, y1, WHITE);
            x1++;
            y1++;
            idp = idp + incfacp;
            cout << idp << "," << endl;
        } else {
            cout << x1 << "," << y1 << endl;
            putpixel(x1, y1, WHITE);
            x1++;
            idp = idp + incfacn;
            cout << idp << "," << endl;
        }
        x++;
    }
    int x3 = 500, y3 = 232, x4 = 1054, y4 = 836;
    line(x3, y3, x4, y4);
    getch();
    closegraph();
}