import random
import sys

def run_security_quiz():
    # Questions and answers for the quiz
    questions = [
        ("What is the primary difference between a stateful and a stateless firewall?", 
         ["Stateful firewalls monitor traffic patterns, stateless do not.",
          "Stateless firewalls are hardware-based, stateful are software-based.",
          "Stateful firewalls keep track of active connections, stateless firewalls do not.",
          "Stateless firewalls require regular updates, stateful do not."], 
         "C"),
        ("Why is a Security Information and Event Management (SIEM) system important in an organization?",
         ["It manages employee internet usage.",
          "It aids in regulatory compliance and real-time security monitoring.",
          "It is primarily used for data storage.",
          "It replaces the need for a cybersecurity team."],
         "B"),
        ("What is a phishing attack?",
         ["An attack that shuts down systems until a ransom is paid.",
          "A method where the attacker physically breaks into a network.",
          "An attack that uses disguised email as a weapon.",
          "A virus that corrupts files on a computer."],
         "C"),
        ## ADDITONAL QUESTIONS SHOULD GO HERE FOLLOWING THE SAME FORMAT 
    ]

    # Game initialization
    lives = 3
    points = 0
    while lives > 0:
        # Shuffle the questions each round
        random.shuffle(questions)
        for question, options, answer in questions:
            print(question)
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")

            # User input and validation
            user_answer = input("Your answer (please enter the option number): ").strip().upper()
            if user_answer == answer:
                points += 1
                print("Correct! +1 point")
            else:
                points -= 2
                print("Wrong! -2 points")
                if points < 0:
                    lives -= 1
                    points = 0
                    print(f"You lost a life! Lives remaining: {lives}")
                    if lives == 0:
                        break
                    print("Next question:")
        
        if lives > 0:
            print("You've completed the round!")
            print(f"Your score: {points}")
            print("Starting new round...")
        else:
            print("YOU LOSE")
            print("Press spacebar to start again")
            # Wait for the user to press spacebar to restart the game
            while True:
                restart_key = input()
                if restart_key == " ":
                    lives = 3
                    points = 0
                    break
                else:
                    print("Press spacebar to continue")

    print("Game Over! Thanks for playing.")

# Run the quiz game, close winodw to end the game 
run_security_quiz()
