// Implementing basic OOPs concept to get familiar with CPP

#include <iostream>
using namespace std;

class Contract{
  virtual string getPromotion() = 0;
};

class Person: Contract{
  string Name;
  string Characteristics;
  int Age;
  float Salary;

public:
  Person(string name, string character, int age, float salary){
    Name = name;
    Characteristics = character;
    Age = age;
    Salary = salary;
  }

  string getPromotion(){
    int character = Characteristics.compare("Smart");
    if ( character == 0 && (Age >= 25 || Salary < 5000.00)){
      return (Name + "gets a promotion!");
    }
    return (Name + " does not get a promotion!");
  }

  void getter(){
    cout << Name << '\n';
    cout << Characteristics << '\n';
    cout << Age << '\n';
    cout << Salary << '\n';
  }
};

int main(){
  Person p1 = Person("Ujjwal", "Timid", 21, 4500.99);
  p1.getter();
  cout << '\n' << p1.getPromotion();
}