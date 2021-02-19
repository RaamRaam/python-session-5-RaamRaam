**# Session 5 - Assignment 2 solutions are in Assignment2.ipynb**

**# Session 5 - Assignment 1 solutions are in session5.py and test_session5.py**



The task is to deal cards to players and determine winner in basic poker. The inputs are number of decks in set, number of players, number of cards per player and card combination for each of the player



**## The session5.py has the following**



1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts



  function: # create_deck_using_lambda_zip_map



  input: (vals: 'face values as List[String]', suits: 'classes as List[String]') 



  output: Deck as List[String]



  



2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts



  function: # create_deck_using_list_comprehension



  input: (vals: 'face values as List[String]', suits: 'classes as List[String]') 



  output: Deck as List[String]



  



3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the [game of poker (Links to an external site.)](https://i.pinimg.com/474x/6b/1f/f7/6b1ff73716c14139c951241f3c1d7c46.jpg)! - 150 pts



  function: # deal (called from main function)



  input: (no_of_decks: int,no_of_players: int,no_of_cards: int)



  output: Dealt Cards for each player



  



  function: # get_rank (called from decider)



  input: (hand: 'hand of cards with player as List[String]')



  output: Rank



  

  function: # decider (calls get_rank)



  input: (hand1: 'Dealt cards to Player 1 as List[String]',hand2: 'Dealt cards to Player 2 as List[String]') 



  output: winner



4. Main Function calls in following order



   hands=deal(2, 2, 5)   



   print(decider(hands[0],hands[1]))



**## test_session5.py has the test cases**