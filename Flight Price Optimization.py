import sys
sys.path.append('../input')
from flight_revenue_simulator import simulate_revenue, score_me



def pricing_function(days_left, tickets_left, demand_level):
    """Sample pricing function"""
    price = demand_level - 10
    return price

simulate_revenue(days_left=7, tickets_left=50, pricing_function=pricing_function, verbose=True)

score_me(pricing_function)
