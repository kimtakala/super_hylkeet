'''
This module generates bibTeX references in the following format:
@type{key,
    field1      = "value1",
    field2      = "value2",
}
'''
from entities.citation import Citation


def generate_reference(citation_data: "Citation") -> str:
    '''
    takes a class:Citation object and returns a string
    with all of the data in the BibTeX reference format.
    '''

    ignored_fields = ["type", "id", "timestamp"]
    all_data = citation_data.all_data
    bibtex_reference = "@" + str(all_data['type']) + "{"\
        + str(all_data['key']) + ",\n"
    for key, data in all_data.items():
        if key in ignored_fields:
            continue
        if key == 'year':
            bibtex_reference += f'{key:<12} = {data},\n'
            continue
        bibtex_reference += f'{key:<12} = "{data}",\n'
    return bibtex_reference + "}"


def generate_references(lst: list["Citation"]) -> list:
    '''
    returns a list of strings that contain the references
    in the correct BibTeX reference format.
    '''
    result_list = []
    for cit in lst:
        result_list.append(generate_reference(cit))
    return result_list
