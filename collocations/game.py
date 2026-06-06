"""
Game Logic
Handles the interactive collocation guessing game
"""

import json
import os
from datetime import datetime

class CollocationGame:
    """Main game class for interactive collocation learning"""
    
    def __init__(self, database):
        self.db = database
        self.collocations = database.get_all_collocations()
        self.stats_file = "player_stats.json"
        self.stats = self._load_stats()
        self.current_score = 0
        self.current_attempts = {}
    
    def _load_stats(self):
        """Load player statistics from file"""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r') as f:
                    return json.load(f)
            except:
                return self._initialize_stats()
        return self._initialize_stats()
    
    def _initialize_stats(self):
        """Initialize empty statistics"""
        return {
            "total_games": 0,
            "total_correct": 0,
            "total_attempts": 0,
            "collocations_learned": {},
            "last_played": None
        }
    
    def _save_stats(self):
        """Save player statistics to file"""
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)
    
    def play_game(self):
        """Main game loop for playing the collocation game"""
        print("\n" + "="*60)
        print("  INTERACTIVE COLLOCATION GAME")
        print("  Guess the 5 most common collocations")
        print("="*60 + "\n")
        
        self.current_score = 0
        self.current_attempts = {}
        
        # Shuffle collocations for variety
        import random
        game_collocations = random.sample(self.collocations, len(self.collocations))
        
        for index, collocation in enumerate(game_collocations, 1):
            self._play_round(collocation, index, len(game_collocations))
            
            # Ask if player wants to continue
            if index < len(game_collocations):
                cont = input("\nPress Enter to continue to next collocation (or 'q' to quit): ").strip().lower()
                if cont == 'q':
                    break
        
        self._show_final_results()
        self._update_stats()
    
    def _play_round(self, collocation, round_num, total_rounds):
        """Play a single round of the game"""
        print(f"\n{'─'*60}")
        print(f"Collocation {round_num}/{total_rounds}")
        print(f"{'─'*60}")
        
        # Show difficulty indicator
        difficulty_indicator = "⭐" * collocation["difficulty"]
        print(f"Difficulty: {difficulty_indicator}")
        
        print(f"\n📝 Complete the phrase: \"{collocation['prompt']} ___\"\n")
        
        correct_answers = set(collocation["correct_answers"])
        guessed_correct = set()
        attempts = 0
        max_attempts = 7
        
        while len(guessed_correct) < len(correct_answers) and attempts < max_attempts:
            remaining = len(correct_answers) - len(guessed_correct)
            print(f"Remaining answers to guess: {remaining}/{len(correct_answers)}")
            print(f"Attempts left: {max_attempts - attempts}")
            
            guess = input("Your guess (or 'hint' for hint, 'skip' to skip): ").strip().lower()
            
            if guess == 'skip':
                print(f"❌ Skipped! The answers were: {', '.join(sorted(correct_answers))}")
                self.current_attempts[collocation['id']] = {'correct': len(guessed_correct), 'total': len(correct_answers), 'skipped': True}
                return
            
            if guess == 'hint':
                self._show_hint(collocation, guessed_correct)
                continue
            
            if guess in correct_answers:
                if guess not in guessed_correct:
                    guessed_correct.add(guess)
                    print(f"✅ Correct! \"{collocation['prompt']} {guess}\"")
                    self.current_score += 1
                else:
                    print(f"⚠️  You already guessed that one!")
            else:
                print(f"❌ Not correct. Try again!")
            
            attempts += 1
            print()
        
        if len(guessed_correct) == len(correct_answers):
            print(f"🎉 Perfect! You found all the answers!")
            print(f"   Answers: {', '.join(sorted(guessed_correct))}")
        else:
            print(f"\n📊 You found {len(guessed_correct)}/{len(correct_answers)} answers")
            if len(guessed_correct) < len(correct_answers):
                missed = correct_answers - guessed_correct
                print(f"   Missing: {', '.join(sorted(missed))}")
        
        self.current_attempts[collocation['id']] = {
            'correct': len(guessed_correct),
            'total': len(correct_answers)
        }
        
        # Show explanation and examples
        self._show_collocation_details(collocation)
    
    def _show_hint(self, collocation, already_guessed):
        """Provide a hint to the player"""
        remaining = set(collocation["correct_answers"]) - already_guessed
        if remaining:
            hint = list(remaining)[0]
            print(f"💡 Hint: The answer starts with '{hint[0].upper()}' and has {len(hint)} letters")
    
    def _show_collocation_details(self, collocation):
        """Show detailed information about a collocation"""
        print(f"\n📚 COLLOCATION DETAILS")
        print(f"{'─'*60}")
        print(f"Phrase: {collocation['prompt']} {', '.join(collocation['correct_answers'][:3])}...")
        print(f"Category: {collocation['category'].upper()}")
        print(f"\nExplanation: {collocation['explanation']}")
        
        print(f"\n📖 EXAMPLE SENTENCES:")
        for topic, example in collocation['examples'].items():
            print(f"   • {topic}: {example}")
        
        print(f"\n🔄 Variants: {', '.join(collocation['variants'])}")
    
    def _show_final_results(self):
        """Show final game results"""
        print(f"\n\n{'='*60}")
        print("  GAME RESULTS")
        print(f"{'='*60}\n")
        
        print(f"📊 Final Score: {self.current_score} collocations guessed correctly")
        
        if self.current_score >= 25:
            rating = "🏆 Excellent! Band 8-9 level"
        elif self.current_score >= 20:
            rating = "⭐ Very Good! Band 7-8 level"
        elif self.current_score >= 15:
            rating = "👍 Good! Band 6-7 level"
        else:
            rating = "📚 Keep practicing! More work needed"
        
        print(f"Rating: {rating}")
    
    def _update_stats(self):
        """Update and save player statistics"""
        self.stats['total_games'] += 1
        self.stats['total_correct'] += self.current_score
        self.stats['total_attempts'] += len(self.current_attempts)
        self.stats['last_played'] = datetime.now().isoformat()
        
        for coll_id, result in self.current_attempts.items():
            if coll_id not in self.stats['collocations_learned']:
                self.stats['collocations_learned'][str(coll_id)] = {
                    'attempts': 0,
                    'correct': 0
                }
            self.stats['collocations_learned'][str(coll_id)]['attempts'] += 1
            self.stats['collocations_learned'][str(coll_id)]['correct'] += result['correct']
        
        self._save_stats()
    
    def learn_mode(self):
        """Learning mode - study collocations without guessing"""
        print("\n" + "="*60)
        print("  LEARN MODE - Study Collocations")
        print("="*60 + "\n")
        
        print("Choose learning option:")
        print("1. View all 30 collocations")
        print("2. Filter by difficulty")
        print("3. Filter by category")
        print("4. Back to main menu")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            collocations = self.collocations
        elif choice == "2":
            print("\n1. Beginner (⭐)")
            print("2. Intermediate (⭐⭐)")
            print("3. Advanced (⭐⭐⭐)")
            diff = input("Select difficulty (1-3): ").strip()
            collocations = self.db.get_by_difficulty(int(diff))
        elif choice == "3":
            print("\n1. Verbal")
            print("2. Adjectival")
            print("3. Adverbial")
            cat = input("Select category: ").strip().lower()
            category_map = {"1": "verbal", "2": "adjectival", "3": "adverbial"}
            collocations = self.db.get_by_category(category_map.get(cat))
        else:
            return
        
        self._display_collocations(collocations)
    
    def _display_collocations(self, collocations):
        """Display collocations in a readable format"""
        for index, coll in enumerate(collocations, 1):
            print(f"\n{'─'*60}")
            print(f"Collocation {index}")
            print(f"{'─'*60}")
            print(f"Phrase: {coll['prompt']} {', '.join(coll['correct_answers'])}")
            print(f"Difficulty: {'⭐' * coll['difficulty']}")
            print(f"Category: {coll['category']}")
            print(f"\nExplanation: {coll['explanation']}")
            print(f"\nExamples:")
            for topic, example in coll['examples'].items():
                print(f"  • {topic}: {example}")
            print(f"\nVariants: {', '.join(coll['variants'])}")
            
            if index < len(collocations):
                input("\nPress Enter to continue...")
    
    def show_statistics(self):
        """Display player statistics"""
        print("\n" + "="*60)
        print("  YOUR STATISTICS")
        print("="*60 + "\n")
        
        if self.stats['total_games'] == 0:
            print("❌ No games played yet. Start playing to build statistics!")
            return
        
        print(f"📊 OVERALL STATS:")
        print(f"   Total games played: {self.stats['total_games']}")
        print(f"   Total correct guesses: {self.stats['total_correct']}")
        print(f"   Total attempts: {self.stats['total_attempts']}")
        avg_score = self.stats['total_correct'] / self.stats['total_games']
        print(f"   Average score per game: {avg_score:.1f}")
        print(f"   Last played: {self.stats['last_played']}")
        
        print(f"\n📈 TOP COLLOCATIONS (Most Correct):")
        if self.stats['collocations_learned']:
            # Sort by correct answers
            sorted_colls = sorted(
                self.stats['collocations_learned'].items(),
                key=lambda x: x[1]['correct'],
                reverse=True
            )[:5]
            
            for coll_id, data in sorted_colls:
                coll = self.db.get_collocation(int(coll_id))
                if coll:
                    print(f"   • {coll['prompt']}: {data['correct']}/{data['attempts']} correct")
        
        input("\nPress Enter to return to menu...")