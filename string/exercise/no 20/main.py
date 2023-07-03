"""
Write a program that converts a time from one time zone to another. The user enters the time
in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters
is that of the original time and the second is the desired time zone. The possible time zones
are Eastern, Central, Mountain, or Pacific.
Time: 11:48pm
Starting zone: Pacific
Ending zone: Eastern
2:48am

"""


def twenty():
    TIMEZONE_OFFSETS = {
        'Eastern': -5,
        'Central': -6,
        'Mountain': -7,
        'Pacific': -8
    }

    # Get user input
    time_input = input("Enter the time (e.g., 3:48pm or 11:26am): ")
    original_timezone = input("Enter the original time zone (Eastern, Central, Mountain, or Pacific): ")
    desired_timezone = input("Enter the desired time zone (Eastern, Central, Mountain, or Pacific): ")

    # Convert time input to 24-hour format
    time_parts = time_input[:-2].split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    ampm = time_input[-2:].lower()
    if ampm == 'pm' and hour != 12:
        hour += 12
    elif ampm == 'am' and hour == 12:
        hour = 0

    # Calculate time zone differences
    original_offset = TIMEZONE_OFFSETS[original_timezone]
    desired_offset = TIMEZONE_OFFSETS[desired_timezone]
    hour_difference = desired_offset - original_offset

    # Perform time conversion
    converted_hour = (hour + hour_difference) % 24

    # Format the converted time
    converted_ampm = 'am' if converted_hour < 12 else 'pm'
    converted_hour = converted_hour if converted_hour <= 12 else converted_hour - 12
    converted_time = f"{converted_hour:02d}:{minute:02d}{converted_ampm}"

    # Display the converted time
    print(f"The converted time is: {converted_time}")


twenty()

