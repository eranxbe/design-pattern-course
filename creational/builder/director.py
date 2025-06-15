"""controls the building process using a builder instance"""

from builder import Builder


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct_sandwich(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()
