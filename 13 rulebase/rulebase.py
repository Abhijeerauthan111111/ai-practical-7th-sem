class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        
    def add_fact(self, fact):
        self.facts.add(fact)
        
    def remove_fact(self, fact):
        self.facts.discard(fact)
        
    def check_condition(self, condition):
        return condition in self.facts
    
    def run_diagnostic(self):
        print("Computer Troubleshooting System")
        print("------------------------------")
        
        # Gather initial symptoms
        response = input("Is the computer turning on? (yes/no): ").lower()
        if response == "no":
            self.add_fact("no_power")
        
        response = input("Do you hear any beeping sounds? (yes/no): ").lower()
        if response == "yes":
            self.add_fact("beeping")
        
        response = input("Is the screen displaying anything? (yes/no): ").lower()
        if response == "no":
            self.add_fact("no_display")
            
        # Apply rules
        if self.check_condition("no_power"):
            print("\nDiagnosis: Power Issue")
            print("Possible solutions:")
            print("1. Check if the power cable is properly connected")
            print("2. Test the power outlet")
            print("3. Check if the power supply unit is working")
            
        elif self.check_condition("beeping"):
            print("\nDiagnosis: Hardware Error")
            print("Possible solutions:")
            print("1. Check if RAM is properly seated")
            print("2. Check if all internal cables are connected")
            print("3. Remove and reseat the hardware components")
            
        elif self.check_condition("no_display"):
            print("\nDiagnosis: Display Issue")
            print("Possible solutions:")
            print("1. Check if monitor is properly connected")
            print("2. Test with different display cable")
            print("3. Test monitor with different computer")
            
        else:
            print("\nNo specific issues detected or unknown problem")
            print("Please contact technical support for further assistance")

# Create and run the system
if __name__ == "__main__":
    expert_system = RuleBasedSystem()
    expert_system.run_diagnostic()