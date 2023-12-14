import math

# constant distance values for a standard keyboard

# size (height & width) in mm
keysize = 19.05

# Offset of the second and third row on the keyboard with respect to the first
row1_offset = 0.25 * keysize
row2_offset = 0.75 * keysize

# Compute the middle position (x, y) of every key
key_positions = {
    0: [(0.5 * keysize + keysize * i, 0.5 * keysize) for i in range(0, 12)],
    1: [(0.5 * keysize + keysize * i + row1_offset, 1.5 * keysize) for i in range(0, 11)],
    2: [(0.5 * keysize + keysize * i + row2_offset, 2.5 * keysize) for i in range(0, 10)],
}

# What fingers is used for what column on the keyboard
col_finger = [0, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]

layout_keys = {
    "qwerty": [
        "qwertyuiop[]",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ],
    "colemak": [
        "qwfpbjluy;[]",
        "arstgmneio'",
        "xcdvzkh,./",
    ],
    "colemakdh": [
        "qwfpgjluy;[]",
        "arstdhneio'",
        "zxcvbkm,./",
    ],
    "dvorak": [
        "',.pyfgcrl/=",
        "aoeuidhtns-",
        ";qjkxbmwvz",
    ],
}

layouts = {}

for layout, keys in layout_keys.items():
    layouts[layout] = {}
    for i, row in enumerate(keys):
        for j, char in enumerate(row):
            layouts[layout][char] = (key_positions[i][j], col_finger[j])

print(layouts["qwerty"])


def get_distance(char1, char2, layout):
    if not char1.isalpha() or not char2.isalpha():
        raise ValueError("Characters must be alphabetic")

    if layout not in layouts:
        raise ValueError("Layout not supported")

    pos1, _ = layouts[layout][char1.lower()]
    pos2, _ = layouts[layout][char2.lower()]

    return math.sqrt(abs(pos1[0] - pos2[0]) ** 2 + abs(pos1[1] - pos2[1]) ** 2)


print(get_distance("a", "b", "qwerty"))
print(get_distance("b", "q", "qwerty"))
print(get_distance("g", "c", "qwerty"))
print(get_distance("h", "j", "qwerty"))
print(get_distance("l", "j", "qwerty"))
print(get_distance("p", "x", "qwerty"))
print(get_distance("y", "y", "qwerty"))
