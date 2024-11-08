from common.utilities import (
    convert_to_packets,
    is_acknowledgement_error,
    is_packet_error,
    is_acknowledgement_lost,
    is_packet_lost,
    print_stats,
)
from common.constants import (
    ACK_TRANSFER_TIME,
    DATA_SIZE,
    PACKET_TRANSFER_TIME,
    TIMEOUT,
)


def rdt3(data: int) -> int:
    total_time: int = 0  # ms
    number_of_packets: int = convert_to_packets(data)
    packets_sent: int = 0

    while packets_sent != number_of_packets:
        print(f"Sending data packet: {packets_sent}")

        if is_packet_lost(packets_sent) or is_acknowledgement_lost(
            packets_sent
        ):
            total_time += TIMEOUT
            continue

        total_time += PACKET_TRANSFER_TIME + ACK_TRANSFER_TIME

        if not is_packet_error(packets_sent) and not is_acknowledgement_error():
            packets_sent += 1

    return total_time


time_taken = rdt3(DATA_SIZE)
print_stats(time_taken)
