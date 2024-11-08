from common.utilities import (
    convert_to_packets,
    is_acknowledgement_error,
    is_packet_error,
    print_stats,
)
from common.constants import (
    ACK_TRANSFER_TIME,
    DATA_SIZE,
    PACKET_TRANSFER_TIME,
)


def rdt21(data: int) -> int:
    total_time: int = 0  # ms
    number_of_packets: int = convert_to_packets(data)
    packets_sent: int = 0

    while packets_sent != number_of_packets:
        print(f"Sending data packet: {packets_sent}")
        total_time += PACKET_TRANSFER_TIME

        total_time += ACK_TRANSFER_TIME

        if not is_packet_error(packets_sent) and not is_acknowledgement_error():
            packets_sent += 1

    return total_time


time_taken = rdt21(DATA_SIZE)
print_stats(time_taken)
