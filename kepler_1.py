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
import matplotlib.axes


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

#class UniverseWith3Bodies(Universe):
#    """
#    Демо-вселенная.
#    Кому угодно понятно, что она ненастоящая.
#    Зато уже есть.
#    """
#
#    def __init__(self,
#                 G: float,  # гравитационная постоянная
#                 collision_distance: float  # всё-таки это не точки
#                 ):
#        """В начале было... да, а потом тестовая вселенная с пупом мира и двумя камнями"""
#        self.G = G
#        self.collision_distance = collision_distance
#
#        self.centrum = Body(self, 500.0, vec([0.0, 0.0]), vec([0.0, 0.0]))
#        self.p_1 = Body(self, 10.0, vec([50.0, 0.0]), vec([0.0, 15.0]))
#        self.p_2 = Body(self, 10.0, vec([50.0, 40.0]), vec([-7.0, 7.0]))
#
#    def gravity_flow_dencity_per_1_1(self, dist: float) -> float:
#        # будем считать, что отскакивают точки друг от друга резко,
#        # но стараться не допускать этого
#        return self.G / dist ** 2 if dist > self.collision_distance else -self.G / dist ** 3
#
#    def model_step(self):
#        self.p_1.apply_force(self.p_1.force_induced_by_other(self.centrum))
#        self.p_2.apply_force(self.p_2.force_induced_by_other(self.centrum))
#        self.p_1.advance()
#        self.p_2.advance()

class UniverseWithBodies(Universe):
    """
    Будем считать, что это наша вселенная. Кстати, в ней тела действуют и
    друг на друга.
    """

    def __init__(self,
                 G: float,  # гравитационная постоянная
                 collision_distance: float,  # всё-таки это не точки
                 bodies: List[Body]
                 ):
        super().__init__()
        self.G = G
        self.collision_distance = collision_distance
        self.bodies = bodies

    def gravity_flow_dencity_per_1_1(self, dist: float) -> float:
        # будем считать, что отскакивают точки друг от друга резко,
        # но стараться не допускать этого
        return self.G / dist ** 2 if dist > self.collision_distance else -self.G / dist ** 3

    def model_step(self):
        for i in range(len(self.bodies)):
            for j in range(len(self.bodies)):
                if i != j:
                    self.bodies[i].apply_force(self.bodies[i].force_induced_by_other(self.bodies[j]))
        for i in range(len(self.bodies)):
            self.bodies[i].advance()


#class UniverseWithDimensionsAndBodies(UniverseWithBodies):
#    """
#    А это уже вселенная, у которой пространственных измерений, сколько скажут
#    """
#
#    def __init__(self,
#                 dimensions: int, # сколько пространственных измерений
#                 G: float,  # гравитационная постоянная
#                 collision_distance: float,  # всё-таки это не точки
#                 bodies: List[Body]
#                 ):
#        super().__init__(G, collision_distance, bodies)
#        self.dimensions = dimensions
#
#    def gravity_flow_dencity_per_1_1(self, dist: float) -> float:
#        # Должна использовать self.dimensions
#        raise NotImplementedError("Запрограммируй меня!")


if __name__ == '__main__':

    bodies_hit_the_floor = [Body(UniverseWithBodies, 500.0, vec([0.0, 0.0]), vec([0.0, 0.0])), Body(UniverseWithBodies, 10.0, vec([50.0, 0.0]), vec([0.0, 15.0])), Body(UniverseWithBodies, 10.0, vec([50.0, 40.0]), vec([-7.0, 7.0]))]
    un = UniverseWithBodies(50, 3.0, bodies_hit_the_floor)

    MODEL_DELTA_T = 0.01
    TIME_TO_MODEL = 10

    positions: List[Unioin[float, float]] = []
    for stepn in range(int(TIME_TO_MODEL / MODEL_DELTA_T)):
        for i in range(len(un.bodies)):
            positions.append([un.bodies[i].position[0], un.bodies[i].position[1]])
        un.model_step()
    
#    c = plt.Circle((0, 0), 2, color='b')
    ax: matplotlib.axes.Axes = plt.gca()  # !! typing
    ax.set_aspect('equal')
    ax.add_patch(c)

    for i in range(len(positions)):
        plt.plot(positions[i][0], positions[i][1])

    plt.show()
