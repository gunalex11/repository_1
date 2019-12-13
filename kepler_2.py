#!/usr/bin/env python3

"""
Численное решение задачи скольких-то тел
"""

from __future__ import annotations  # !! typing
from abc import abstractmethod, ABC
from typing import List, Union
from numpy import array as vec
import numpy.linalg
import matplotlib.pyplot as plt


class Body:
    """Тело, движущаееся по двумерной плоскости"""

    def __init__(self, universe: Universe, mass: float, position: vec, velocity: vec):
        # Аннотации типов по желанию, но могут помочь IDE и компилятору, когда таковые имеются
        self.universe = universe
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def force_induced_by_other(self, other: Body) -> vec:
        """Сила, с которой другое тело действует на данное"""
        # Body is forward reference here
        delta_p = other.position - self.position
        distance = numpy.linalg.norm(delta_p)  # Евклидова норма (по теореме Пифагора)
        force_direction = delta_p / distance
        force = force_direction * self.mass * other.mass *\
                self.universe.gravity_flow_dencity_per_1_1(distance)
        return force

    def advance(self):
        """Перемещаем тело, исходя из его скорости"""
        self.position += self.velocity * MODEL_DELTA_T

    def apply_force(self, force: vec):
        """Изменяем скорость, исходя из силы, действующей на тело"""
        self.velocity += force * MODEL_DELTA_T / self.mass


# ABC это не алфавит, а AbstractBaseClass. Не даст создать экземпляр, пока не переопределишь все методы-заглушки
class Universe(ABC):
    """Невнятная вселенная, основа всех миров"""

    @abstractmethod
    def gravity_flow_dencity_per_1_1(self, dist: float) -> float:
        """
        Плотность потока гравитационного поля между двумя
        единичными массами на заданном расстоянии
        """
        raise NotImplementedError()

    @abstractmethod
    def model_step(self):
        """Итерация решения задачи Коши. Конечно не присуща вселенной, но тут на своём месте"""
        raise NotImplementedError()
    

class UniverseWithDimensionsAndBodies(Universe):
    """
    А это уже вселенная, у которой пространственных измерений, сколько скажут
    """
    
    def __init__(self,
                dimensions: int, # сколько пространственных измерений
                G: float,  # гравитационная постоянная
                collision_distance: float,  # всё-таки это не точки
            ):
        super().__init__()
        self.dimensions = dimensions
        self.G = G
        self.collision_distance = collision_distance
        self.bodies: List[Body] = []
        
    def gravity_flow_dencity_per_1_1(self, dist: float) -> float:
        # будем считать, что отскакивают точки друг от друга резко,
        # но стараться не допускать этого
        return self.G / dist ** (dimensions - 1) if dist > self.collision_distance else -self.G / dist ** dimensions
    
    def model_step(self):
        for i in range(len(self.bodies)):
            for j in range(len(self.bodies)):
                if i != j:
                    self.bodies[i].apply_force(self.bodies[i].force_induced_by_other(self.bodies[j]))
        for i in range(len(self.bodies)):
            self.bodies[i].advance()
            
    def add_body(self, b: Body):
        self.bodies.append(b)

        
if __name__ == '__main__':

    dimensions = int(input("How many dimensions do you live in?" + '\n'))
    
    un = UniverseWithDimensionsAndBodies(dimensions, 50, 3.08)
    
    bodies_hit_the_floor = [
        Body(un, 100.0, vec([0.0, 0.0]), vec([0.0, -15.0])),
        Body(un, 100.0, vec([20.0, 0.0]), vec([0.0, 15.0])),
        Body(un, 100.0, vec([10.0, 10.0]), vec([-15.0, 0.0])),
        Body(un, 100.0, vec([10.0, -10.0]), vec([15.0, 0.0]))
    ]
    
    for i in range(len(bodies_hit_the_floor)):
    	un.add_body(bodies_hit_the_floor[i])

    MODEL_DELTA_T = 0.01
    TIME_TO_MODEL = 5

    positions: Union[List[List[float]]] = [[[0 for i in range(int(TIME_TO_MODEL / MODEL_DELTA_T))] for a in range(len(un.bodies))], [[0 for i in range(int(TIME_TO_MODEL / MODEL_DELTA_T))] for a in range(len(un.bodies))]]
    
    for stepn in range(int(TIME_TO_MODEL / MODEL_DELTA_T)):
        for i in range(len(un.bodies)):
        	positions[0][i][stepn] = un.bodies[i].position[0]
        	positions[1][i][stepn] = un.bodies[i].position[1]
        un.model_step()


    for i in range(len(positions[0])):
    	plt.plot(positions[0][i], positions[1][i])

    plt.show()
