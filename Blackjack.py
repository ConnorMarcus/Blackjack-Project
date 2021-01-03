from random import *
from tkinter import *

def deal_cards() -> None:
    global my_cards
    global dealer_cards
    my_cards_dealt = 0
    dealer_cards_dealt = 0
    for card_count in range(4):
        if(my_cards_dealt != 2):
            my_cards += [shuffled_deck[card_count]]
            my_cards_dealt += 1
        elif(dealer_cards_dealt != 2):
            dealer_cards += [shuffled_deck[card_count]]
            dealer_cards_dealt += 1
    return my_cards, dealer_cards
    

def check_bust_and_total(hand) -> tuple:
    total = 0
    has_a_high_ace = False
    card = 0
    
    while (card < len(hand)):
        if ((hand[card][0] == "A") and (total <= 10)):
            total += 11
            has_a_high_ace = True
        elif((hand[card][0] == "A") and (total > 10)):
            total += 1
        else:
            total += card_values[hand[card][0]]
        if((total > 21) and (has_a_high_ace)):
            total -= 10
            has_a_high_ace = False
        card += 1
    
    if (total <= 21):
        return False, total
    else:
        return True, total

def hit() -> None:
    global my_bust
    global my_card_total
    global my_cards
    global current_card
    global xpos
    global my_cardimg1
    global my_cardimg2
    global my_cardimg3
    global my_cardimg4
    global my_card3
    global my_card4
    global my_card5
    global my_card6    
    global number_of_hits
    global my_total_label

    if ((number_of_hits < 4) and (not my_bust) and (not stand)):
        my_cards += [shuffled_deck[current_card]]
        my_bust, my_card_total = check_bust_and_total(my_cards)
        my_total_label.destroy()
        my_total_label = Label(window, text=str(my_card_total), font="Arial 30")
        my_total_label.place(relx=0.18, rely=0.5, anchor="center")        
    
        if (number_of_hits == 0):
            my_cardimg1 = PhotoImage(file="card_images/" + my_cards[-1] + ".png")
            my_card3 = Label(window, image=my_cardimg1)
            my_card3.place(relx=xpos, rely=0.8, anchor="center") 
        elif (number_of_hits == 1):
            my_cardimg2 = PhotoImage(file="card_images/" + my_cards[-1] + ".png")
            my_card4 = Label(window, image=my_cardimg2)
            my_card4.place(relx=xpos, rely=0.8, anchor="center") 
        elif (number_of_hits == 2):
            my_cardimg3 = PhotoImage(file="card_images/" + my_cards[-1] + ".png")
            my_card5 = Label(window, image=my_cardimg3)
            my_card5.place(relx=xpos, rely=0.8, anchor="center") 
        else:
            my_cardimg4 = PhotoImage(file="card_images/" + my_cards[-1] + ".png")
            my_card6 = Label(window, image=my_cardimg4)
            my_card6.place(relx=xpos, rely=0.8, anchor="center") 
    
        
        current_card += 1
        number_of_hits += 1
        xpos += 0.18
        
    if (my_bust):
        loss_screen()
 

