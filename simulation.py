from customer import Customer
from soda_machine import SodaMachine
import user_interface

class Simulation:
    def __init__(self):
        self.customer = Customer() # Move under Init?
        self.soda_machine = SodaMachine() # Move under Init?

    def run_simulation(self):
        """The central method called in main.py."""
        will_proceed = True # Changed from false to true
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 0: # changed '=' to '=='
                self.soda_machine.begin_transaction(self.customer) # Added self. to soda_machine and customer
            elif user_option == 1: # changed '=' to '=='
                self.customer.check_coins_in_wallet() # Added self. to customer
            elif user_option == 2: # changed '=' to '=='
                self.customer.check_backpack() # Added self. to customer
            elif user_option == 3: # added 3 option to terminate simulation
                user_interface.output_text("Have a nice day :) ")
                break
            else:
                will_proceed = False
