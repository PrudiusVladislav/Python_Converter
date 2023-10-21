from enum import Enum;


class ConvertMethodEnum(Enum):
    DecimalToBinary = 1,
    BinaryToDecimal = 2,
    DecimalToHex = 3,
    HexToDecimal = 4,
    BinaryToHex = 5,
    HexToBinary = 6