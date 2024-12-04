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
    takes a class:Citation object and returns a string with all of the data in the BibTeX reference format.
    '''

    ignored_fields = ["type", "id", "timestamp"]
    all_data = citation_data.all_data
    # print(f'{all_data}')
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
    returns a list of strings that contain the references in the correct BibTeX reference format.
    '''
    result_list = []
    for cit in lst:
        result_list.append(generate_reference(cit))
    return result_list

# if __name__ == "__main__":
# #     '''
# #     COLUMN_NAMES = [
# #     "id",
# #     "key",
# #     "type",
# #     "title",
# #     "year",
# #     "pages",
# #     "volume",
# #     "publisher",
# #     "doi",
# #     "tags",
# #     "booktitle",
# #     "citation_url",
# #     "timestamp"
# # ]
# #     '''
#     data_1 = [
#         "1",
#         "exampleKey",
#         "book",
#         "Example Book Title",
#         "2023",
#         "123-456",
#         "1",
#         "Example Publisher",
#         "10.1234/example.doi",
#         "example, book",
#         "Example Book Title",
#         "http://example.com",
#         "2023-10-01"
#     ]
#     citation = Citation(data_1)

#     # Generate the reference
#     reference = generate_reference(citation)

#     # Print the generated reference
#     print(reference)
