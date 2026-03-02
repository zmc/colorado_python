def validate_attribute_lengths(obj: object, lengths: dict[str, int]) -> None:
    # Validate that the abbreviations are all uppercase and have the correct lengths
    for attr_name, expected_length in lengths.items():
        attr_value = getattr(obj, attr_name)

        if not isinstance(attr_value, str):
            raise ValueError(f"{attr_name} must be a string")

        if not attr_value.isupper():
            raise ValueError(f"{attr_name} must be uppercase")

        if not len(attr_value) <= expected_length:
            raise ValueError(f"{attr_name} must be <={expected_length} characters long")
