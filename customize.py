import os

def getValues():
    replacements = {
        "explorer-server-ip": input("Enter value for explorer-server-ip: "),
        "node-server-ip": input("Enter value for node-server-ip: "),
        "custom-currency-name": input("Enter value for custom-currency-name: "),
        "custom-currency-symbol": input("Enter value for custom-currency-symbol: "),
        "custom-chainid": input("Enter value for custom-chainid: "),
        "custom-network-name": input("Enter value for custom-network-name: "),
        "custom-logo-url": input("Enter value for custom-logo-url: ")
    }
    return replacements

def replaceInFile(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    for key, value in replacements.items():
        content = content.replace(key, value)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def replaceInDir(directory, replacements):
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            dirs.remove('.git') 
        for file in files:
            file_path = os.path.join(root, file)
            replaceInFile(file_path, replacements)

if __name__ == "__main__":
    replacements = getValues()
    docker_compose_dir = os.path.join(os.getcwd(), 'docker-compose')  
    replaceInDir(docker_compose_dir, replacements)
    print("Replacement complete.")
