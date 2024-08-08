#!/usr/bin/python3
from models.base_model import BaseModel

def test_base_model():
    """Test the BaseModel class."""
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89

    print(my_model)  # Should show the initial state with default attributes

    my_model.save()  # Update the updated_at attribute
    print(my_model)  # Should show the updated state

    my_model_json = my_model.to_dict()  # Convert to dictionary
    print(my_model_json)  # Should show dictionary representation

    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

if __name__ == "__main__":
    test_base_model()
