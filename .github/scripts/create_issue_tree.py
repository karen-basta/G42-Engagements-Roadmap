import sys
import yaml

def main(template_path):
    with open(template_path, "r") as f:
        data = yaml.safe_load(f)
    print(data)  # For now, just print. Replace this with GitHub API calls to create issues.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_issue_tree.py <template_path>")
        sys.exit(1)
    main(sys.argv[1])
