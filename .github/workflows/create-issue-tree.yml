name: Create Issue Tree

on:
  workflow_dispatch:
    inputs:
      template_file:
        description: 'Path to template YAML (default: .github/issue-tree-template.yaml)'
        required: true
        default: '.github/issue-tree-template.yaml'

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      contents: read
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install PyYAML requests

      - name: Run issue tree creator
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          REPO: ${{ github.repository }}
        run: python .github/scripts/create_issue_tree.py "${{ github.event.inputs.template_file }}"
