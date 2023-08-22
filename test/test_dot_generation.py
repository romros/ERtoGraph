import os
import json
from app.dot_generator import generate_dot_from_json
# Si tens una funció `dot_to_svg` en `graph_utils.py`:
from app.graph_utils import dot_to_svg


def load_fixture(filename):
    with open(f'test/fixtures/{filename}', 'r') as file:
        return json.load(file)


def test_generate_dot_from_example1():
    # Carrega l'exemple de JSON
    example_data = load_fixture('example1.json')

    # Genera el codi DOT utilitzant la funció
    result_dot = generate_dot_from_json(example_data)

    # Opcionalment, si vols comprovar la generació d'SVG i DOT:
    dot_path, svg_path = dot_to_svg(
        result_dot, "app/static/generated_svgs", "example1")
    assert os.path.exists(dot_path)  # assegura't que el DOT s'ha creat
    assert os.path.exists(svg_path)  # assegura't que l'SVG s'ha creat


def test_generate_dot_from_example2():
    # Carrega l'exemple de JSON
    example_data = load_fixture('example2.json')

    # Genera el codi DOT utilitzant la funció
    result_dot = generate_dot_from_json(example_data)

    # Opcionalment, si vols comprovar la generació d'SVG i DOT:
    dot_path, svg_path = dot_to_svg(
        result_dot, "app/static/generated_svgs", "example2")
    assert os.path.exists(dot_path)  # assegura't que el DOT s'ha creat
    assert os.path.exists(svg_path)  # assegura't que l'SVG s'ha creat
