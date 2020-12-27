'''
Created on Sep 20, 2020

@author: Maria
'''

from Player import Player
from Deck import Deck
from Card import Card
from Actions import Action
import string
import random
import math
from importlib.resources import path




global attack
attack = [0]
global current_player
current_player = [0]
global action_cards
##### DIFFUSE AND NOPE NOT IN BECUASE SPECIAL CASE
action_cards = {"draw", "attack", "skip", "favor", "see the future", "shuffle"}
actions = ["diffuse", "nope", "attack", "favor", "see the future", "skip", "shuffle", "match 2", "match 3", "different", "draw"]

################# PASS IN LIST FROM 1:
def init_player(l: list):
    out = Player()
    out.hand = l
    return out

def init_deck(l: list):
    return Deck(l)

def init_commands(l: list):
    out = []
    #print(l)
    intermediate = []
    mult = False
    for item in l:
        if item[0] == '[':
            mult = True
            item = item[1:]
            #print("start")
        if mult:
            if item[-1] != ']':
                intermediate.append(int(item))
            else:
                intermediate.append(int(item[:-1]))
        else:
            out.append(int(item))
        if item[-1] == ']':
            mult = False
            out.append(intermediate)
    return out

def init_indices(l: list):
    out = []
    for item in l:
        out.append(int(item))
    return out

inits = {"Player": init_player,
         "Deck": init_deck,
         "Commands": init_commands,
         "NumCards": init_indices,
         "Discard": init_deck}


def get_mult_inputs(p: path):
    out = []
    test = open(p, 'r+')
    temp = []
    for line in test.readlines():
        
        ### MAKE INTO PARSABLE LIST SO CAN HAVE MULTIPLE INPUTS
        
        if line.split(",")[0] == "\n":
            out.append(temp)
            temp = []
        else:
            item = line.strip("\n").split(", ")
            temp.append(item)
    return out


def get_mult_inputs_output(p: path):
    out = []
    test = open(p, 'r+')
    temp = []
    for line in test.readlines():
        if line.split(",")[0] == "Discard":
            temp.append(line.strip("\n").split(", "))
            out.append(temp)
            temp = []
        else:
            item = line.strip("\n").split(", ")
            temp.append(item)
    return out

### [players, deck, commands, indices, discard]
def init_items(commands: list):
    out = []
    for item in commands:
        temp = []
        players = []
        coms = []
        inds = []
        discard = []
        for element in item:
            if element[0] == "Player":
                players.append(inits[element[0]](element[1:]))
            elif element[0] == "Commands":
                coms.append(inits[element[0]](element[1:]))
            elif element[0] == "Deck":
                temp.append(players)
                temp.append(inits[element[0]](element[1:]))
            elif element[0] == "Discard":
                discard.append(inits[element[0]](element[1:]))
        temp.append(coms)
        temp.append(inds)
        if len(discard) != 0:
            temp.append(discard[0])
        else:
            temp.append(Deck({}))
        out.append(temp)
                
    '''
            OUT PARAMETERS:
            players list,
            deck (deck type),
            commands (list of commands list),
            discard pile
    
    '''
    return out


def init_items_output(commands: list):
    out = []
    for item in commands:
        temp = []
        players = []
        for element in item:
            if element[0] == "Player":
                players.append(inits[element[0]](element[1:]))
            if element[0] == "Deck":
                temp.append(players)
            if element[0] != "Player":
                temp.append(inits[element[0]](element[1:]))
        out.append(temp)
    return out


def check_single(played_cards: list, action_cards: set):
    if played_cards[0] in action_cards:
        return played_cards[0]
    return "invalid"

def check_match(played_cards: list, action_cards: set):
    temp = played_cards[0]
    print(temp)
    for card in played_cards:
        if card != temp:
            return "invalid"
    return "match " + str(len(played_cards))

def check_diff(played_cards: list, action_cards: set):
    temp = []
    for card in played_cards:
        if card in temp:
            return "invalid"
        temp.append(card)
    return "different"
    
def check_valid(played_cards: list, action_cards: set):
    length_lookup = {1: check_single, 2: check_match, 3: check_match, 5: check_diff}
    return length_lookup[len(played_cards)](played_cards, action_cards)
        
def attack_continue():
    global attack
    if attack[0] > 0:
        return True
    return False
    
'''
gets index, played card, and transformation of played card(s) for the player
return list of
    indices = indices for player
    played = card played
    played_action = transformation of played into what to play
'''
def get_played(players: list, current_player: list, action_list: list):
    inds = []
    played = []
    if type(action_list[current_player[0]][0]) == int:
        played.append(players[current_player[0]].hand[action_list[current_player[0]][0]])
        inds.append(action_list[current_player[0]][0])
    else:
        for i in action_list[current_player[0]][0]:
            played.append(players[current_player[0]].hand[i])
            inds.append(i)
    played_action = check_valid(played, action_cards)
    
    return [inds, played, played_action]


