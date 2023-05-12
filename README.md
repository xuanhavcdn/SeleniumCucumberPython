# Project struture
```javascript
project_folder/
    |- features/
    |   |- testUploadFile.feature
    |- pages/
    |   |- uploadFilePage.py
    |- steps/
    |   |- uploadFileSteps.py
```
# Setup
## Download and install:
### Install Homedrew:
```javascript
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
More info: https://brew.sh/
### Install Python
```javascript
brew install python
```
### Check Python version
```javascript
python --version
```
### Install PycharmIDE Proffessional
```javascript
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=macM1
```
## Clone and Open the Project on Pycharm
### Install behave - selenium - allure report
<img width="979" alt="image" src="https://github.com/xuanhavcdn/UploadFeaturesAutomation/assets/24319147/646ded46-2f20-4321-95ce-c14a6048706b">

### Secect Python Interpreter:
<img width="634" alt="image" src="https://github.com/xuanhavcdn/UploadFeaturesAutomation/assets/24319147/70b8bbbe-5c2a-4d7f-95b2-f5435eba5db4">
### Copy file path and change the locator of Upload File base on local device:
<img width="1087" alt="image" src="https://github.com/xuanhavcdn/UploadFeaturesAutomation/assets/24319147/3d63afee-7b23-46a8-b68e-f5b446ec4cd9">
Because of Github limit upload file, so please download the file on and paste on the project forder: https://drive.google.com/drive/folders/1vuwJLsqVIsC8osnNAWnt9dMhWfAzP-ZO?usp=sharing
## Run testUploadFile.feature file
<img width="665" alt="image" src="https://github.com/xuanhavcdn/UploadFeaturesAutomation/assets/24319147/49288574-3af3-4182-ba59-678c0a8cae6c">

## Run test in terminal with Report
```javascript
behave -f allure_behave.formatter:AllureFormatter -o reports/ feature
```
### Generate html report
```javascript
allure serve reports/
```
# Demo video
