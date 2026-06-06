#!/usr/bin/env python3
"""
IELTS Collocation Master - Interactive Learning Game
Main entry point for the collocation guessing game
"""

import json
import os
from collocations.game import CollocationGame
from collocations.database import CollocationDatabase

def main():
    """Main function to run the IELTS Collocation Master game"""
    
    print("\n" + "="*60)
    print("  IELTS COLLOCATION MASTER 🎯")
    print("  Learn Band 8-9 Collocations Interactively")
    print("="*60 + "\n")
    
    # Initialize the game
    db = CollocationDatabase()
    game = CollocationGame(db)
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Start Interactive Game (30 Collocations)")
        print("2. Learn Mode (Study collocations with examples)")
        print("3. View Statistics")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            game.play_game()
        elif choice == "2":
            game.learn_mode()
        elif choice == "3":
            game.show_statistics()
        elif choice == "4":
            print("\n✨ Thank you for learning with IELTS Collocation Master!")
            print("Keep practicing to improve your writing band score!\n")
            break
        else:
            print("❌ Invalid option. Please select 1-4.")

if __name__ == "__main__":
    main()