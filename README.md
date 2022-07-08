# QOTD-Manager
Video Tutorial: https://www.youtube.com/watch?v=DArlLAq56Mo

## Intended Purpose
This program was intended to serve as a means of managing the questions on Headstarters QOTD Bot in these ways:
1. Maintain a list of questions in `questions.txt`, with the question number cooresponding to the line number in the file.
2. Add a list of questions from `input.txt` to the questions list.
3. Using the `requests` library, post the questions to the server

## .env
This program contains an `.env` file which contains the following
- `ID`: Channel ID of a given Discord server. This can be found by right-clicking a channel in Discord and slecting "copy ID" (note that you must have "Developer Mode" enabled to do so. This can be found in Discord settings.)
    - Put in the `.env` file (hidden via the `.gitignore` file) for the sake of privacy.
- `AUTHORITY`: Authorization tag. Go to discord on desktop, click f12, go to request headers -> authorization. This appears to work for any channel from what I can tell.
    - Also put in the `.env` file, although this varaible works for all servers.

## Why It Doesn't Work As Intended
This program doesn't suit its intended purpose, as it posts the commands as a message, rather than it being sent to the bot itself. The program doesn't connect to the bot directly, and I thought that simply posting the command as a message would be interpreted as a command. It does not.

Code from Tutorial Video (with aforementioned `.env` varaibles added): https://github.com/russellelliott/QOTD-Manager/tree/45458d5f91f740a98ccde660f7bdd27cfe52bee4