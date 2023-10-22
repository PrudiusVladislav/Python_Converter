
from Converter_Logic.ValueParser import ValueParser;


class Converter:

    @staticmethod
    def convert(string_number, source_base, target_base):
        if source_base == target_base:
            return True, string_number;
        if not (2 <= source_base <= 16 and 2 <= target_base <= 16):
            return False, "Invalid source base or target base specified (bases supported: 2-16)";
        validate_status, validate_res = ValueParser.validate_any_base_number(string_number, source_base);
        if not validate_status:
            return False, "Invalid input number";

        if source_base == 10:
            return True, Converter.convert_decimal_to_any_base(int(string_number), target_base);
        if target_base == 10:
            return True, Converter.convert_to_decimal(string_number, source_base)

        return True, Converter.convert_decimal_to_any_base(Converter.convert_to_decimal(string_number, source_base),
                                                           target_base);

    @staticmethod
    def convert_to_decimal(string_number, base):
        available_digits = ValueParser.get_available_digits();
        result = 0
        power = 0

        for digit in reversed(string_number):
            if digit not in available_digits[:base]:
                return "Invalid digit in the number"

            digit_value = available_digits.index(digit)
            result += digit_value * (base ** power)
            power += 1

        return result

    @staticmethod
    def convert_decimal_to_any_base(decimal_number, base):
        available_digits = ValueParser.get_available_digits();

        result = "";
        while decimal_number > 0:
            remainder = decimal_number % base
            result = available_digits[remainder] + result
            decimal_number //= base

        return result



