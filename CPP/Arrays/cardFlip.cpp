/*
I encountered this problem in a placement test. It was fairly easy but I could not complete it back then becuase my mind was not working back then. I could not find this problem on the net so I going to try to explain it to the best of my knowledge:

Suppose I have a deck of cards. On the front side of each of the cards, numbers are printed from 1 to 9 & on the back of each card numbers are printed -1 to -9. I shuffle the deck thoroughly. Then I randomly flip cards in the deck itself so that some cards are facing down and some cards are facing up. Then I select at random 5 cards from the deck. Hence some cards will show negative numbers whereas some will show positive. I can flip simultaneous cards which are facing down (change negative to positive). My goal is to find the highest sum of the 5 numbers. A test case is given below: 

I have a list of these 5 cards selected: [1, -5, 9, -2, -8]

Now I can flip the cards that are facing backwards but, they have to be consecutive to each other. Like I can flip -5 but then I cant flip -2 or -8 because they do not come directly after -5, 2 is in the way. So, if I flip -5, then the sum of the list would be 5 but, if I flip -2 and then its consecutive card -8, we get 15 which the highest sum possible. This is the game.

One more test case is that if I have an array like this: [-1, 5, 9, -2, -8], I can flip -2, -8 & -1. Hence I move in circles in the list.

Future Prospects: If the problem is solved, I can make the size of the array variable and then solve the problem.
*/

// Learning OOPs & pointers in cpp for now:

#include <iostream>
using namespace std;

class CardFlip{
  public:
    int arr[5], size;
};
CardFlip deck;

int main(){

  return 0;
}