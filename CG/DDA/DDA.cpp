#include <graphics.h>
#include <iostream>

/*DDA ALGO
            start
    X1 Y1
    X2 Y2
    Delta X = X2 -X1
    Delta Y = Y2 - Y1
    Incval = max( Delta X, Delta Y)
    Xinc = delta X / incval
    Yinc = delta Y / incval
    N=0
    Cordset = {(X1,Y1),(X1+n(Xinc),Y1+n(Yinc)),
               (X1+(n+1)(Xinc),Y1+(n+1)(Yinc)),(till n+7)(X2,Y2)}
            (Can also use for or while loop)
    Stop*/


int main() {

    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    
    int x1=123,x2=850,y1=150,y2=750;
    int delx = x2 - x1;
    int dely = y2-y1;
    int incval = 0;
    if (delx > dely) {
        incval = delx;
    }
    else (dely > delx)
                ;{
        incval = dely;
    };
    int xinc = delx / incval;
    int yinc = dely / incval;
    xinc = abs(xinc);
	yinc = abs(yinc);
    for (int i = 0; i <incval;i++)
    {
        putpixel(x1, y1, WHITE);
        x1 = x1 + xinc;
        y1 = y1 + yinc;
    }
    getch();
    closegraph();
    return 0;
}

