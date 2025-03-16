import os
import yaml

# Paths
template_path = 'template.xml'
themes_directory = './themes/'
output_directory = './royalts-output/'  # Define your output directory

# Function to correct indentation in YAML files
def correct_yaml_indentation(yaml_path):
    with open(yaml_path, 'r') as file:
        content = file.readlines()
    
    corrected_content = []
    
    for line in content:
        corrected_line = line.replace('\t', '  ')  # Change '\t' to two spaces
        corrected_content.append(corrected_line)
    
    # Write the corrected content back to the file
    with open(yaml_path, 'w') as file:
        file.writelines(corrected_content)

# Read the template XML file
with open(template_path, 'r') as template_file:
    template_content = template_file.read()

# Loop through all files in the themes directory
for filename in os.listdir(themes_directory):
    if filename.endswith('.yml'):
        yml_path = os.path.join(themes_directory, filename)

        # Correct YAML indentation
        correct_yaml_indentation(yml_path)

        # Read the corrected YAML file
        with open(yml_path, 'r') as yml_file:
            yml_content = yaml.safe_load(yml_file)

        # Fill in the template
        filled_content = template_content
        for key, value in yml_content.items():
            placeholder = f"<{key}>"
            filled_content = filled_content.replace(placeholder, value)

        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Write the filled content to a new XML file with the same name as the YML file
        output_filename = os.path.splitext(filename)[0] + '.rtcp'
        output_path = os.path.join(output_directory, output_filename)

        with open(output_path, 'w') as output_file:
            output_file.write(filled_content)

print("Processing complete. Check the output directory for generated files.")