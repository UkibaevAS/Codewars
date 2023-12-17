"""
We all want to climb the leaderboard. Even given some of the massive scores on there, it's nice to know how close you are...

In this kata you will be given a username and their score, your score (not your real score) and you need to calculate
how many kata you need to complete to beat their score, by 1 point exactly.

As this is the easy version (harder one to folow at some point in the future), let's assume only Beta kata and 8kyu
kata are available. Worth 3 and 1 point respectively.

Return a string in this format: "To beat <user>'s score, I must complete <x> Beta kata and <y> 8kyu kata."

If the total number of kata you need to complete >1000, add "Dammit!" to the end of the string, like so:
"To beat <user>'s score, I must complete <x> Beta kata and <y> 8kyu kata. Dammit!"

If your score is higher than the user's already, return "Winning!" and if they are equal, return "Only need one!"

Note: You are looking to complete as few kata as possible to get to your target.
"""


def leader_b(user, user_score, your_score):
    if user_score == your_score:
        return "Only need one!"
    elif user_score < your_score:
        return "Winning!"
    else:
        x_b = (user_score - your_score) // 3
        x_8 = (user_score - your_score) % 3
        text = f"To beat {user}'s score, I must complete {x_b} Beta kata and {x_8} 8kyu kata."
        if x_b + x_8 <= 1000:
            return text
        return text + " Dammit!"