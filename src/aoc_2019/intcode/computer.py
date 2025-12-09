from dataclasses import dataclass, field
from enum import Enum

from common.input import get_lines


class Operation(Enum):
    ADD = 1
    MULTIPLY = 2
    STOP = 99


@dataclass
class Computer:
    initial_memory: list[int] = field(default_factory=list)
    memory: list[int] = field(init=False, default_factory=list)
    pointer: int = field(init=False, default=0)

    @staticmethod
    def from_input(data: str) -> 'Computer':
        return Computer([int(x) for x in "".join(get_lines(data)).split(",")])

    def __post_init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.pointer = 0
        self.memory = list(self.initial_memory)

    def run(self) -> None:
        operation = Operation(self.memory[self.pointer])
        while operation != Operation.STOP:
            match operation:
                case Operation.ADD:
                    self.pointer = self.add(self.pointer)
                case Operation.MULTIPLY:
                    self.pointer = self.multiply(self.pointer)
            operation = Operation(self.memory[self.pointer])

    def _lookup_arith(self, index: int) -> tuple[int, int, int, int]:
        li = index + 1
        ri = index + 2
        ai = index + 3
        result = index + 4
        lvi = self.memory[li]
        rvi = self.memory[ri]
        avi = self.memory[ai]
        return self.memory[lvi], self.memory[rvi], avi, result

    def add(self, index: int) -> int:
        left, right, answer, result = self._lookup_arith(index)
        self.memory[answer] = left + right
        return result

    def multiply(self, index: int) -> int:
        left, right, answer, result = self._lookup_arith(index)
        self.memory[answer] = left * right
        return result

    def __getitem__(self, index: int) -> int:
        return self.memory[index]

    def __setitem__(self, index: int, value: int) -> None:
        self.memory[index] = value
