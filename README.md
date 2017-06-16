# deepThorin
A neural network that mimics a certain user's tweet style.

This project was inspired by deep_cyber.

Credit to https://github.com/sherjilozair/char-rnn-tensorflow for most of the tensorflow code.

Scraping tweets to text:

I used this script to scrape tweets into a json file https://github.com/taspinar/twitterscraper

Our neural network uses a text file as input, so we need to convert the json to a text file.

I wrote a small script json_scrape.py to do that job. It is located in the scrape folder.

Running json_scrape.py will output a text file. Move that file to data/tweets/ and make sure it is named "input.txt".

Now we are ready to start utilizing the RNN to learn how to tweet.

Training the RNN:

The core of the RNN is based on https://github.com/sherjilozair/char-rnn-tensorflow which in turn was based on code written by Andrej Karpathy. You can find more details on how that works, as well as more info on how to customize the parameters, in that repository.

I used 512 hidden layers (as opposed to the original default of 128) which takes a lot longer to train but allowed me to achieve better results than my first attempt at 128. I am just learning so I do not know what the optimal setup would be at this moment. You can customize these in the train.py file, or input the rnn size as a parameter in the command line. The code is currently set up for 512 layers because that is what I used based on a suggestion from deep_cyber.

Running the training script is fairly simple:

1) Go to the folder where your files for this project is stored. Default name is deepThorin.

2) Make sure your data/tweets folder has input.txt in it.

3) Make sure your savetweets folder is empty. This will be where we save the checkpointed model data.

4) Open command line and navigate to your folder.

5) Run: python train.py --data_dir data/tweets --save_dir savetweets/

6) Wait and watch your network train. You will see the train_loss go down over time, exciting!

7) After it is done training, you are ready to start generating text.

Generating text:

To generate text we will use the sample.py script.

Run that in the command line in the same folder:

1) Run: python sample.py --save_dir savetweets

2) Enjoy your generated text!

Note: You can add a prime to the generator to give it the start of a sentence and it will try to complete that sentence. Examine the sample.py file for parameters, as well as elements you can change. For example, you might want to change the numbers of characters it generates.


Currently I am just generating text and then copying the ones I find interesting to another file, and then posting those to the twitter account @deep_thorin manually. This allows me to validate for comprehension and choose the ones I find most interesting. I could write a script to post tweets directly but it might become too spammy, or not interesting enough. Also, at this moment the model lacks polish so some tweets can be hard to comprehend.







