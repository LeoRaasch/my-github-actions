# zulip-pr-reminder

Fetches open pull requests aswell as the missing reviews and sends a pull request reminder into a channel's topic via a bot.

## Inputs

| Name            | Required   | Description                                                                                                                  |
|-----------------|------------|------------------------------------------------------------------------------------------------------------------------------|
| git-token       | Yes        | The Github token of the repository, whose prs should be monitored. Transmit as Github secret.                                |
| mapping         | Yes        | Githubname: Zulipname mappings in JSON format. E.g. {"gitname 1": "@\*\*zulipname 1**", "gitname 2": "@\*\*zulipname 2\*\*"}.|
| bot-api-key     | Yes        | API key of the bot, that should send the message. Transmit as Github secret.                                                 |
| bot-email       | Yes        | Email adress of the bot, that should send the message.                                                                       |
| organization-url| Yes        | URL of the Zulip organization.                                                                                               |
| channel         | No         | Channel that should receive the reminders. The default channel is 'pr-reminders'.                                            |
| topic           | No         | Topic of the channel, that should receive the reminders. The default topic is 'channel events'.                              |
