def is_a_line_of_page_no(line:str)->bool :
    s = line.strip()
    return s.isnumeric()

with open('output.txt', 'w', encoding='utf-8') as f:
    with open('input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if is_a_line_of_page_no(line) :
                continue
            f.writelines(line)

