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
    WINDOW_SIZE,
)


def go_back_n(data: int) -> int:
    total_time: int = 0  # ms
    number_of_packets: int = convert_to_packets(data)
    base_position: int = 0

    while base_position < number_of_packets:
        base_increment: int = 0
        for i in range(min(WINDOW_SIZE, number_of_packets - base_position)):
            packet_number: int = base_position + i
            print(f"Sending data packet: {packet_number}")

            if is_packet_lost(packet_number) or is_acknowledgement_lost(
                packet_number
            ):
                break

            if is_packet_error(packet_number) or is_acknowledgement_error():
                break

            base_increment += 1
        else:
            base_position += base_increment
            total_time += PACKET_TRANSFER_TIME + ACK_TRANSFER_TIME
            continue

        total_time += TIMEOUT
        print("Timeout")
        base_position += base_increment

    return total_time


time_taken = go_back_n(DATA_SIZE)
print_stats(time_taken)
