# Privilee QA Automation Assessment

This repository contains automated tests for the Privilee website and API, created as part of the QA Engineer assessment.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Test Scenarios](#test-scenarios)
- [GitHub Actions Workflow](#github-actions-workflow)

## Overview
This assessment evaluates the main features of the Privilee website ([Map page](https://staging-website.privilee.ae/map)) and validates selected API endpoints from [GoRest](https://gorest.co.in/).  

The repository contains:
- UI tests covering functionality, user interface, performance, and data accuracy.
- API tests validating different endpoints.
- CI workflow to run tests automatically on GitHub Actions and generate test reports.

## Requirements
- Python 3.14+
- The following Python packages (listed in `requirements.txt`):
- pytest==9.0.2
- playwright==1.39.1
- requests==2.32.0
- Pillow==10.0.0
- pytest-xdist==3.2.2

## Setup
1. Clone the repository:
git clone <your-repo-url>
cd privilee-qa
2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
3. Install dependencies:
pip install --upgrade pip
pip install -r requirements.txt
4. Install Playwright browsers:
playwright install

## Running Tests
1. Run all UI tests:
pytest tests/ui --maxfail=1 --disable-warnings --junitxml=ui-test-results.xml
2. Run all API tests:
pytest tests/api --maxfail=1 --disable-warnings --junitxml=api-test-results.xml
3. Run all tests together:
pytest tests --maxfail=1 --disable-warnings

Screenshots from UI tests will be saved in the tests/ui/ folder (e.g., map_center_click.png).

## Test Scenarios
UI Tests
1. Map Container Visible
- Feature: Mapbox canvas container
- Expected Outcome: Canvas exists and has non-zero dimensions
- Setup: Open Map page in browser
- Importance: Verifies the main map element renders correctly (Functionality/UI)

2. Map Responsive
- Feature: Canvas resizing on different viewports
- Expected Outcome: Canvas size changes between desktop and mobile
- Setup: Open Map page and adjust viewport
- Importance: Ensures responsive design works (UI/Functionality)

3. Click Map Center
- Feature: Interactivity with map
- Expected Outcome: Click action does not break the map; screenshot confirms
- Setup: Open Map page and click canvas center
- Importance: Verifies user interaction works (Functionality/Data Accuracy)

4. Map Tiles Loaded
- Feature: Map rendering/performance
- Expected Outcome: Canvas is non-empty within 10s
- Setup: Open Map page and wait for tiles
- Importance: Ensures map content loads and performance is acceptable (Performance/Data Accuracy)

5. Map Zoom In/Out
- Feature: Zoom functionality via mouse wheel
- Expected Outcome: Canvas renders after zoom in/out
- Setup: Open Map page, move mouse to canvas center, perform wheel actions
- Importance: Validates interactive functionality (Functionality/UI)

API Tests
Endpoints:
/public/v2/users
/public/v2/posts
/public/v2/users/7373665/posts
/public/v2/todos

Validation: Response status, data format, and content correctness
Importance: Verifies API reliability and data integrity

## GitHub Actions Workflow
- Workflow file: .github/workflows/tests.yml
- Automatically runs tests on push or pull request to main
- Generates JUnit XML reports for UI and API tests
- Uploads screenshots and test reports as artifacts