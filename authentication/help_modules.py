

# app constants
# size constants
LENGTH = int(64)
LONG_LENGTH = int(LENGTH * 2)
BIG_LENGTH = int(LENGTH * 4)
SHORT_LENGTH = int(LENGTH / 2)
SMALL_LENGTH = int(LENGTH / 4)


# remove required fields with values
# from required_fields array
# return improper fields
def validate_fields(required_fields):
    for key in list(required_fields):
        if required_fields[key]:
            del required_fields[key]

    return required_fields

