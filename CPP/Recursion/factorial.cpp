#include <iostream>
using namespace std;

int factorial(int number){
  if (number <= 0)
    return 1;
  
  return (number*factorial(number-1));
}

int main(){
  int number = 0;
  cout << "Please enter a number: "; 
  cin >> number;
  if (number < 0){
    cout << endl << "Please enter a whole number: ";
    cin >> number;
  }
  cout << endl << "Factorial of that number is: " << factorial(number) << endl;
  return 0; 
}