def generate_entities_dot(entities):
    dot_output = []

    for entity in entities:
        entity_name = entity["NAME"].upper()

        if entity.get("IS_WEAK_ENTITY"):
            dot_output.append(
                f'"{entity_name}" [shape=box, style="rounded,dashed", label="{entity_name}"];')
        else:
            dot_output.append(
                f'"{entity_name}" [shape=box, label="{entity_name}"];')

    return "\n".join(dot_output)


def generate_attributes_dot(entities):
    dot_output = []

    for entity in entities:
        entity_name = entity["NAME"].upper()

        for attribute in entity.get("ATTRIBUTES", []):
            attribute_name = f'{entity_name}_{attribute["NAME"]}'
            display_name = attribute["NAME"]
            attribute_type = attribute.get("TYPE", "NORMAL")
            key_type = attribute.get("KEY_TYPE", "NONE")

            shape = "ellipse"
            style = ""
            width = "0.5"
            height = "0.3"

            if attribute_type == "COMPOSITE":
                style = "filled"
            elif attribute_type == "MULTIVALUED":
                shape = "doublecircle"
            elif attribute_type == "DERIVED":
                style = "dashed"

            if key_type == "PK":
                display_name = f'<u>{display_name}</u>'

            dot_output.append(
                f'"{attribute_name}" [shape={shape}, style="{style}", label=< {display_name} >, width={width}, height={height}, fontsize="10"];')
            dot_output.append(
                f'"{entity_name}" -- "{attribute_name}" [dir=none];')

    return "\n".join(dot_output)


def generate_relationships_dot(relationships):
    dot_output = []

    for relationship in relationships:
        relationship_name = relationship["NAME"].upper()

        dot_output.append(
            f'"{relationship_name}" [shape=diamond, style=filled, color=black, fillcolor=lightgrey, label="{relationship_name}"];')

        for entity in relationship["ENTITIES"]:
            entity_name = entity["NAME"].upper()
            cardinality = entity.get("CARDINALITY", "")

            dot_output.append(
                f'"{relationship_name}" -- "{entity_name}" [label="{cardinality}", dir=none];')

    return "\n".join(dot_output)


def generate_dot_from_json(json_model):
    entities = json_model.get("ENTITIES", [])
    relationships = json_model.get("RELATIONSHIPS", [])

    dot_parts = [
        "graph ConceptualModel {",
        "rankdir=LR;",
        "layout=neato;",
        generate_entities_dot(entities),
        generate_attributes_dot(entities),
        generate_relationships_dot(relationships),
        "}"
    ]

    return "\n".join(dot_parts)
