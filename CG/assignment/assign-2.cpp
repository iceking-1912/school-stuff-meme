
#include <iostream>
#include <graphics.h>
using namespace std;


struct p{
    int x,y;
};

int m_abs(double num) {
    if (num < 0) {
        num = -num;
    }
    int roundedValue = static_cast<int>(num + 0.5);
    return roundedValue;
}

void DDA_l(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;

    int steps;
    if (m_abs(dx) > m_abs(dy))
        steps = m_abs(dx);
    else
        steps = m_abs(dy);

    float Xinc = dx / (float) steps;
    float Yinc = dy / (float) steps;

    float x = x1;
    float y = y1;

    for (int i = 0; i <= steps; i++) {
        putpixel(x, y, WHITE);
        x += Xinc;
        y += Yinc;
    }
}


class loop_square {
private:

public:
    p a[];

    void setter(p x[],int n) {
        for (int z = 0; z < n; z++) {
            a[z] = x[z];
        }

    };

    void show_cord(int n ,p co[] = nullptr) {
        if (co == nullptr) {
            co = a;
        }
        for (int x = 0; x < n; x++) {
            cout << "(" << co[x].x << ", " << co[x].y << ")" << endl;
        }
    }

    void draw_poly(int n,p ax[] = nullptr) {
        if (ax == nullptr) {
            ax = a;
        }
        for (int i = 0; i < n; i++) {
            DDA_l(ax[i].x, ax[i].y, ax[(i + 1) %n].x, ax[(i + 1) % n].y);
        }
    };

    p midp_fin(p p1, p p2) {
        p mid;
        mid.x = (p1.x + p2.x) / 2;
        mid.y = (p1.y + p2.y) / 2;
        return mid;
    }

    void p_gen(p p1[], p p2[], int n) {
        for (int i = 0; i < n; i++) {
            p2[i] = midp_fin(p1[i], p1[(i + 1) % n]);
        }
    }

    void p_up(p p1[], p p2[], int n) {
        for (int j = 0; j < n; j++) {
            p1[j] = p2[j];
        }
    }
    void call(p pi[],int n){

        p temp[n];
        setter(pi,n);
        show_cord(n);
        draw_poly(n,pi);
        for (int i = 0; i < 10; i++) {
            draw_poly(n,pi);
            p_gen(pi, temp, n);
            p_up(pi, temp, n);
            delay(250);
        }
    }
};

int main() {
    initwindow(1920, 1080);
    loop_square s1,s2,s3;
    int a = 5;
    p pfi[5] = {{200, 100},
                {300, 200},
                {250, 300},
                {150, 300},
                {100, 200}};
    s1.call(pfi,a);
    int n = 4;
    p pf[4] = {{700, 600},
               {950, 600},
               {950, 850},
               {700, 850}};
    s2.call(pf,n);
    int z = 3;
    p pt[3] = {{1600, 200},
               {1400, 500},
               {1800, 500}};
    s3.call(pt,z);
    getch();
    return 0;
}
