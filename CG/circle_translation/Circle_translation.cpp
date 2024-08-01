#include <graphics.h>

main(){
	initwindow(1000,1000);
//	int x = 100,y = 100;
//	
//	for (int i;i<1000;i++)
//	{
//		circle(x+i,y+i,50);
//		delay(5);
//		cleardevice();
//		}	
//	
//	getch();
//	int x = 100,y = 100;
//	
//	for (int i;i<1000;i++)
//	{
//		circle(x+i,y,50);
//		delay(5);
//		cleardevice();
//		}	
//	
//	getch();
	int x = 100,y = 100;
	
	for (int i;i<1000;i++)
	{
		circle(x,y+i,50);
		delay(5);
		cleardevice();
		}	
	
	getch();	
	
}
