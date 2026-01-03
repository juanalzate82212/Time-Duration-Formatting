def format_duration(seconds):
    if seconds == 0:
        return "now"

    # Define the time units in seconds
    units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]

    parts = []
    for name, unit_seconds in units:
        # Calculate how many of this unit fit into the remaining seconds
        value, seconds = divmod(seconds, unit_seconds)
        
        if value > 0:
            # Handle pluralization
            label = f"{name}s" if value > 1 else name
            parts.append(f"{value} {label}")

    # Join the parts with commas and "and"
    if len(parts) == 1:
        return parts[0]
    else:
        # Join all but the last part with commas, then add the last part with "and"
        return ", ".join(parts[:-1]) + " and " + parts[-1]

# Examples
print(format_duration(62))    # "1 minute and 2 seconds"
print(format_duration(3662))  # "1 hour, 1 minute and 2 seconds"