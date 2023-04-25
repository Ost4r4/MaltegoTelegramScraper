# Description
Maltego plugin which is used to find all the accounts forwarded by a Telegram user

## Example of use

![](https://user-images.githubusercontent.com/128547363/233212976-cf17fe5c-3e38-48cf-93f6-4c41cd64026f.gif)
_Loading times have been sped up as part of this gif._

## Installation

Install the necessary libraries

```
pip3 install maltego-trx
pip3 install selenium
```
Start a new project with Maltego-TRX. This will create a new_project directory in your home
```
maltego-trx start new_project
```
Install Chromium
```
sudo apt update ; sudo apt install chromium
```
Download MTS (MaltegoTelegramScraper)
```
git clone https://github.com/Ost4r4/MaltegoTelegramScraper.git
```
Move the script to the directory specific to Maltego-TRX
```
mv MaltegoTelegramScraper/MaltegoTelegramScraper.py new_project/transforms/MaltegoTelegramScraper.py
```
Start Maltego
```
maltego
```
Click on "New Local Transform"

![](https://user-images.githubusercontent.com/128547363/233213562-5bb0dcbe-1847-48b0-bb6f-68ad5985bed0.png)

Fill parameters

![](https://user-images.githubusercontent.com/128547363/233213620-d11103b0-0c0f-45e6-b6fe-8c21d06d39bb.png)

Again

![](https://user-images.githubusercontent.com/128547363/233213666-eacda4b8-11af-4122-a610-fbbc05abe69a.png)

Deploy an alias entity of your choice

![](https://user-images.githubusercontent.com/128547363/233214333-2ab8c3a5-b32e-44e6-b725-9f4b64843cf8.png)

Right-click, choose Local transform and launch the transformation

![](https://user-images.githubusercontent.com/128547363/233214395-659033ad-18cb-4c83-95e8-e8d6c65f2aed.png)

## For further

If you want two or three levels of scrapping, you can either start over or automate it with "machines"

![](https://user-images.githubusercontent.com/128547363/234405271-e6fb2751-4fbc-44f7-9986-8b4a9910cac4.png)

GLHF !
