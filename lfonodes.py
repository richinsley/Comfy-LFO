import math

TREE_MAIN = "LFO"

class TriangleNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "position": ("FLOAT", {"default": 0.0, "step": 0.001}),
                "phase_offset": ("FLOAT", {"default": 0.5, "step": 0.001}),
                "frequency": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "amplitude": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "offset": ("FLOAT", {"default": 0.0, "step": 0.001}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "triangle_wave"
    CATEGORY = TREE_MAIN

    def triangle_wave(self, position, phase_offset, frequency, amplitude, offset):
        position = position + phase_offset
        phase = (position * frequency) - int(position * frequency)
        return offset + amplitude * (2 * abs(2 * phase - 1) - 1),

class SineNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "position": ("FLOAT", {"default": 0.0, "step": 0.001}),
                "phase_offset": ("FLOAT", {"default": 0.5, "step": 0.001}),
                "frequency": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "amplitude": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "offset": ("FLOAT", {"default": 0.0, "step": 0.001}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "sine_wave"
    CATEGORY = TREE_MAIN

    def sine_wave(self, position, phase_offset, frequency, amplitude, offset):
        position = position + phase_offset
        phase = position * frequency * 2 * math.pi
        return offset + amplitude * math.sin(phase),

class SawtoothNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "position": ("FLOAT", {"default": 0.0, "step": 0.001}),
                "phase_offset": ("FLOAT", {"default": 0.5, "step": 0.001}),
                "frequency": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "amplitude": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "offset": ("FLOAT", {"default": 0.0, "step": 0.001}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "sawtooth_wave"
    CATEGORY = TREE_MAIN

    def sawtooth_wave(self, position, phase_offset, frequency, amplitude, offset):
        position = position + phase_offset
        phase = (position * frequency) - int(position * frequency)
        return offset + amplitude * (2 * phase - 1),

class SquareNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "position": ("FLOAT", {"default": 0.0, "step": 0.001}),
                "phase_offset": ("FLOAT", {"default": 0.5, "step": 0.001}),
                "frequency": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "amplitude": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "offset": ("FLOAT", {"default": 0.0, "step": 0.001}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "square_wave"
    CATEGORY = TREE_MAIN

    def square_wave(self, position, phase_offset, frequency, amplitude, offset):
        position = position + phase_offset
        phase = (position * frequency) - int(position * frequency)
        return offset + amplitude * (1 if phase < 0.5 else -1),

class PulseNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "position": ("FLOAT", {"default": 0.0, "step": 0.001}),
                "phase_offset": ("FLOAT", {"default": 0.5, "step": 0.001}),
                "frequency": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "amplitude": ("FLOAT", {"default": 1.0, "step": 0.001}),
                "offset": ("FLOAT", {"default": 0.0, "step": 0.001}),
                "pulse_width": ("FLOAT", {"default": 0.3, "step": 0.001}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "pulse_wave"
    CATEGORY = TREE_MAIN

    def pulse_wave(self, position, pulse_width, phase_offset, frequency, amplitude, offset):
        position = position + phase_offset
        phase = (position * frequency) - int(position * frequency)
        return offset + amplitude * (1 if phase < pulse_width else -1),

NODE_CLASS_MAPPINGS = {
    "LFO_Triangle": TriangleNode,
    "LFO_Sine": SineNode,
    "LFO_Sawtooth": SawtoothNode,
    "LFO_Square": SquareNode,
    "LFO_Pulse": PulseNode,
}