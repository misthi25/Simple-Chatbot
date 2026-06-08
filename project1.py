import datetime

def start_advanced_chatbot():
    # 1. DEFINE SYSTEM PERSONA & LOGGING
    BOT_NAME = "DecodeGuard"
    
    # 2. HIERARCHICAL KNOWLEDGE BASE (Multi-State Memory)
    # The bot checks the current 'state' first, then evaluates the intent.
    state_machine = {
        "main": {
            "hello": "System active. Options: '1' Account, '2' System Status, '3' Compliance.",
            "hi": "System active. Options: '1' Account, '2' System Status, '3' Compliance.",
            "1": "Switched to [ACCOUNT MANAGEMENT]. Options: 'balance', 'tier', or 'back'.",
            "2": "Switched to [SYSTEM STATUS]. Options: 'uptime', 'load', or 'back'.",
            "3": "Switched to [COMPLIANCE]. Options: 'framework', 'safety', or 'back'.",
            "help": "Type '1', '2', or '3' to enter a subdomain pipeline. Type 'exit' to terminate."
        },
        "account": {
            "balance": "All internship accounts show a balanced credit metric of 100%.",
            "tier": "Your access level: Junior AI Engineer (Foundation Phase Loop)[cite: 6, 7].",
            "back": "Returning to Main Menu."
        },
        "system_status": {
            "uptime": "Logic Engine Core uptime is at 99.998% deterministic precision[cite: 34].",
            "load": "Current linear complexity threat level: 0(1) Constant Time Optimal[cite: 153, 154].",
            "back": "Returning to Main Menu."
        },
        "compliance": {
            "framework": "Deterministic Filter active: Simulating Llama Guard / NVIDIA NeMo boundaries[cite: 68, 69].",
            "safety": "White Box Execution Profile: Zero hallucination risk verified[cite: 55, 59].",
            "back": "Returning to Main Menu."
        }
    }

    # Initialize state variables
    current_state = "main"

    print("==========================================================")
    print(f"       {BOT_NAME} v2.0 - Hierarchical Guardrail Engine      ")
    print("        (State Tracking, Context Memory, & Logs Active)     ")
    print("==========================================================")
    print("DecodeGuard: System initialized. Say 'hello' or type 'help' to begin.")

    # 3. CONTINUOUS PIPELINE LOOP
    while True:
        raw_input = input("\nYou: ")
        
        # Sanitization Block
        clean_input = raw_input.lower().strip()
        
        # Kill Command Strategy
        if clean_input in ['exit', 'quit', 'terminate']:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {BOT_NAME}: System breaking loop cleanly. Goodbye!")
            break
            
        # 4. HIERARCHICAL PROCESS BLOCK
        # Look up the allowed inputs for our current menu state
        allowed_intents = state_machine[current_state]
        
        # Retrieve mapped response or handle fallback via atomic operation
        reply = allowed_intents.get(clean_input, None)
        
        if reply is not None:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {BOT_NAME}: {reply}")
            
            # State Transition Logic (Context Switching)
            if current_state == "main":
                if clean_input == "1":
                    current_state = "account"
                elif clean_input == "2":
                    current_state = "system_status"
                elif clean_input == "3":
                    current_state = "compliance"
            elif clean_input == "back":
                current_state = "main"
                
        else:
            # Context-Specific Fallback Tracking
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {BOT_NAME}: Fallback Exception! ")
            if current_state == "main":
                print("            -> Hint: Try typing '1', '2', '3', or 'help'.")
            else:
                print(f"            -> Hint: You are currently inside [{current_state.upper()}]. Type 'back' to change menus.")

if __name__ == "__main__":
    start_advanced_chatbot()