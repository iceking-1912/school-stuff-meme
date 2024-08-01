/*
 * Assignment Statement:
Implement a class Complex which represents the Complex Number data type.
Implement the following:
1. Constructor (including a default constructor which creates the complex number 0+0i).
2. Overload operator+ to add two complex numbers.
3. Overload operator* to multiply two complex numbers.
4. Overload operators << and >> to print and read Complex Numbers.
*/

//CODE SOLUTION:
#include <iostream>
using namespace std;

class complex {
private:
    int real;
    int img;
public:
    string name;

    complex() {
        real = 0;
        img = 0;
    }

    complex(int a, int b,string n = "c") {
        real = a;
        img = b;
        name = n;
    }

    void show() {
        cout << "Complex number"<<name<< " is: ";
        cout << real << "+" << img << "i" << endl;/.mcbk
    }
    complex operator+ (const complex& oc) const {
        complex tempc;
        tempc.real = real + oc.real;
        tempc.img = img + oc.img;
        return tempc;
    }
    complex operator*( const complex& oc) const {
        complex tempc;
        tempc.real = real * oc.real - img * oc.img;
        tempc.img = real * oc.img + img * oc.real;
        return tempc;
    }
    complex operator<< (const complex& oc ) const{

    }
    friend ostream& operator<<(ostream& os, const complex& oc){
        os << oc.real << "+"<< oc.img<< "i" << endl;
        return os;
    }
    friend istream& operator>>(istream& is,complex& oc){
        is >> oc.real >>oc.img;
        return is;
    }
};

int main() {
    complex c,c1(100,5), c2(10, 20),c3,c4;
    c1.show();
    c2.show();
    c3 = c1 +c2;
    c3.show();
    c4 = c1 * c2;
    cout << c4;
    cout << "Enter real and img part for c complex number: ";
    cin >> c;
    c.show();
}