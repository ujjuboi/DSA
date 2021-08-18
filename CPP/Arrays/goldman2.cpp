// The problem can be found here: https://prepinsta.com/goldman-sachs/technical-test/coding-questions/

#include<iostream>
using namespace std;

int lossCalc(int size, int arr[]){
  int loss = 0;
  // For loop to iterate in the array:
  for (int i=0; i<size; i++){
    // for loop to iterate after selecting one element (i) from the previous for loop
    // this checks for all consecutive prices:
    for (int j = i+1; j<size; j++){
      // if the price consecutive to i is greater then break 
      if (arr[i] < arr[j])
        continue;
      else if ((arr[i] - arr[j]) > loss)
        loss = arr[i] - arr[j];
    }
  }
  return loss;
}

int main(){
  int size = 7;
  int arr[size] = {1,8,4,2,10,3,2};
  cout << "The stock prices are: ";
  for (int i=0; i<size; i++)
    cout << arr[i] << " ";
  cout << endl << "The loss is: " << lossCalc(size, arr);
  return 0;
}