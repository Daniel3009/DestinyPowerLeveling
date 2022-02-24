#!/usr/bin/env python
# coding: utf-8


from statistics import mean
from random import randint
from math import floor
import numpy as np
import itertools



items = [1525, 1527, 1530, 1525, 1530, 1531, 1528, 1525]
activities = [11,0, 10]
simulate_runs = 10_000
analyze_first_n_drops = 5




class Player():
    def __init__(self,items: list):
        self.power=items
        
    def equip_item(self,slot: int, power:int):
        if power > self.power[slot]:
            self.power[slot] = power   
            
    def current_power(self): 
        return floor(mean(self.power))
    
    def update_blues(self):
        current_power = self.current_power()
        for idx, value in enumerate(self.power):
            if value < current_power - 1:
                self.power[idx]= current_power - 1
            


        
    
class Rewards():
    def __init__(self, player):
        self.player=player
        
    def drop_item(self, tier):
        player_power = self.player.current_power()
        power_drop = player_power + min(tier + 2, 5)
        slot = randint(0,7)
        self.player.equip_item(slot, power_drop)
        self.player.update_blues()

        
class Game():
    def __init__(self, items, activities):
        self.saved_items = items
        self.saved_activities = activities 
        self.orders = []
        self.pattern = {}
        
    def calculate_best_order(self, N):
        for i in range(1,N+1):
            player = Player(list(self.saved_items))
            rewards = Rewards(player)
            activities = np.array(self.saved_activities)
            order = [] 
            while(len(np.nonzero(activities)[0])):
                tier = self.draw_activity(activities)
                order.append(tier)
                rewards.drop_item(tier)
            resulting_power = np.average(player.power)
            self.orders.append((order, resulting_power))
        
        
    def draw_activity(self, activities):
        idx_nonzero, = np.nonzero(activities)
        #print(activities, idx_nonzero)
        idx = np.random.choice(idx_nonzero)
        activities[idx]-= 1
        return idx+1
    
    def show_results(self):
        self.orders.sort(key=lambda x: x[1],reverse=True)
        for order in self.orders:
            print(order)
            
    def analyze_results(self, next_steps):
        a1 = np.array([x[0] for x  in self.orders])
        a2 = np.array([x[1] for x  in self.orders])
        for i in range(1,next_steps+1):
            x = [1, 2, 3]
            checks = [p for p in itertools.product(x, repeat=i)]
            for check in checks:
                bool_mask = [True]*len(a1)
                for idx, tier in enumerate(check):
                    bool_mask = bool_mask & (a1[:,idx] == tier)
                results = a2[bool_mask]
                if results.size > 0:
                    self.pattern[check] = np.average(a2[bool_mask])
                
        return self.orders



g = Game(items, activities)
g.calculate_best_order(simulate_runs)
g.analyze_results(analyze_first_n_drops)
results = dict(sorted(g.pattern.items(), key=lambda item: item[1], reverse=True))
for i in results.items():
    print(i[0], i[1])
