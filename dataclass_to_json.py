import dataclasses
import json

def dataclass_to_json(data_class_obj):
    """
    Convert a data class object into JSON format.

    Args:
        data_class_obj: An instance of a data class.

    Returns:
        str: The JSON representation of the data class object.
    """
    if not dataclasses.is_dataclass(data_class_obj):
        raise ValueError("Input object is not a data class.")

    def _convert_to_json(obj):
        json_data = {}
        for field in dataclasses.fields(obj):
            field_value = getattr(obj, field.name)

            if dataclasses.is_dataclass(field_value):
                json_data[field.name] = _convert_to_json(field_value)
            else:
                json_data[field.name] = field_value
        return json_data

    return json.dumps(_convert_to_json(data_class_obj), indent=4)

