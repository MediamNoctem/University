import numpy
import numpy.random


class Swarm:
    def __init__(self, swarm_size, min_values, max_values, current_velocity_ratio, local_velocity_ratio, global_velocity_ratio):
        self.swarm_size = swarm_size

        self.min_values = numpy.array(min_values[:])
        self.max_values = numpy.array(max_values[:])

        self.current_velocity_ratio = current_velocity_ratio
        self.local_velocity_ratio = local_velocity_ratio
        self.global_velocity_ratio = global_velocity_ratio

        self.global_best_final_func = None
        self.global_best_position = None

        self.swarm = self.create_swarm()

    def create_swarm(self):
        return [Particle(self) for i in range(self.swarm_size)]

    def next_iteration(self):
        for particle in self.swarm:
            particle.next_iteration(self)

    def get_min_values(self):
        return self.min_values

    def get_max_values(self):
        return self.max_values

    def get_current_velocity_ratio(self):
        return self.current_velocity_ratio

    def get_local_velocity_ratio(self):
        return self.local_velocity_ratio

    def get_global_velocity_ratio(self):
        return self.global_velocity_ratio

    def get_global_best_position(self):
        return self.global_best_position

    def get_global_best_final_func(self):
        return self.global_best_final_func

    def get_final_func(self, position):
        final_func = self.final_func(position)
        if self.global_best_final_func is None or final_func < self.global_best_final_func:
            self.global_best_final_func = final_func
            self.global_best_position = position[:]
        return final_func

    def final_func (self, position):
        penalty = self.get_penalty (position, 10000.0)
        final_func = sum(position * position)
        return final_func + penalty

    def dimension(self):
        return len(self.min_values)

    def get_penalty(self, position, ratio):
        penalty1 = sum([ratio * abs(coord - min_val)
                        for coord, min_val in zip(position, self.min_values)
                        if coord < min_val])

        penalty2 = sum([ratio * abs(coord - max_val)
                        for coord, max_val in zip(position, self.max_values)
                        if coord > max_val])

        return penalty1 + penalty2


class Particle:
    def __init__(self, swarm):
        self.current_position = self.get_init_position(swarm)
        self.local_best_position = self.current_position[:]
        self.local_best_final_func = swarm.get_final_func(self.current_position)
        self.velocity = self.get_init_velocity(swarm)

    def get_position(self):
        return self.current_position

    def get_velocity(self):
        return self.velocity

    @staticmethod
    def get_init_position(swarm):
        return numpy.random.rand(swarm.dimension()) * (swarm.get_max_values() - swarm.get_min_values()) + swarm.get_min_values()

    @staticmethod
    def get_init_velocity(swarm):
        min_val = -(swarm.get_max_values() - swarm.get_min_values())
        max_val = (swarm.get_max_values() - swarm.get_min_values())
        return numpy.random.rand(swarm.dimension()) * (max_val - min_val) + min_val

    def next_iteration(self, swarm):
        rnd_current_best_position = numpy.random.rand(swarm.dimension())

        rnd_global_best_position = numpy.random.rand(swarm.dimension())

        velo_ratio = swarm.get_local_velocity_ratio() + swarm.get_global_velocity_ratio()
        common_ratio = (2.0 * swarm.get_current_velocity_ratio() /
                       (numpy.abs(2.0 - velo_ratio - numpy.sqrt(velo_ratio ** 2 - 4.0 * velo_ratio))))

        new_velocity_part1 = common_ratio * self.velocity

        new_velocity_part2 = (common_ratio *
                             swarm.get_local_velocity_ratio() *
                             rnd_current_best_position *
                             (self.local_best_position - self.current_position))

        new_velocity_part3 = (common_ratio *
                             swarm.get_global_velocity_ratio() *
                             rnd_global_best_position *
                             (swarm.get_global_best_position() - self.current_position))

        self.velocity = new_velocity_part1 + new_velocity_part2 + new_velocity_part3

        self.current_position += self.velocity

        final_func = swarm.get_final_func(self.current_position)
        if final_func < self.local_best_final_func:
            self.local_best_position = self.current_position[:]
            self.local_best_final_func = final_func


class ParticleSwarmMethod:
    @staticmethod
    def particle_swarm_method(swarm_size, min_values, max_values, current_velocity_ratio, local_velocity_ratio, global_velocity_ratio, iterations):
        swarm = Swarm(swarm_size, min_values, max_values, current_velocity_ratio, local_velocity_ratio, global_velocity_ratio)
        for n in range(iterations):
            swarm.next_iteration()
        min_point = swarm.get_global_best_position().tolist()
        return min_point


# if __name__ == "__main__":
#     psw = ParticleSwarmMethod()
#     print(psw.particle_swarm_method(200, numpy.array ([-5] * 2), numpy.array ([5] * 2), 0.1, 1.0, 5.0, 300))
