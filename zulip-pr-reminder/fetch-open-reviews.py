from github import Github
from datetime import datetime
import json
import pytz
import os

#Git - Zulip name mapping 
git_to_zulip = json.loads(os.getenv('MAP'))

# Set up conncetion to git repository
git = Github(os.getenv('GITHUB_TOKEN'))
repo = git.get_repo('LeoRaasch/pr_reminder_test')

# Fetch open pull requests
pulls = repo.get_pulls(state='open', sort='created')

message = ""
# Create review reminder for each pr
for pr in pulls:
    requested_reviewers = pr.get_review_requests()[0]
    requested_reviewers_name = [reviewer.login for reviewer in requested_reviewers]
    reviews = pr.get_reviews()
    reviewers_name = [review.user.login for review in reviews]

    open_reviewers = [reviewer for reviewer in requested_reviewers_name if reviewer not in reviewers_name]
    open_reviewers_zulip = [git_to_zulip.get(user, f"{user}") for user in open_reviewers]
    open_reviewers_joined = ", ".join(open_reviewers_zulip)

    daysAgo = (datetime.now(pytz.utc) - pr.created_at).days
    stalenessTime = (datetime.now(pytz.utc) - pr.updated_at).days

    if open_reviewers_zulip:
        message += f"[#{pr.number}] [{pr.title}]({pr.html_url}) ({pr.user.login})\n {stalenessTime} days stale - {daysAgo} days old - Waiting on: {open_reviewers_joined}\n"

with open('/home/runner/work/_temp/message.txt', 'w') as file:
    file.write(message.strip())
    
    


