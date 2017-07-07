#include <iostream>
#include "Student.h"
using namespace std;

int main() {
  cout << "Hello, world!" << endl;
  Student st1();
  Student st2("Rick James", 40);
  cout << st2.getName() << endl;
}
