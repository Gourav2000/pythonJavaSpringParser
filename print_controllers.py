import os                  # Required for directory traversal
import shutil              # Required for working with temporary directories
import tempfile            # Required for creating temporary directories
import zipfile             # Required for working with zip files
import javalang            # Required for parsing Java source code

# Extract the contents of the zip file to a temporary directory
def extract_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        # Extract the contents of the zip file to the temporary directory
        zip_file.extractall(temp_dir)
        # List the files in the temporary directory
        files_in_temp_dir = os.listdir(temp_dir)
        print(f'Files in temporary directory: {files_in_temp_dir}')
        # Update the temporary directory path to the first extracted directory
        temp_dir = os.path.join(temp_dir, files_in_temp_dir[0])
        # List the files in the updated temporary directory
        files_in_temp_dir = os.listdir(temp_dir)
        print(f'Files in temporary directory: {files_in_temp_dir}')
        # Return the temporary directory path
        return temp_dir

# Load all Java source files in a directory and its subdirectories into memory
def load_files(dir_path):
    files = []
    for root, dirs, filenames in os.walk(dir_path):
        # Traverse the directory tree, and for each file found, add its contents to the `files` list
        for filename in filenames:
            # Check if the file is a Java source file
            if filename.endswith('.java'):
                with open(os.path.join(root, filename), 'r') as f:
                    files.append(f.read())
    # Return the list of Java source files
    return files

# Find all classes that extend the RestController class
def find_rest_controllers(java_sources):
    controllers = set()
    entities=set()
    repositories=set()
    for i in java_sources:
        # Parse the Java source code
        tree = javalang.parse.parse(i)
        for path, node in tree:
            if isinstance(node, javalang.tree.InterfaceDeclaration):
                # Check if the interface extends JpaRepository
                if node.extends is not None:
                    for i in node.extends:
                        if 'JpaRepository' in i.name:
                            repositories.add(node.name)
                # Check if the interface is annotated with @RestController, @Controller or @RequestMapping
                for annotation in node.annotations:
                    if isinstance(annotation, javalang.tree.Annotation):
                        if annotation.name == 'RestController' or annotation.name == 'Controller' or annotation.name == 'RequestMapping':
                            controllers.add(node.name)
                        # Check if the interface is annotated with @Entity
                        if annotation.name == 'Entity':
                            entities.add(node.name)
                
            if isinstance(node, javalang.tree.ClassDeclaration):
                # Check if the class is annotated with @RestController, @Controller or @RequestMapping
                for annotation in node.annotations:
                    if isinstance(annotation, javalang.tree.Annotation):
                        if annotation.name == 'RestController' or annotation.name == 'Controller' or annotation.name == 'RequestMapping':
                            controllers.add(node.name)
                        # Check if the class is annotated with @Entity
                        if annotation.name == 'Entity':
                            entities.add(node.name)
                    
    # Return a dictionary with the lists of controllers, entities and repositories found
    return {"controllers": controllers, "entities": entities, "repositories": repositories}

# Example usage
zip_file_path = 'Spring-Boot-Sample-Project.zip'
extracted_dir = extract_zip(zip_file_path)      # Extract the contents of the zip file
print(extracted_dir)
java_source = load_files(extracted_dir)  
# Load all Java source files
rest_controllers = find_rest_controllers(java_source)   # Find all controllers that extend RestController
print(rest_controllers['controllers'])  # Print the list of controllers found
print(rest_controllers['entities'])     # Print the list of entities found                            
print(rest_controllers['repositories']) # Print the list of repositories found
shutil.rmtree(extracted_dir) # delete the temp directory