def increment(current_player: list, players: list, attack_decrement: bool):
    global attack
    if attack[0] > 0 and attack_decrement:
        attack[0] = attack[0] - 1
    elif current_player[0] == len(players)-1:
        current_player[0] = 0
    else:
        current_player[0] = current_player[0] + 1
        
        
### deck = deck
### discard_pile = discard
### players = player list
### current_player = global current_player
### action_list = commands
### inds = indices of inputs required

### FOR TEST CASES, RETURN STATE OF THE GAME
### RETURN EACH PARAMETER'S CURRENT STATE TO ALLOW FOR COMAPRISON TESTING
### INSERT KITTEN INTO CERTAIN SPOT FOR TESTING PURPOSES


def play_card(deck: Deck, discard_pile: Deck, players: list, current_player: list, action_list: list, inds: list):###, num_cards: list):
    global action_cards
    count = 0
    global attack
    num_turns = 0
    print("action list: ", end = "")
    print(action_list)
    #print("inds: ", end = "")
    #print(inds)
    while num_turns > 1 or len(players) > 1:
        if(len(action_list[current_player[0]]) == 0):
            return
        while(len(action_list[current_player[0]]) > 0):
            ###### INSTEAD OF FOR LOOP, GO UNTIL DRAW
            ###### KEEP DRAW IN INDEX 0 AND JUST USE THAT AS INPUT
            ###### TO DRAW CARD
            
            played = get_played(players, current_player, action_list)
            action_list[current_player[0]].pop(0)
            attack_decrement = False if attack[0] == 0 else True
            if played[2] == "invalid":
                print("PLAYED2 INVALID")
                print("invalid")
            else:
                ### Execute action
                action = Action()
                print("inds: ", end = "")
                print(inds)
                action.action(deck, current_player, players, attack, played[2], discard_pile, inds)
                if played[1][0] == "draw":
                    break
                players[current_player[0]].remove_played(played[0])
                discard_pile.push(played[2])
                if played[1][0] == "attack":
                    attack_decrement = False
                    break
            
        ''' debug:
        print(action_list[current_player[0]])
        deck.print()
        players[0].print()
        discard_pile.print()
        players[0].print()'''
        
        ### for testing
        #increment(current_player, players, attack_decrement)
        #num_turns = num_turns + 1
           
                    
def test_mult_cases(test_cases: list, inds_list: list):
    global current_player
    global attack

    for item in range(len(test_cases)):
        print("TEST " + str(item))
        current_player = [0]
        attack = [0]
        inds_list[item].pop(0)
        play_card(test_cases[item][1], test_cases[item][4], test_cases[item][0], current_player, test_cases[item][2], inds_list[item])#, test_cases[item][3])
        print()
        
### execute_states - state after finishes executing
### final_states - inputted states that is from final state file
### test - test number
def compare_one_state(execute_states: list, final_states: list, test: int):
    valid = True
    message = ""
    for item in range(len(execute_states[0])):
        if execute_states[0][item] != final_states[0][item]:
            message = "FAILED - "
            execute_states[0][item].print()
            final_states[0][item].print()
            print()
            reason = ": invalid player hand"
            valid = False
    if execute_states[1] != final_states[1]:
        message = "FAILED - "
        execute_states[1].print()
        final_states[1].print()
        reason = ": invalid deck"
        valid = False
    if execute_states[4] != final_states[4]:
        message = "FAILED - "
        execute_states[4].print()
        final_states[4].print()
        reason = ": invalid discard"
        valid = False
    if valid:
        message = "PASSED - "
    message = message + "test number " + str(test)
    if not valid:
        message = message + reason
    print(message)
    return valid

def compare_all_states(execute_states: list, final_states: list):
    for state in range(len(execute_states)):
        compare_one_state(execute_states[state], final_states[state], state)

def parse_inputs(file_path: string):
    test = open(file_path, 'r+')
    temp = []
    for line in test.readlines():
        item = line.strip("\n").split(", ")
        test_split = item[0].split(":")
        item[0] = test_split[0]
        item.insert(1, test_split[1].strip())
        temp.append(item)
    out = temp
    return out

if __name__ == "__main__":
    in_file = "/Users/Maria/Desktop/Exploding Kittens/MultipleTests3.txt"
    fin_states = "/Users/Maria/Desktop/Exploding Kittens/OutputStates.txt"
    index_inputs = "/Users/Maria/Desktop/Exploding Kittens/AutomatedIndexInputs.txt"
    
    parsed_indices = parse_inputs(index_inputs)
    
    
    tests = get_mult_inputs(in_file)
    
    
    
    states = init_items(tests)
    
    
    fin_ds = get_mult_inputs_output(fin_states)
    temp = init_items(fin_ds)
    
    
    
    ### each item in states: [player(s), deck, commands, indices, discard]
    
    
    ### states items order: [players list, draw deck, commands list, indices list, discard pile]
    
    test_mult_cases(states, parsed_indices)
    
        
    compare_all_states(states, temp)



