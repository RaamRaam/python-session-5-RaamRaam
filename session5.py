import random
from operator import itemgetter



def create_deck_using_lambda_zip_map(vals: 'face values as List[String]', suits: 'classes as List[String]') -> 'Deck as List[String]':
    '''
    creates a deck of cards
    Input: 
        vals: ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        suits: ['spades', 'clubs', 'hearts', 'diamonds']    
        lists and not sets.  set orders the values
    Return:
        The deck in order (not sorted nor shuffled)
    Note: 
        forced to use map, lambda and zip 
    '''
    if not (vals and suits):
        raise ValueError('Empty lists.  please provide values for cartesian product')        
    else:
        return list(map(lambda i: suits[i[0]]+'-'+vals[i[1]],list(zip(sorted(list(range(len(suits)))*len(vals)),list(range(len(vals)))*len(suits)))))    

def create_deck_using_list_comprehension(vals: 'face values as List[String]', suits: 'classes as List[String]') -> 'Deck as List[String]':
    '''
    creates a deck of cards
    Input: 
        vals: ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        suits: ['spades', 'clubs', 'hearts', 'diamonds']    
        lists and not sets.  set orders the values
    Return:
        The deck in order (not sorted nor shuffled)
    Note: 
        Used comprehension to create the deck
    '''
    if not (vals and suits):
        raise ValueError('Empty lists.  please provide values for cartesian product')        
    else:
        return [i+'-'+j for i in suits for j in vals]


def deal(no_of_decks: int,no_of_players: int,no_of_cards: int)->'Dealt Cards for each player':
    '''
    deals the decks(depending on number of decks) to number of players and number of cards per player
    Input: 
        no_of_decks: number of decks
        no_of_players: number of players
        no_of_cards: number of cards per player
    process:
        creates cards list based on number of decks, shuffle, distributes to players so as not to affect probability
    Return:
        list of cards for each of player
    Note: 
        used list instead of sets, because sets would not allow duplicates in case of more than one deck
    '''
    if no_of_cards<=0 or no_of_decks<=0 or no_of_players<=1:
        raise ValueError('Please enter valid values for no_of_card, no_of_decks, no_of_players')        
    else:
        vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        cards=create_deck_using_list_comprehension(vals, suits)
        cards=cards * no_of_decks
        random.shuffle(cards)
        return [list((itemgetter(*list(range(i,no_of_players*no_of_cards,2)))(cards))) for i in range(no_of_players)]

def decider(hand1: 'Dealt cards to Player 1 as List[String]',hand2: 'Dealt cards to Player 2 as List[String]')->'winner':
    '''
    Decides the winner
    Input: 
        hand1: Cards with player 1
        hand2: Cards with player 2
    process:
        Ranks the card combination with each of the player
    Return:
        hand, Winner depending on rank (lower the rank, the player is winner) and the reason
    Note: 
        Hardcoded for two players.  Can be generalized
    '''
    
    if not (hand1 and hand2):
        raise ValueError('Please enter valid hands for players')        
    else:
        combination={1:'Royal Flush', 2:'Straight Flush', 3:'Four of a Kind', 4:'Full House', 5:'Flush', 6:'Straight', 7:'Three of a Kind', 8:'Two Pair', 9:'One Pair', 10:'High Card'}

        a=get_rank(hand1)
        b=get_rank(hand2)
        game={'Player 1': [hand1,combination[a]],'Player 2': [hand2,combination[b]]}
        
        if a==b:
            return (game,'no clear winner')
        elif a>b:
            return (game,'Player2 is winner')
        else:
            return (game,'Player1 is winner')
    
def get_rank(hand: 'hand of cards with player as List[String]')->'Rank':
    '''
    Ranks the card combination
    Input: 
        hand: Cards with player
    process:
        Ranks the card combination with each of the player
        Ranking logic in order
        if same suit, consecutive starting with ace, rank 1
        if same suit, consecutive not starting with ace, rank 2
        if same suit, not consecutive (all unique since hard coded for one deck), rank 5
        if not same suit, but consecutive, rank 6
        if all cards have unique face value, rank 10
        if only 2 face values and one of them appears only once, rank 3
        if only 2 face values, rank 4
        if a face value appears thrice, rank 7
        if 2 face values appears twice, rank 8
        if 1 face value appears twice, rank 9
        
    Return:
        Rank
    '''
    if not hand:
        raise ValueError('Please enter valid hands for players')        
    else:
        repl_dict={'jack':11,'queen':12,'king':13,'ace':14}
        hand_suits=[i.split('-')[0] for i in hand]
        hand_vals=sorted([repl_dict[i.split('-')[1]] if i.split('-')[1] in repl_dict.keys() else int(i.split('-')[1]) for i in hand])
        same_suit = [hand_suits[0]]*len(hand_suits)==hand_suits
        consecutive = [j-i for i, j in zip(hand_vals[:-1], hand_vals[1:])] == [1] * (len(hand_vals)-1)
        if same_suit:
            if consecutive:
                if hand_vals[-1]==14:
                    return 1
                else:
                    return 2
            else:
                return 5
        else:
            if consecutive:
                return 6
            
        freq=list({i:hand_vals.count(i) for i in hand_vals}.values())
        if freq==[1]*len(hand_vals):
            return 10
        elif len(freq)==2 and 1 in freq:
            return 3
        elif len(freq)==2:
            return 4
        elif 3 in freq:
            return 7
        elif 2 in freq and freq.count(2)==2:
            return 8
        elif 2 in freq:
            return 9
        

    
if __name__ == '__main__':
    hands=deal(2,2,5)       
    print(decider(hands[0],hands[1]))
    