import yaml

resume = {
    'name': 'Никита',
    'age': 28,
    'languages': 'Python',
    'kek': True
}


with open('YAML_write_test.yaml', 'w', encoding='utf-8') as yaml_write_test:
    yaml.dump(data=resume, stream=yaml_write_test, allow_unicode=True)

print(yaml_write_test)

with open('YAML_read_test.yaml', 'r', encoding='utf-8') as yaml_read_test:
    yaml_read_test_data = yaml.safe_load(yaml_read_test)

print(yaml_read_test_data)
print(yaml_read_test_data['kek'],type(yaml_read_test_data['kek']))