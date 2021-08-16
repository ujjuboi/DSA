// Implementing basic OOPs concept to get familiar with CPP

#include <iostream>
using namespace std;

class Contract{
  virtual string getPromotion() = 0;
};

class Employee: Contract{
protected:
  string Name;
  string Characteristics;
  int Age;
  float Salary;

public:

  string getPromotion(){
    int character = Characteristics.compare("Smart");
    if ( character == 0 && (Age >= 25 || Salary < 5000.00)){
      return (Name + "gets a promotion!");
    }
    return (Name + " does not get a promotion!");
  }

  void getter(){
    cout << Name << " is " << Characteristics << ". " << Age << " years old & is earning " << Salary << " ";
  }

  virtual void work(){
    cout << Name << " is doing the assinged work!" << endl;
  }
};

class Developer : public Employee{

  string Language;

public:
  Developer(string name, string character, int age, float salary, string language){
    Name = name;
    Characteristics = character;
    Age = age;
    Salary = salary;
    Language = language;
  }

  void work(){
    cout << Name << " is implementing the project using " << Language <<endl;
  }
};

class Analyst: public Employee{

  int Level;

public:
  Analyst(string name, string character, int age, float salary, int level){
    Name = name;
    Characteristics = character;
    Age = age;
    Salary = salary;
    Level = level;
  }

  void who(){
    getter();
    cout << "he is on level: " << Level << endl;
  }
};

int main(){
  Developer d = Developer("Ujjwal", "Timid", 21, 4500.99, "Python");
  Analyst a = Analyst("Sharma", "Smart", 28, 5000.25, 4);

  Employee* e1 = &d;
  Employee* e2 = &a;

  e1->work();
  e2->work();
  cout << e1->getPromotion() << endl;
  cout << e2->getPromotion() << endl;
  a.who();
}