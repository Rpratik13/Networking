import random

from common.constants import DATA_SIZE, ERROR_RATE, LOSS_RATE, PACKET_SIZE


def convert_to_packets(data: int) -> int:
    return (data // PACKET_SIZE) + (0 if (data % PACKET_SIZE) == 0 else 1)


def is_acknowledgement_error():
    is_acknowledgement_errored: bool = random.random() < ERROR_RATE

    if is_acknowledgement_errored:
        print(f"Error in acknowledgement")

    return is_acknowledgement_errored


def is_acknowledgement_lost(packet_number: int):
    acknowledgement_lost: bool = random.random() < LOSS_RATE

    if acknowledgement_lost:
        print(f"Data packet {packet_number} arrived at destination")
        print(f"Acknowledgement lost")

    return acknowledgement_lost


def is_packet_error(packet_number: int):
    is_packet_errored: bool = random.random() < ERROR_RATE

    if is_packet_errored:  # Error sending packet
        print(f"Error in packet: {packet_number}")
    else:
        print(f"Data packet {packet_number} arrived at destination")

    return is_packet_errored


def is_packet_lost(packet_number: int):
    packet_lost: bool = random.random() < LOSS_RATE

    if packet_lost:
        print(f"Data packet: {packet_number} lost")

    return packet_lost


def print_stats(time_taken: int) -> None:
    print(f"\nTotal time taken: {time_taken}")
    print(f"Throughput: {round(DATA_SIZE / time_taken, 2)}")
