

class Converter:

    @staticmethod
    def convert_decimal_to_binary(decimal_num):
        if decimal_num == 0:
            return '0';

        binary = '';
        power = 0;
        while 2 ** power <= decimal_num:
            power += 1;

        power -= 1;

        while power >= 0:
            if 2 ** power <= decimal_num:
                binary += '1';
                decimal_num -= 2 ** power;
            else:
                binary += '0';

            power -= 1;

        return binary;

    @staticmethod
    def convert_binary_to_decimal(binary_num):
        result_decimal = 0;

        for i in range(len(binary_num)):
            if binary_num[i] == '1':
                result_decimal += 2 ** (len(binary_num) - i - 1);

        return result_decimal;

    @staticmethod
    def convert_decimal_to_hex(decimal_num):
        result_array = [];
        whole_fraction = decimal_num;
        remaining = whole_fraction % 16;
        while remaining > 0:
            whole_fraction //= 16;
            remaining = whole_fraction % 16;
            result_array.append(remaining);

    # @staticmethod
    # def format_array_to_hex(array):
        # for el
