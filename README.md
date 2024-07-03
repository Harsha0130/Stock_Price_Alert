# Stock Price Alert

This project notifies users about significant changes in stock prices using data from Alpha Vantage API and sends alerts via Twilio's SMS API.

-This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course by Dr. Angela Yu.

## Project Overview

### Purpose

Developed a Python script to monitor stock prices (specifically Nvidia Corporation - NVDA) using Alpha Vantage API and send SMS alerts via Twilio when the price change exceeds a certain threshold.

### API Integration

Integrated the Alpha Vantage API (`https://www.alphavantage.co/query`) to fetch daily stock price data for Nvidia Corporation (NVDA) by specifying the stock symbol and API key.

### Stock Price Analysis

Implemented a comparison of the closing prices of the latest two days to calculate the price difference and percentage change. If the percentage change exceeds 5%, the script fetches related news articles using the NewsAPI (`https://newsapi.org/v2/everything`) and sends SMS alerts.

### Twilio Integration

Utilized Twilio's REST API (`twilio.rest.Client`) to send SMS alerts (`client.messages.create`) containing stock price change information and headlines of related news articles.

## Prerequisites

Ensure you have Python installed and install the following libraries:

- requests
- twilio

## Usage

Replace placeholders in the script:
   - Replace `--ACCOUNT_SID--` with your Twilio Account SID.
   - Replace `--AUTH_TOKEN--` with your Twilio Auth Token.
   -  Replace `--NEWS_API_KEY--` with your News API key.
   - Replace `--STOCK_API_KEY--` with your Alpha Vantage API key.

## Screenshot:

![WhatsApp Image 2024-07-03 at 15 31 22_ce369ea9](https://github.com/Harsha0130/Stock_Price_Alert/assets/127675058/46a3d694-0042-4be0-90ee-3560dafa22b6)
