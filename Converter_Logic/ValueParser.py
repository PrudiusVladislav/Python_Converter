
class ValueParser:

    @staticmethod
    def get_available_digits():
        return "0123456789ABCDEF";

    @staticmethod
    def try_parse_to_float(string):
        try:
            result = float(string);
            return True, result;
        except ValueError:
            return False, None;

    @staticmethod
    def try_parse_int(string):
        try:
            value = int(string);
            return True, value;
        except ValueError:
            return False, None;

    @staticmethod
    def try_parse_to_binary(string):
        if string[:2] != "0b":
            return False, None;
        string_without_prefix = string[2:];
        for char in string_without_prefix:
            if char != '0' and char != '1':
                return False, None;

        return True, [int(num) for num in string_without_prefix];

    @staticmethod
    def try_parse_to_hex(string):
        if string[:2] != "0x":
            return False, None;

        return ValueParser.try_parse_to_float(string[2:]);

    @staticmethod
    def validate_any_base_number(string_number, base):
        available_digits = ValueParser.get_available_digits();
        for char in string_number:
            if char not in available_digits[:base]:
                return False, None;
        return True, string_number.lstrip('0');

