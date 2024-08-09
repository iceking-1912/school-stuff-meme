#include <graphics.h>

void mpcda(int xc,int yc,int rad){
	int x,y,idp;
	idp = (1-rad);
	x = 0;
	y = rad;
	while (x!=y){
		if (idp < 0){
			idp += (2*x+1);
			delay(50);
					}
		else{
			y -= 1;
			idp += (2*(x-y)+1);
			}			
		x += 1;
		putpixel(x+xc,y+yc,WHITE);
		putpixel(-x+xc, y+yc,WHITE);
		putpixel(x+xc, -y+yc,WHITE);
		putpixel(-x+xc, -y+yc,WHITE);
		putpixel(y+xc, x+yc,WHITE);
		putpixel(-y+xc, x+yc,WHITE);
		putpixel(y+xc, -x+yc,WHITE);
		putpixel(-y+xc, -x+yc,WHITE);
				}
}


void bcdal(int xc,int yc,int rad){
	int x,y,idp;
	idp = (3-2*rad);
	x = 0;
	y = rad;
	while (x!=y){
		x += 1;
		if (idp < 0){
			idp = idp + (4*x+6);
			delay(50);
					}
		else{
			y = y-1;
			idp=idp +(4*(x-y)+10);
			}			
		putpixel(x+xc,y+yc,WHITE);
		putpixel(-x+xc, y+yc,WHITE);
		putpixel(x+xc, -y+yc,WHITE);
		putpixel(-x+xc, -y+yc,WHITE);
		putpixel(y+xc, x+yc,WHITE);
		putpixel(-y+xc, x+yc,WHITE);
		putpixel(y+xc, -x+yc,WHITE);
		putpixel(-y+xc, -x+yc,WHITE);
				}
}

int main(){
	initwindow(1000,1000);
	int xc1,yc1,r1;
	xc1 = 500;
	yc1 = 500;
	r1 = 100;
	mpcda(xc1,yc1,r1);
	int xc2,yc2,r2;
	xc2 = 750;
	yc2 = 750;
	r2 =100;
	bcdal(xc2,yc2,r2);
	getch();
}
		
	
