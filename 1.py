from datetime import datetime
def string_to_date(date_str: str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d" ).date()
    except ValueError:
        return "Error type of string"



print(string_to_date("2024-01-01"))