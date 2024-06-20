import re
# Xaero format
# waypoint:name:initials:x:y:z:color:disabled:type:set:rotate_on_tp:tp_yaw:visibility_type:destination
# EX: waypoint:hello:H:-361:83:393:8:false:0:gui.xaero_default:false:0:0:false


# Steps to format voxel file for xaero transfer
# 1. Remove the x:, y:, z:
# 2. Turn string into list by splitting at the commas
# 2.1. Remove the special case ~comma~
# 2.2. replace name with waypoint
# 3. swap z & y from voxel to y & z
# 4. append everything together
# 5. write to text file END
def main():
    finalAppend = "8:false:0:gui.xaero_default:false:0:0:false\n"

    with open("VoxelWaypoints.txt", 'r') as voxelFile:
        with open("XaeroWaypoints.txt", 'w') as xaeroFile:

            for line in voxelFile:
                # Find and replace to almost match format of xaero
                formattedWaypoint = re.sub("(x:|y:|z:)", '', line)
                formattedWaypoint = re.sub("~comma~", '', formattedWaypoint)
                formattedWaypoint = re.sub("name", 'waypoint', formattedWaypoint)
                formattedWaypoint = re.split(",|:", formattedWaypoint)

                # Split formatted string into a list
                i = len(formattedWaypoint) - 1
                while i != 4:
                    formattedWaypoint.pop(i)
                    i -= 1

                # Use the first character of the name as the xaero waypoint Initial letter
                firstString = formattedWaypoint[1]
                firstChar = firstString[0]

                # Swap the y & z coordinates from voxel to xaero's layout
                temp = formattedWaypoint[3]
                formattedWaypoint[3] = formattedWaypoint[4]
                formattedWaypoint[4] = temp

                # Add remaining strings to be appended together and write to xaero's file
                formattedWaypoint.insert(2, firstChar)
                formattedWaypoint.append(finalAppend)
                formattedWaypoint = ':'.join(formattedWaypoint)
                xaeroFile.write(formattedWaypoint)

        xaeroFile.close()
    voxelFile.close()


if __name__ == "__main__":
    main()