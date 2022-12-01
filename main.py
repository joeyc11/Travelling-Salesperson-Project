import pandas as pd

from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions
from nnf import dsharp

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure

import random

import tkinter as tk
from tkinter import ttk

E = Encoding() 
TIRE_SEASON = ["Summer", 'Winter']
TIRE_USE = ["Heavy", "Medium", "Light"]
WEIGHT = ["Heavy", "Medium", "Light"]
FRICTION = ["High", "Medium", "Low"]
ROUTE = [1,2,3]
ROUTE_CONDITION = ["Icy", " Dry" ]
ROUTE_SPEED_LIMIT = [60,80 ,100, 120]

PROPOSITIONS = []
#proposition for route to have a condition
@proposition(E)
class RouteCondition:
    def _init_(self, route, condition):
        self.route = route
        self.condition = condition
    def __str__(self):
        return f"condition(r{self.route})={self.condition}"
#proposition for route to have a speed limit
class RouteSpeed:
    def _init_(self, route, speed):
        self.route = route
        self.speed = speed
    def __str__(self) -> str:
        return f"speed(r{self.route})={self.speed}"
#proposition for route to have a safety level
class RouteSafety:
    def _init_(self, route, safety):
        self.route = route
        self.safety = safety
    def __str__(self) -> str:
        return f"safety(r{self.route})={self.safety}"
#proposition for tires to have season
class tireS:
    def __init__(self, season):
        self.season = season
    def __str__(self) -> str:
        return f"tires({self.season}"
#proposition for tire to have a level of wear
class tireW:
    def __init__(self, wear):
        self.wear = wear
    def __str__(self) -> str:
        return f"tires({self.wear}"
#proposition for tire to match road condition
class tireMatch:
    def __init__(self, matching):
        self.matching = matching
    def __str__(self) -> str:
        return f"tires({self.matching}"
#proposition for vehicle to have a weight
class vehicleW:
    def __init__(self, weight):
        self.weight = weight
    def __str__(self) -> str:
        return f"vehicle(weight{self.weight})"
#proposition for vehicle to have a friction
class vehicleF:
    def __init__(self, friction):
        self.frico = friction
    def __str__(self) -> str:
        return f"vehicle(friction{self.friction})"
#proposition for best route
class bestRoute:
    def __init__(self, route):
        self.route = route
    def __str__(self) -> str:
        return f"Best route({self.friction})"
#Constraints#

#Each road can only have one road condition
for route in ROUTE:
    constraint.add_exactly_one(E, [RouteCondition(route, condition) for condition in ROUTE_CONDITION])

#Each road can only have one speed limit and one safety level
for route in ROUTE:
    constraint.add_exactly_one(E, [RouteSpeed(route, speed) for speed in ROUTE_SPEED_LIMIT])
    constraint.add_exactly_one(E, [RouteSpeed(route, friction) for friction in FRICTION])
#Tires can only be winter or summer
    constraint.add_exactly_one(E), [tireS(season) for season in TIRE_SEASON]
#Tires can only have one condition
    constraint.add_exactly_one(E), [tireW(use) for use in TIRE_USE]
#Vehicle can only have one weight and one friction level
    constraint.add_exactly_one(E), [vehicleW(weight) for weight in WEIGHT]
    constraint.add_exactly_one(E), [vehicleF(friction) for friction in FRICTION]
#Any tire works on dry roads, but icy roads require winter tires to be safe
matching = tireMatch("True")
for n in ROUTE:
    E.add_constraint(tireS("Winter") & (route(n, "Icy")>> matching))
    E.add_constraint((route(n, "Dry") >> matching))
#RULES

#The car's friction is affected by its weight, the tire's wear, and the tires versus the type of road.
#If there are two or more negatively contributing factors, the vehicle will have low friction
for n in ROUTE:
    E.add_constraint(~matching & tireW("Heavy") >> vehicleF("Low") & RouteSafety(n, "Low"))
    E.add_constraint(vehicleW("Light") & ~matching >> vehicleF("Low")& RouteSafety(n, "Low"))
    E.add_constraint(vehicleW("Light")& tireW("Heavy") >> vehicleF("Low")& RouteSafety(n, "Low"))
        
#If there are two or more positively contributing factors, the vehicle has high friction
    E.add_constraint(matching & tireW("Heavy") >> vehicleF("High")& RouteSafety(n, "High"))
    E.add_constraint(vehicleW("Heavy") & matching >> vehicleF("High")& RouteSafety(n, "High"))
    E.add_constraint(vehicleW("Heavy")& tireW("Light") >> vehicleF("High")& RouteSafety(n, "High"))
        
#If there is one positive factor, one negative, and one neutral, the vehicle has neutral friction
    E.add_constraint(matching &  tireS("Light") >> vehicleF("Medium") & RouteSafety(n, "Medium"))
    E.add_constraint(~matching & tireS("Heavy") >> vehicleF("Medium")& RouteSafety(n, "Medium"))
    E.add_constraint(~matching &  tireS("Medium") & vehicleW("Heavy") >> vehicleF("Medium")& RouteSafety(n, "Medium"))
    E.add_constraint(matching & tireS("Medium") & vehicleW("Light") >> vehicleF("Medium")& RouteSafety(n, "Medium"))

#The ideal route is one that has medium friction, and the highest speed limit. If there is no such route, it prioritizes safety(High friction, but lower speed).
    E.add_constraint(RouteSpeed(120) & route())


    


