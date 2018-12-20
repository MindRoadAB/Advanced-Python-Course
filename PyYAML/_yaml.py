import yaml

# Exercise 8
from yaml import load, dump, safe_dump


def yaml_read(data):
    """ Load a yaml file """
    with open("test.yaml", 'r') as f:
        cur_yaml = yaml.safe_load(f)  # Note the safe_load
        cur_yaml.update(data)
        #print(cur_yaml)
        # _loderdata = load(file)
        # print(dump(_loderdata, default_flow_style=False))
        """To Print the result awesomely :D """
        from pprint import pprint as awesome
        awesome(cur_yaml)
    if cur_yaml:
        with open("test.yaml", 'w') as fil:
            safe_dump(cur_yaml, fil)


def yaml_dump(new_data, _new_file):
    """Dumps data to a yaml file"""
    with open(_new_file, 'w') as file:
        safe_dump(new_data, file, default_flow_style=False, allow_unicode=True)

_new_file = "dump_file.yaml"
if __name__ == "__main__":
    data = {
        "MindRoad": {
            "Embedded Group": ["Anders", "Tony"],
            "Academy": ["Mattias", "Tony"],
            "Birth": 2016,
            "Courses": {
                '1': 'Python',
                '2': 'Advanced Python',
                '3': 'Embedded Linux',
                '4': 'Advanced JavaScript'
            },
            "Programming Languages": {'markup': ['HTML', 'XML'],
                                      "Programming": ['C#', 'C++', 'Python', 'JavaScript']},
        }
    }

yaml_read(data)
yaml_dump(data, _new_file)



# Exercise 9

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return self.name + " Age:" + self.age + ", Salary:" + self.salary


_employee = Employee('Tony', 31, 27500)
print(dump(_employee, default_flow_style=False))

# Store YAML in file
with open("out.yaml", "w") as file:
    dump(_employee, file)

