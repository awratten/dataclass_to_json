# Data Class to JSON Converter

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This Python utility provides a simple way to convert data class objects into JSON format. The `dataclass_to_json` function takes an instance of a data class as input and returns its JSON representation.

## Usage

```python
import dataclasses
import json

def dataclass_to_json(data_class_obj):
    # ... (code snippet provided in the repository)

# Example usage
@dataclasses.dataclass
class Person:
    name: str
    age: int
    address: str

person_obj = Person(name="John Doe", age=30, address="123 Main St")
json_representation = dataclass_to_json(person_obj)
print(json_representation)
```

## How it works

The `dataclass_to_json` function converts the provided data class object into a JSON string by recursively traversing the data class attributes. If an attribute is another data class, it creates a nested JSON object for it. Otherwise, it includes the attribute as a key-value pair in the JSON structure.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to [open an issue](https://github.com/yourusername/dataclass-json-converter/issues) or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Note: This utility is inspired by the Python `dataclasses` module and uses the `json` module for JSON serialization.*
