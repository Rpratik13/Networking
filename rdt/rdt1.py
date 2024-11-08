from common.utilities import convert_to_packets, print_stats
from common.constants import DATA_SIZE, PACKET_TRANSFER_TIME


def rdt1(data: int) -> int:
    total_time: int = 0  # ms
    number_of_packets: int = convert_to_packets(data)

    for i in range(number_of_packets):
        print(f"Sending data packet: {i}")
        total_time += PACKET_TRANSFER_TIME
        print(f"Data packet {i} arrived at destination")

    return total_time


time_taken = rdt1(DATA_SIZE)
print_stats(time_taken)
