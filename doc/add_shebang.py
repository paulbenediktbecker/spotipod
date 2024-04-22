import os
import glob

def add_shebang_to_pl_files(folder_path):
    # Navigate to the specified folder
    os.chdir(folder_path)

    # List all .pl files in the folder
    pl_files = glob.glob("*.pl")

    # Iterate over each .pl file
    for file_name in pl_files:
        file_path = os.path.join(folder_path, file_name)

        # Read the content of the file
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Add shebang as the first line if it's not already there
        if len(lines) == 0 or not lines[0].startswith("#!/usr/bin/perl"):
            lines.insert(0, "#!/usr/bin/perl\n")

        # Write the modified content back to the file
        with open(file_path, 'w') as f:
            f.writelines(lines)

if __name__ == "__main__":
    folder_path = "/home/becker/git/gnupod/src"  # Specify the folder path here
    add_shebang_to_pl_files(folder_path)