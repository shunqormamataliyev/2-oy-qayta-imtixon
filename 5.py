def data_to_str(data: str):
    result = ''
    for i in data:
        if i.isalpha():
            result += i
    return result

data = "AI-powered spreadsheets help you and your team manage, visualize and analyze data."
print(data_to_str(data))
