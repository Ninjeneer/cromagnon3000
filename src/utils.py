def clear_config(lines: list) -> list:
    output = []
    for line in lines:
        if not line.startswith('#') and not line.startswith('\n'):
            output.append(line)
    return output