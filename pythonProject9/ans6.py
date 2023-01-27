def student_data(info_needed):
    directory = {"student_id":"22106037",
    "student_name" : "Nishtha Mehta",
    "student_stream": "cseds"}
    print(directory.get(f'{info_needed}'))


student_data(str(input('What do you want to know?')))