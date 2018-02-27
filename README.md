# twitter-capture-analysis

## Setting up the Project

This program captures tweets using Tweepy, a Python package for accessing the Twitter API, and then analyzes them. To setup the project, clone this repository and run the following command:

    $ cd twitter-capture-analysis

If you haven't done so already, download Python and Tweepy.

## Running the Text Capture

Enter the query search keyword, a from date (must be less than a week old), a to date (must be greater than from date), and number of tweets to retrieve.

    $ python capture.py

The output can be found in the `captures` directory.

## Running the Capture Analysis

Enter the query search keyword from the text capture program and the number of records to display.

    $ python analyze.py

The output can be found in the `analyses` directory. 
