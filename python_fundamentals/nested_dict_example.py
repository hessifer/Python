def main():
    nested_dict: dict = {
        "hessifer@gmail": {
            "phone": "443.545.4181",
            "fname": "Charles",
            "lname": "Hessifer",
        },
        "xdhessifer@gmail.com": {
            "phone": "443.718.1187",
            "fname": "Xaviera",
            "lname": "Hessifer",
        }
    }

    # display top level keys for nested_dict
    for key, value in nested_dict.items():
        print(f"Key: {key}")
        for k in value.keys():
            print(f"Nested Key: {k}")


if __name__ == "__main__":
    main()