def dealer_hit() -> None:
    global dealer_cards
    global dealer_bust
    global dealer_card_total
    global current_card
    global dealer_card1
    global flipped_card
    global dealer_card3
    global dealer_card4
    global dealer_card5
    global dealer_card6
    global dealer_cardimg1
    global dealer_cardimg2
    global dealer_cardimg3
    global dealer_cardimg4
    global dealer_cardimg5
    global stand
    global dealer_total_label
    
    dealer_hits = 0
    xpos2 = 0.54
    stand = True
    
    if(not my_bust):
        dealer_card1.destroy()
        dealer_cardimg1 = PhotoImage(file="card_images/" + dealer_cards[0] + ".png")
        flipped_card = Label(window, image=dealer_cardimg1)
        flipped_card.place(relx=0.9, rely=0.2, anchor="center")
        
        while ((dealer_card_total < 16) and (dealer_hits<4) and (not dealer_bust)):
            dealer_cards += [shuffled_deck[current_card]]
            dealer_bust, dealer_card_total = check_bust_and_total(dealer_cards)
            current_card += 1
            
            if (dealer_hits == 0):
                dealer_cardimg2 = PhotoImage(file="card_images/" + dealer_cards[-1] + ".png")
                dealer_card3 = Label(window, image=dealer_cardimg2)
                dealer_card3.place(relx=xpos2, rely=0.2, anchor="center")
            elif (dealer_hits == 1):
                dealer_cardimg3 = PhotoImage(file="card_images/" + dealer_cards[-1] + ".png")
                dealer_card4 = Label(window, image=dealer_cardimg3)
                dealer_card4.place(relx=xpos2, rely=0.2, anchor="center")
            elif(dealer_hits == 2):
                dealer_cardimg4 = PhotoImage(file="card_images/" + dealer_cards[-1] + ".png")
                dealer_card5 = Label(window, image=dealer_cardimg4)
                dealer_card5.place(relx=xpos2, rely=0.2, anchor="center")
            else:
                dealer_cardimg5 = PhotoImage(file="card_images/" + dealer_cards[-1] + ".png")
                dealer_card6 = Label(window, image=dealer_cardimg5)
                dealer_card6.place(relx=xpos2, rely=0.2, anchor="center")
            
            dealer_hits += 1
            current_card += 1
            xpos2 -= 0.18
        
        
        dealer_total_label = Label(window, text=str(dealer_card_total), font="Arial 30")
        dealer_total_label.place(relx=0.97, rely=0.4, anchor="center")
        if(dealer_bust):
            win_screen()
        else:
            find_winner()


def play_game() -> None:
    global my_bust
    global dealer_bust
    global my_card_total
    global dealer_card_total
    global dealer_card1
    global dealer_card2
    global my_total_label
    global my_card1
    global my_card2
    
    deal_cards()
    my_bust, my_card_total = check_bust_and_total(my_cards)
    dealer_bust, dealer_card_total = check_bust_and_total(dealer_cards)    
    
    window.geometry("1000x750")
    window.title("Blackjack")
    img1 = PhotoImage(file="card_images/background.png")      
    bg = Label(window, image=img1)
    bg.place(relx=0.5, rely=0.5, anchor="center")
    my_total_label = Label(window, text=str(my_card_total), font="Arial 30")
    my_total_label.place(relx=0.18, rely=0.5, anchor="center")    
    img2 = PhotoImage(file="card_images/" + my_cards[0] + ".png")
    my_card1 = Label(window, image=img2)
    my_card1.place(relx=0.1, rely=0.8, anchor="center")
    img3 = PhotoImage(file="card_images/" + my_cards[1] + ".png")
    my_card2 = Label(window, image=img3)
    my_card2.place(relx=0.28, rely=0.8, anchor="center")
    
    img4 = PhotoImage(file="card_images/gray_back.png")
    dealer_card1 = Label(window, image=img4)
    dealer_card1.place(relx=0.9, rely=0.2, anchor="center")
    
    img5 = PhotoImage(file="card_images/" + dealer_cards[1] + ".png")
    dealer_card2 = Label(window, image=img5)
    dealer_card2.place(relx=0.72, rely=0.2, anchor="center")
    img6 = PhotoImage(file="card_images/label2.png")
    dealer_label = Label(window, image=img6)
    dealer_label.place(relx=0.8, rely=0.4, anchor="center")
    img7 = PhotoImage(file="card_images/label1.png")
    player_label = Label(window, image=img7)
    player_label.place(relx=0.2, rely=0.6, anchor="center")
    testimg = PhotoImage(file="card_images/9C.png")
    mylab = Label(window, image=testimg)
    hit_button = Button(window, text="Hit", font="Arial 48", width="3", activeforeground="red", command=hit)
    hit_button.place(relx=0.1, rely=0.5, anchor="center")
    stand_button = Button(window, text="Stand", font="Arial 48", activeforeground="red", command=dealer_hit)
    stand_button.place(relx=0.28, rely=0.5, anchor="center")
    window.mainloop()



def find_winner() -> None:
    global result_text
    if(my_card_total < dealer_card_total):
        loss_screen()
    elif(my_card_total > dealer_card_total):
        win_screen()
    else:
        tie_screen()



