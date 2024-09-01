#include <graphics.h>

main ()
{	
	initwindow(1000,1000);	
//	setcolor(RED);	
	circle(500,500,400);
	circle(350,350,100);
	circle(650,350,100);
	
	line(500,400,450,550);
	line(500,400,550,550);
	line(450,550,550,550);
	
	line(275,600,500,750);	
	line(500,750,700,600);	
		
	getch();	
	
}
