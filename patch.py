import os
import math
from functions import *

def ttyd_patch(patch_folder, ratio_value, scaling_factor, visual_fixes):

    visual_fixesa = visual_fixes[0]

    scaling_factor = float(scaling_factor)
    ratio_value = float(ratio_value)
    print(f"The scaling factor is {scaling_factor}.")
    hex_value = make_hex(ratio_value, 1)
    hex_value2, hex_value3 = ttyd_hex23(ratio_value)
    version_variables = ["1.0.0"]
    for version_variable in version_variables:
        file_name = f"{version_variable}.pchtxt"
        file_path = os.path.join(patch_folder, file_name)

        if version_variable == "1.0.0":
            nsobidid = "78F37BB55D015BE3B368EC22AF595455F1544DC1"
            visual_fix = visual_fixesa
            

        patch_content = f'''@nsobid-{nsobidid}

@flag print_values
@flag offset_shift 0x100

@enabled
002f25c8 {hex_value2}
002f25cc {hex_value3}
@stop

{visual_fix}

// Generated using ttyd-AAR by Fayaz (github.com/fayaz12g/ttyd-aar)'''
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as patch_file:
            patch_file.write(patch_content)
        print(f"Patch file created: {file_path}")

# This works by doing the following:
# fmov s1, #Rounded_Ratio
# movz w9, #0xe38e
# movk w9, #0x4018, lsl #16
# The last two are the floating point in hex, split with the last 4 then the first 4