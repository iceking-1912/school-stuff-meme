#include<iostream> 
#include<string.h> 
using namespace std; 
class stackop 
{ char st[20],st1[20]; int top,top1,ss[10],e1,e2,e3,flag; 
 public: 
 void input(); 
 void push(char a); 
 void pop(); 
 int pri(char b); 
 void eval(); 
 void push1(int d); 
 void pop1(); 
 }; 
 int stackop::pri(char b) 
 { if(b=='-') 
 return 1; 
 if(b=='+') 
 return 2; 
 if(b=='/') 
 return 3; 
 if(b=='*') 
 return 4; 
 } 
 
void stackop::input() 
{ char ch[20]; top=-1; int f=1,l,i=0,j=0; flag=0; 
 cout<<"\n enter the expression\n"; 
 cin>>ch; 
 l=strlen(ch); 
 
 
 
 while(i<l) 
 { f=1; 
 if(isalpha(ch[i])) 
 { cout<<ch[i]; st1[j]=ch[i]; j++; flag=1; } 
 if(isdigit(ch[i])) 
 { cout<<ch[i]; st1[j]=ch[i]; j++; } 
 if(ch[i]=='(') 
 { push(ch[i]); } 
 if(ch[i]==')') 
 { 
 while(st[top]!='(') 
 { cout<<st[top]; st1[j]=st[top]; j++; pop();} 
 pop(); 
 } 
 if((ch[i]=='+')||(ch[i]=='-')||(ch[i]=='*')||(ch[i]=='/')) 
 { while(f==1) 
 { 
 if(top==-1) 
 { push(ch[i]); f=0; } 
 else 
 { if(st[top]=='(') 
 { push(ch[i]); f=0; } 
 else 
 { 
 if((pri(ch[i]))>(pri(st[top]))) 
 { push(ch[i]); f=0; } 
 else 
 { cout<<st[top]; st1[j]=st[top]; j++; 
pop(); } 
 
 } 
 } 
 } 
 } 
 i++; 
 } 
 while(top!=-1) 
 { cout<<st[top]; st1[j]=st[top]; j++; pop(); } cout<<"\n"; 
 cout<<st1; 
} 
void stackop::eval() 
{ int j=0; top1=-1; 
 if(flag==0) 
{ 
 while(j<strlen(st1)) 
{ 
 if(st1[j]=='1') 
 push1(1); 
if(st1[j]=='2') 
 push1(2); 
if(st1[j]=='3') 
 push1(3); 
if(st1[j]=='4') 
 push1(4); 
if(st1[j]=='5') 
 push1(5); 
if(st1[j]=='6') 
 push1(6); 
if(st1[j]=='7') 
 push1(7); 
if(st1[j]=='8') 
 push1(8); 
if(st1[j]=='9') 
 push1(9); 
if(st1[j]=='0') 
 push1(0); 
if(st1[j]=='+') 
{ e1=ss[top1]; pop1(); 
 e2=ss[top1]; pop1(); 
 e3=e2+e1; 
 push1(e3); 
} 
if(st1[j]=='-') 
 { e1=ss[top1]; pop1(); 
 e2=ss[top1]; pop1(); 
 e3=e2-e1; 
 push1(e3); 
} 
 
if(st1[j]=='*') 
{ e1=ss[top1]; pop1(); 
 e2=ss[top1]; pop1(); 
 e3=e2*e1; 
 push1(e3); 
} 
if(st1[j]=='/') 
{ e1=ss[top1]; pop1(); 
 e2=ss[top1]; pop1(); 
 e3=e2/e1; 
 push1(e3); 
} j++; 
} 
cout<<"\n evaluated value:"; 
cout<<ss[0]; 
} 
else 
{ cout<<"\n cannot evaluate given input"; 
} 
} 
void stackop::push(char a) 
{ top++; st[top]=a; } 
void stackop::pop() 
{ top--; } 
void stackop::push1(int d) 
{ top1++; ss[top1]=d; } 
void stackop::pop1() 
{ top1--; } 
int main() 
{ stackop s; 
 s.input(); 
 s.eval(); 
 cout<<"\n"; 
 return 0; 
} 