def loss_screen() -> None:
    global result_text
    global play_again_button
    result_text = Label(window, text="You Lose!", font="Impact 48")
    result_text.place(relx=0.5, rely=0.5, anchor="center")
    play_again_button = Button(window, text="Play Again", font="Arial 48", activeforeground="red", command=play_again)
    play_again_button.place(relx=0.8, rely=0.5, anchor="center")    

def win_screen() -> None:
    global result_text
    global play_again_button
    result_text = Label(window, text="You Win!", font="Impact 48")
    result_text.place(relx=0.5, rely=0.5, anchor="center")
    play_again_button = Button(window, text="Play Again", font="Arial 48", activeforeground="red", command=play_again)
    play_again_button.place(relx=0.8, rely=0.5, anchor="center")    


def tie_screen() -> None:
    global result_text
    global play_again_button
    result_text = Label(window, text="It's a Tie!", font="Impact 48")
    result_text.place(relx=0.5, rely=0.5, anchor="center")
    play_again_button = Button(window, text="Play Again", font="Arial 48", activeforeground="red", command=play_again)
    play_again_button.place(relx=0.8, rely=0.5, anchor="center")    


def play_again() -> None:
    global shuffled_deck
    global my_bust
    global my_card_total
    global current_card
    global my_cards
    global dealer_cards
    global dealer_bust
    global dealer_card_total
    global number_of_hits
    global xpos
    global stand
    result_text.destroy()
    play_again_button.destroy()
    my_card1.destroy()
    my_card2.destroy()
    my_card3.destroy()
    my_card4.destroy()
    my_card5.destroy()
    my_card6.destroy()
    flipped_card.destroy()
    dealer_card2.destroy()
    dealer_card3.destroy()
    dealer_card4.destroy()
    dealer_card5.destroy()
    dealer_card6.destroy()
    shuffled_deck = sample(card_list, len(card_list))
    my_cards = []
    dealer_cards = []
    current_card = 4
    my_bust, my_card_total = False, 0
    dealer_bust, dealer_card_total = False, 0
    number_of_hits = 0
    xpos = 0.46
    stand = False    
    play_game()

    


#Main Script
card_list = ["2C", "2D", "2H", "2S", "3C", "3D", "3H", "3S", "4C", "4D", "4H", 
            "4S", "5C", "5D", "5H", "5S", "6C", "6D", "6H", "6S", "7C", "7D",
            "7H", "7S", "8C", "8D", "8H", "8S", "9C", "9D", "9H", "9S", "10C",
            "10D", "10H", "10S", "JC", "JD", "JH", "JS", "QC", "QD", "QH",
            "QS", "KC", "KD", "KH", "KS", "AC", "AD", "AH", "AS"]

card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "1":10,
               "J":10, "Q":10, "K":10}


shuffled_deck = sample(card_list, len(card_list))
my_cards = []
dealer_cards = []
current_card = 4
my_bust, my_card_total = False, 0
dealer_bust, dealer_card_total = False, 0
number_of_hits = 0
xpos = 0.46
stand = False
window = Tk()
my_card1 = Label(window)
my_card2 = Label(window)
my_card3 = Label(window)
my_card4 = Label(window)
my_card5 = Label(window)
my_card6 = Label(window)
my_cardimg1 = PhotoImage(file="card_images/2C.png")
my_cardimg2 = PhotoImage(file="card_images/2C.png")
my_cardimg3 = PhotoImage(file="card_images/2C.png")
my_cardimg4 = PhotoImage(file="card_images/2C.png")
dealer_cardimg1 = PhotoImage(file="card_images/2C.png")
dealer_cardimg2 = PhotoImage(file="card_images/2C.png")
dealer_cardimg3 = PhotoImage(file="card_images/2C.png")
dealer_cardimg4 = PhotoImage(file="card_images/2C.png")
dealer_cardimg5 = PhotoImage(file="card_images/2C.png")
dealer_card1 = Label(window)
flipped_card = Label(window)
dealer_card2 = Label(window)
dealer_card3 = Label(window)
dealer_card4 = Label(window)
dealer_card5 = Label(window)
dealer_card6 = Label(window)
my_total_label = Label(window, text="0")
dealer_total_label = Label(window, text="0")
result_text = Label(window)
play_again_button = Button(window)
play_game()


