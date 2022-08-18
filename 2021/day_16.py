import functools
from typing import Tuple

from python_utils import get_input


class Packet:
    def __init__(self, version: int, type_id: int):
        self.version = version
        self.type_id = type_id
        self.values = []
        self.sub_packets = []
        self.length = 0

    def total_version(self) -> int:
        return self.version + sum([p.total_version() for p in self.sub_packets])

    def result(self):
        if self.type_id == 4:
            return int(''.join(self.values), 2)
        elif self.type_id == 0:
            return sum([p.result() for p in self.sub_packets])
        elif self.type_id == 1:
            return functools.reduce(lambda x, y: x * y, [p.result() for p in self.sub_packets])
        elif self.type_id == 2:
            return min([p.result() for p in self.sub_packets])
        elif self.type_id == 3:
            return max([p.result() for p in self.sub_packets])
        elif self.type_id == 5:
            return self.sub_packets[0].result() > self.sub_packets[1].result()
        elif self.type_id == 6:
            return self.sub_packets[0].result() < self.sub_packets[1].result()
        elif self.type_id == 7:
            return self.sub_packets[0].result() == self.sub_packets[1].result()


def parse_packet(text: str, pos: int, is_subpacket: bool) -> Tuple[Packet, int]:
    version = int(text[pos:pos + 3], 2)
    type_id = int(text[pos + 3:pos + 6], 2)
    pos = pos + 6
    packet_length = 6
    packet = Packet(version, type_id)

    if type_id == 4:
        stop = False
        while not stop:
            stop = text[pos] == '0'
            packet.values.append(text[pos + 1:pos + 5])
            pos += 5
            packet_length += 5
    else:
        length_type_id = int(text[pos], 2)
        num_bits = 11 if length_type_id else 15
        length = int(text[pos + 1:pos + 1 + num_bits], 2)
        pos += 1 + num_bits
        packet_length += 1 + num_bits
        while length > 0:
            sub_packet, pos = parse_packet(text, pos, True)
            packet.sub_packets.append(sub_packet)
            length -= sub_packet.length if length_type_id == 0 else 1
            packet_length += sub_packet.length

    # pos += packet_length % 4 if not is_subpacket else 0
    packet.length = packet_length
    return packet, pos


def d16p1(text: str):
    text = ''.join([bin(int(x, 16))[2:].zfill(4) for x in text])

    # We have a single packet so we can simply call a recursive func
    packet, _ = parse_packet(text, 0, False)

    return packet.total_version()


def d16p2(text: str):
    text = ''.join([bin(int(x, 16))[2:].zfill(4) for x in text])

    # We have a single packet so we can simply call a recursive func
    packet, _ = parse_packet(text, 0, False)

    return packet.result()


if __name__ == '__main__':
    text = get_input(16, 2021)
    text = text.replace('\n', '')
    # text = "C200B40A82"
    print(f"Part 1: {d16p1(text)}")
    print(f"Part 2: {d16p2(text)}")
