import random
import uuid

class Claim:
    def __init__(self):
        self.id = uuid.uuid4()
        self.operational_cost = 0
        self.resolution_time = 0
        self.state = None
        self.context = {}
        
        self.create_context()
    
    def create_context(self):
        # Operational cost will be a random value between the min and max
        cost_min = random.randint(30000, 60000)
        cost_max = random.randint(120000, 200000)
        self.operational_cost = float(random.randrange(cost_min, cost_max) / 100)

        # Time to resolution will be a random to represent hours to resolve claim
        time_min = random.randint(3, 10)
        time_max = random.randint(375, 550)
        self.resolution_time = random.randint(time_min, time_max)
        
        # Choose a random state
        state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
        self.state = random.choice(state_names)
        
        self.context = {
            "key" : self.id,
            "country" : "USA",
            "custom" : {
                "state" : self.state,
                "operational_cost": self.operational_cost,
                "resolution_time": self.resolution_time
            }
        }

    def adjust_cost(self):
        # Hard coded to 4% per my experiment notes
        adjustment = 0.04 * self.operational_cost
        self.operational_cost -= adjustment
        
    def adjust_resolution(self):
        # Hard coded to 2% per my experiment notes
        adjustment = 0.02 * self.resolution_time
        self.resolution_time = float(self.resolution_time + adjustment)

    def debug(self):
        print("==========")
        print("ID: ", self.id)
        print("Operational cost: ", self.operational_cost)
        print("Resolution time: ", self.resolution_time)
        print("State: ", self.state)
        print("==========")